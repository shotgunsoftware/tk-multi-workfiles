# Copyright (c) 2015 Shotgun Software Inc.
# 
# CONFIDENTIAL AND PROPRIETARY
# 
# This work is provided "AS IS" and subject to the Shotgun Pipeline Toolkit 
# Source Code License included in this distribution package. See LICENSE.
# By accessing, using, copying or modifying this work you indicate your 
# agreement to the Shotgun Pipeline Toolkit Source Code License. All rights 
# not expressly granted therein are reserved by Shotgun Software Inc.

import sgtk
from sgtk.platform.qt import QtCore, QtGui

models = sgtk.platform.import_framework("tk-framework-qtwidgets", "models")
HierarchicalFilteringProxyModel = models.HierarchicalFilteringProxyModel

class EntityProxyModel(HierarchicalFilteringProxyModel):
    """
    """
    
    def __init__(self, compare_sg_fields=None, parent=None):
        """
        """
        HierarchicalFilteringProxyModel.__init__(self, parent)
        self._compare_fields = compare_sg_fields
                   
    def _is_item_accepted(self, item, parent_accepted):
        """
        """
        # if the parent is accepted then this node is accepted by default:
        if parent_accepted:
            return True 
        
        reg_exp = self.filterRegExp()
        if reg_exp.isEmpty():
            # early out
            return True        
        
        # test to see if the item 'text' matches:
        if reg_exp.indexIn(item.text()) != -1:
            # found a match so early out!
            return True

        if self._compare_fields:
            # see if we have sg data:
            sg_data = item.get_sg_data()
            if sg_data:
                return self._sg_data_matches_r(sg_data, self._compare_fields, reg_exp)
        
        # default is to not match!
        return False
                    
    def _sg_data_matches_r(self, sg_data, compare_fields, reg_exp):
        """
        """
        if isinstance(compare_fields, list):
            # e.g. ["one", "two", {"three":"four", "five":["six", "seven"]}]
            for cf in compare_fields:
                if isinstance(cf, dict):
                    # e.g. {"three":"four", "five":["six", "seven"]}
                    for key, value in cf.iteritems():
                        data = sg_data.get(key)
                        if data:
                            if self._sg_data_matches_r(data, value, reg_exp):
                                return True
                else:
                    # e.g. "one"
                    if self._sg_data_matches_r(sg_data, cf, reg_exp):
                        return True
        else:
            # e.g. "one"
            val = sg_data.get(compare_fields)
            if val and reg_exp.indexIn(val) != -1:
                return True
            
        return False
