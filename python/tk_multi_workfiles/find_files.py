# Copyright (c) 2013 Shotgun Software Inc.
# 
# CONFIDENTIAL AND PROPRIETARY
# 
# This work is provided "AS IS" and subject to the Shotgun Pipeline Toolkit 
# Source Code License included in this distribution package. See LICENSE.
# By accessing, using, copying or modifying this work you indicate your 
# agreement to the Shotgun Pipeline Toolkit Source Code License. All rights 
# not expressly granted therein are reserved by Shotgun Software Inc.

def find_all_files(app, work_template, publish_template, context):
    """
    Find files using the 'hook_find_files' hook

    Returned fields should contain:

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
    # call out to hook to provide list of files:
    all_files = app.execute_hook("hook_find_files", 
                                 work_template=work_template, 
                                 publish_template=publish_template, 
                                 context=context)

    if not all_files or not isinstance(all_files, dict):
        return {}
        
    # validate returned files:
    for file_type in ["publish", "work"]:
        files = all_files.get(file_type)
        if files:
            files = [f for f in files if isinstance(f, dict) and "path" in f]
        all_files[file_type] = files
        
    return all_files

