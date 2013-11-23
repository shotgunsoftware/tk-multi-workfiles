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
    
    def execute(self, work_template, publish_template, context, **kwargs):
        """
        Main hook entry point
        
        :blah:   String
                 blah blah blah
           
        The list of returned files should contain the following fields:
        
            # required
            path
                
            # optional
            version
            thumbnail
            name
            task
            description
            
            # additional published file fields:
            published_at
            published_by
            published_file_entity_id  
                        
        """
        all_files = {}
        all_files["publish"] = self._find_published_files(publish_template, context)
        all_files["work"] = self._find_work_files(work_template, context)
        return all_files
            
    def _find_published_files(self, publish_template, context):
        """
        """
        # get list of published files for the context from Shotgun:
        sg_filters = [["entity", "is", context.entity or context.project]]
        if context.task:
            sg_filters.append(["task", "is", context.task])
        published_file_entity_type = sgtk.util.get_published_file_entity_type(self.parent.sgtk)
        sg_fields = ["id", "description", "version_number", "image", "created_at", "created_by", "name", "path", "task"]
        sg_res = self.parent.shotgun.find(published_file_entity_type, sg_filters, sg_fields)
        
        published_files = []
        for sg_file in sg_res:
            if not sg_file.get("path"):
                # don't care about files without a path!
                continue
            
            # get the local path:
            path = sg_file.get("path").get("local_path")

            # make sure path matches the publish template:            
            if not publish_template.validate(path):
                continue

            file_details = {"path":path}
            
            # add in details from sg record:
            file_details["version"] = sg_file.get("version_number")
            file_details["name"] = sg_file.get("name")
            file_details["task"] = sg_file.get("task")
            file_details["description"] = sg_file.get("description")
            file_details["thumbnail"] = sg_file.get("image")
            
            file_details["published_at"] = sg_file.get("created_at")
            file_details["published_by"] = sg_file.get("created_by", {})
            file_details["published_file_entity_id"] = sg_file.get("id")                   
            
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
            # file system resolution, so just exit early insted.
            return []
        
        # return all versions so we want to skip the version key
        work_file_paths = self.parent.sgtk.paths_from_template(work_template, work_fields, ["version"], 
                                                             skip_missing_optional_keys=True)
        
        # and find additional details for each path:
        work_files = []
        for path in work_file_paths:
            file_details = {"path":path}
            
            # description is empty:
            file_details["description"] = None
            
            # and append to the file list:
            work_files.append(file_details)
        
        return work_files
    
       