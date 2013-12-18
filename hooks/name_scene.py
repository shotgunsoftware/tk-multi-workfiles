import tank
from tank import Hook
import shutil
import os

class NameScene(Hook):
    """
    Hook called when a file needs to be named
    """
    
    def execute(self, app, context, **kwargs):
        """
        Main hook entry point
        
        :app:   String
                Source file path to copy
        :context: Context
                The context the file operation is being
                performed in.
        """
        
        default_name = app.get_setting("saveas_default_name")
        return default_name      