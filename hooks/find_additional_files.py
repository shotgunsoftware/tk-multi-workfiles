# Copyright (c) 2013 Shotgun Software Inc.
# 
# CONFIDENTIAL AND PROPRIETARY
# 
# This work is provided "AS IS" and subject to the Shotgun Pipeline Toolkit 
# Source Code License included in this distribution package. See LICENSE.
# By accessing, using, copying or modifying this work you indicate your 
# agreement to the Shotgun Pipeline Toolkit Source Code License. All rights 
# not expressly granted therein are reserved by Shotgun Software Inc.

import sgtk
from sgtk import Hook

class FindAdditionalFiles(Hook):
    """
    Hook that can be used to return a list of additional files
    to display in the file list
    """
    
    def execute(self, **kwargs):
        """
        Main hook entry point
        
        :blah:   String
                 blah blah blah
                        
        """
        
        # default implementation doesn't return any additional files
        return None