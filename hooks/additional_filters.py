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

class AdditionalFilters(Hook):
    """
    Hook that can be used to return a list of additional filters
    to display in the filter list
    """
    
    def execute(self, **kwargs):
        """
        Main hook entry point
        
        :blah:   String
                 blah blah blah
                        
        """
        
        ## default implementation doesn't return any additional filters
        #return None
    
        additional_filters = []
    
        additional_filters.append({"menu_label":"Show Files in the Perforce Depot", 
                                "list_title":"Available Depot Files",
                                "show_in_file_system":False,
                                "mode":"publishes"})
        
        return additional_filters