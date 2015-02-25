# Copyright (c) 2013 Shotgun Software Inc.
# 
# CONFIDENTIAL AND PROPRIETARY
# 
# This work is provided "AS IS" and subject to the Shotgun Pipeline Toolkit 
# Source Code License included in this distribution package. See LICENSE.
# By accessing, using, copying or modifying this work you indicate your 
# agreement to the Shotgun Pipeline Toolkit Source Code License. All rights 
# not expressly granted therein are reserved by Shotgun Software Inc.

# The Modo engine is not supported by Shotgun but has been graciously
# contributed to the community by Walking The Dog and Lutz Paelike.
# It can be found at:
# https://github.com/tremolo/tk-modo

import os

import tank
from tank import Hook
from tank import TankError
from tank.platform.qt import QtGui


class SceneOperation(Hook):
    """
    Hook called to perform an operation with the 
    current scene
    """
    
    def execute(self, operation, file_path, context, parent_action, file_version, read_only, **kwargs):
        """
        Main hook entry point
        
        :param operation:       String
                                Scene operation to perform
        
        :param file_path:       String
                                File path to use if the operation
                                requires it (e.g. open)
                    
        :param context:         Context
                                The context the file operation is being
                                performed in.
                    
        :param parent_action:   This is the action that this scene operation is
                                being executed for.  This can be one of:
                                - open_file
                                - new_file
                                - save_file_as 
                                - version_up
                        
        :param file_version:    The version/revision of the file to be opened.  If this is 'None'
                                then the latest version should be opened.
        
        :param read_only:       Specifies if the file should be opened read-only or not
                            
        :returns:               Depends on operation:
                                'current_path' - Return the current scene
                                                 file path as a String
                                'reset'        - True if scene was reset to an empty 
                                                 state, otherwise False
                                all others     - None
        """
        import modoshotgunsupport
        
        if operation == "current_path":
            return modoshotgunsupport.get_scene_filename()
        elif operation == "open":
            modoshotgunsupport.load_file(file_path )
        elif operation == "save":
            modoshotgunsupport.save_scene()
        elif operation == "save_as":
            modoshotgunsupport.save_scene_as(file_path)
        elif operation == "reset":
            try:
                modoshotgunsupport.reset_scene()
                return  True
            except:
                return False

