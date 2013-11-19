# Copyright (c) 2013 Shotgun Software Inc.
# 
# CONFIDENTIAL AND PROPRIETARY
# 
# This work is provided "AS IS" and subject to the Shotgun Pipeline Toolkit 
# Source Code License included in this distribution package. See LICENSE.
# By accessing, using, copying or modifying this work you indicate your 
# agreement to the Shotgun Pipeline Toolkit Source Code License. All rights 
# not expressly granted therein are reserved by Shotgun Software Inc.

import os

import sgtk
from sgtk import Hook

class FindFiles(Hook):
    """
    Hook that can be used to return a list of files to display in the file list
    """
    
    def execute(self, file_type, work_template, publish_template, context, **kwargs):
        """
        Main hook entry point
        
        :blah:   String
                 blah blah blah
           
        Common fields:
    
            # required
            path
            key
            
            # optional
            version
            name
            task
            description
            
        Additional published file fields:
        
            thumbnail
            published_at
            published_by
            published_file_entity_id    
                        
        """
        if file_type == "published_files":
            # return a list of published files matching the publish template and context
            return self._find_published_files(work_template, publish_template, context)
        elif file_type == "work_files":
            # return a list of work files matching the work template and context
            return self._find_work_files(work_template, context)
            
            
    def _find_published_files(self, work_template, publish_template, context):
        """
        """
        # early out if no publish template specified:
        if not publish_template:
            return []
        
        # get list of published files for entity from Shotgun:
        sg_filters = [["entity", "is", context.entity or context.project]]
        if context.task:
            sg_filters.append(["task", "is", context.task])
        published_file_entity_type = sgtk.util.get_published_file_entity_type(self.parent.sgtk)
        sg_fields = ["id", "description", "version_number", "image", "created_at", "created_by", "name", "path", "task"]
        sg_res = self.parent.shotgun.find(published_file_entity_type, sg_filters, sg_fields)
        
        # will need the context fields for the work template:
        ctx_fields = context.as_template_fields(work_template)
        
        published_files = []
        for sg_file in sg_res:
            if not sg_file.get("path"):
                # don't care about files without a path!
                continue
            
            # only care about local paths:
            path = sg_file.get("path").get("local_path")

            # make sure path matches publish template:            
            if not publish_template.validate(path):
                continue

            # parse the publish fields:
            fields = publish_template.get_fields(path)
                
            file_details = {"path":path}
            
            # add in details from sg record:
            file_details["version"] = sg_file.get("version_number") or fields.get("version")
            file_details["task"] = sg_file.get("task")
            file_details["thumbnail"] = sg_file.get("image")
            file_details["published_at"] = sg_file.get("created_at")
            file_details["published_by"] = sg_file.get("created_by", {})
            file_details["description"] = sg_file.get("description")
            file_details["published_file_entity_id"] = sg_file.get("id")                   
            
            file_details["name"] = self._get_file_display_name(path, publish_template, fields)
            
            # construct a unique key used to match up all versions of publish & work files:
            fields["version"] = 0
            key = work_template.apply_fields(dict(chain(ctx_fields.iteritems(), fields.iteritems())))
            file_details["key"] = key
            
            # append to published files list:
            published_files.append(file_details)
            
        return published_files

    def _find_work_files(self, work_template, context):
        """
        """
        # find work files that match the current work template:
        try:
            work_fields = context.as_template_fields(work_template)
        except TankError:
            # could not resolve fields from this context. This typically happens
            # when the context object does not have any corresponding objects on 
            # disk / in the path cache. In this case, we cannot continue with any
            # file system resolution, so basically just exit early insted.
            return []
        
        work_file_paths = self.parent.sgtk.paths_from_template(work_template, work_fields, ["version"], 
                                                             skip_missing_optional_keys=True)
        
        # and find additional details for each path:
        work_files = []
        for path in work_file_paths:
            file_details = {"path":path}

            # add details from the template fields:
            fields = work_template.get_fields(path)
            if "version" in fields:
                file_details["version"] = fields["version"]
            else:
                file_details["version"] = None
                
            file_details["name"] = self._get_file_display_name(path, work_template, fields)
            
            # get the task:
            if context.task:
                file_details["task"] = context.task
            else:
                # try to create a context from the path and see if that contains a task:
                wf_ctx = self.parent.sgtk.context_from_path(path, context)
                if wf_ctx and wf_ctx.task:
                    file_details["task"] = wf_ctx.task 
            
            # description is empty:
            file_details["description"] = ""
            
            # construct a unique key used to match up all versions of publish & work files:
            key_fields = fields.copy()
            key_fields["version"] = 0            
            key = work_template.apply_fields(key_fields)
            file_details["key"] = key
            
            # and append to the file list:
            work_files.append(file_details)
        
        return work_files
    
    def _get_file_display_name(self, path, template, fields=None):
        """
        Return the 'name' to be used for the file - if possible
        this will return a 'versionless' name
        """
        # first, extract the fields from the path using the template:
        fields = fields.copy() if fields else template.get_fields(path)
        if "name" in fields and fields["name"]:
            # well, that was easy!
            name = fields["name"]
        else:
            # find out if version is used in the file name:
            template_name, _ = os.path.splitext(os.path.basename(template.definition))
            version_in_name = "{version}" in template_name
        
            # extract the file name from the path:
            name, _ = os.path.splitext(os.path.basename(path))
            delims_str = "_-. "
            if version_in_name:
                # looks like version is part of the file name so we        
                # need to isolate it so that we can remove it safely.  
                # First, find a dummy version whose string representation
                # doesn't exist in the name string
                version_key = template.keys["version"]
                dummy_version = 9876
                while True:
                    test_str = version_key.str_from_value(dummy_version)
                    if test_str not in name:
                        break
                    dummy_version += 1
                
                # now use this dummy version and rebuild the path
                fields["version"] = dummy_version
                path = template.apply_fields(fields)
                name, _ = os.path.splitext(os.path.basename(path))
                
                # we can now locate the version in the name and remove it
                dummy_version_str = version_key.str_from_value(dummy_version)
                
                v_pos = name.find(dummy_version_str)
                # remove any preceeding 'v'
                pre_v_str = name[:v_pos].rstrip("v")
                post_v_str = name[v_pos + len(dummy_version_str):]
                
                if (pre_v_str and post_v_str 
                    and pre_v_str[-1] in delims_str 
                    and post_v_str[0] in delims_str):
                    # only want one delimiter - strip the second one:
                    post_v_str = post_v_str.lstrip(delims_str)

                versionless_name = pre_v_str + post_v_str
                versionless_name = versionless_name.strip(delims_str)
                
                if versionless_name:
                    # great - lets use this!
                    name = versionless_name
                else: 
                    # likely that version is only thing in the name so 
                    # instead, replace the dummy version with #'s:
                    zero_version_str = version_key.str_from_value(0)        
                    new_version_str = "#" * len(zero_version_str)
                    name = name.replace(dummy_version_str, new_version_str)
        
        return name 
    
       