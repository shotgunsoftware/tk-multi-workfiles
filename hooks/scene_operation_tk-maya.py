"""
Copyright (c) 2013 Shotgun Software, Inc
----------------------------------------------------

"""
import os
import maya.cmds as cmds

import tank
from tank import Hook
from tank import TankError
from tank.platform.qt import QtGui

class SceneOperation(Hook):
    """
    Hook called to perform an operation with the
    current scene
    """

    def execute(self, operation, file_path, context, **kwargs):
        """
        Main hook entry point

        :operation: String
                    Scene operation to perform

        :file_path: String
                    File path to use if the operation
                    requires it (e.g. open)

        :context:   Context
                    The context the file operation is being
                    performed in.

        :returns:   Depends on operation:
                    'current_path' - Return the current scene
                                     file path as a String
                    'reset'        - True if scene was reset to an empty
                                     state, otherwise False
                    all others     - None
        """
        if operation == "current_path":
            # return the current scene path
            return cmds.file(query=True, sceneName=True)

        elif operation == "open":
            # do new scene as Maya doesn't like opening
            # the scene it currently has open!
            cmds.file(new=True, force=True)
            cmds.file(file_path, open=True)
            return True

        elif operation == "save":
            # save the current scene:
            cmds.file(save=True)
            return True

        elif operation == "save_as":
            # first rename the scene as file_path:
            cmds.file(rename=file_path)

            # Maya can choose the wrong file type so
            # we should set it here explicitely based
            # on the extension
            maya_file_type = None
            if file_path.lower().endswith(".ma"):
                maya_file_type = "mayaAscii"
            elif file_path.lower().endswith(".mb"):
                maya_file_type = "mayaBinary"

            # save the scene:
            if maya_file_type:
                cmds.file(save=True, force=True, type=maya_file_type)
            else:
                cmds.file(save=True, force=True)
            return True

        elif operation == "scene_modified":
            """
            Returns True if the current scene is dirty
            """
            return cmds.file(query=True, modified=True)

        elif operation == "reset":
            """
            Reset the scene to an empty state.
            Does not check if saving is needed.
            """
            # do new file:
            cmds.file(newFile=True, force=True)
            return True

        else:
            raise TankError("Don't know how to perform scene operation '%s'" % operation)


