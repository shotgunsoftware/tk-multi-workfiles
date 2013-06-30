"""
Copyright (c) 2013 Shotgun Software, Inc
----------------------------------------------------

"""
import os
from Py3dsMax import mxs

import tank
from tank import Hook
from tank import TankError

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
            """
            Returns the current scene path
            """
            if not mxs.maxFileName:
                return ""
            return os.path.join(mxs.maxFilePath, mxs.maxFileName)

        elif operation == "open":
            # open the specified scene
            mxs.loadMaxFile(file_path)
            return True

        elif operation == "save":
            # save the current scene:
            file_path = os.path.join(mxs.maxFilePath, mxs.maxFileName)
            mxs.saveMaxFile(file_path)
            return True

        elif operation == "save_as":
            # save the scene as file_path:
            mxs.saveMaxFile(file_path)
            return True

        elif operation == "scene_modified":
            """
            Returns True if the current scene is dirty
            """
            return mxs.getSaveRequired()

        elif operation == "reset":
            """
            Reset the scene to an empty state.
            Does not check if saving is needed.
            """
            # now reset the scene:
            mxs.resetMAXFile(mxs.pyhelper.namify("noPrompt"))

            return True

        else:
            raise TankError("Don't know how to perform scene operation '%s'" % operation)
