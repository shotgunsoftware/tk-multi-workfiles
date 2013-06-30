"""
Copyright (c) 2013 Shotgun Software, Inc
----------------------------------------------------

"""
import os

import tank
from tank import Hook
from tank import TankError

import win32com
from win32com.client import Dispatch, constants
from pywintypes import com_error

Application = Dispatch("XSI.Application").Application


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
                    'reset'        - True if scene was reset to an empty
                                     state, otherwise False
                    all others     - None
        """

        if operation == "current_path":
            # return the current scene path
            scene_name = Application.ActiveProject.ActiveScene.Name
            scene_filename = Application.ActiveProject.ActiveScene.filename.value
            # If the scene name is "Scene" rather than "Untitled", we can be reasonably
            # sure that we haven't opened a file called Untitled.scn
            if scene_name == "Scene" and os.path.basename(scene_filename) == "Untitled.scn":
                return ""
            return scene_filename

        elif operation == "open":
            # open the specified scene
            Application.OpenScene(file_path, 0, 0)
            return True

        elif operation == "save":
            # save the current scene:
            Application.SaveScene()
            return True

        elif operation == "save_as":
            # save the scene as file_path:
            Application.SaveSceneAs(file_path, 0)
            return True

        elif operation == "scene_modified":
            """
            Returns True if the current scene is dirty
            """
            dirty_count = Application.GetValue("Project.dirtycount")
            if dirty_count:
                return True
            for model in Application.ActiveSceneRoot.Models:
                dirty_count = model.GetPropertyFromName("dirty_count")
                if dirty_count:
                    return True
            return False

        elif operation == "reset":
            """
            Reset the scene to an empty state.
            Does not check if saving is needed.
            """
            # reset the scene to an empty state
            Application.NewScene("", 0)
            return True

        else:
            raise TankError("Don't know how to perform scene operation '%s'" % operation)
