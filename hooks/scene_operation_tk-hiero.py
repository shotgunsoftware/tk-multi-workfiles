
import os
import hiero

import tank
from tank import Hook
from tank import TankError
from tank.platform.qt import QtGui

class SceneOperation(Hook):
    """
    Hook called to perform an operation with the 
    current scene
    """
    
    def execute(self, operation, file_path, **kwargs):
        """
        Main hook entry point
        
        :operation: String
                    Scene operation to perform
        
        :file_path: String
                    File path to use if the operation
                    requires it (e.g. open)
                    
        :returns:   Depends on operation:
                    'current_path' - Return the current scene
                                     file path as a String
                    all others     - None
        """
        
        if file_path:
            file_path = file_path.replace("/", os.path.sep)
        
        if operation == "current_path":
            # return the current project path
            project = hiero.core.projects()[-1]
            return project.path()
        
        elif operation == "open":
            # open the specified project
            hiero.core.closeAllProjects(False)
            hiero.core.openProject(file_path)
            
        elif operation == "save":
            # save the current project
            project = hiero.core.projects()[-1]
            project.save()
            
        elif operation == "save_as":
            project = hiero.core.projects()[-1]
            project.saveAs(file_path)
            
        elif operation == "reset":
            # reset the project to an empty state
            hiero.core.closeAllProjects(False)
            hiero.core.newProject()
            
