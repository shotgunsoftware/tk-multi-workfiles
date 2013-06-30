"""
Copyright (c) 2013 Shotgun Software, Inc
----------------------------------------------------

"""
import os
import nuke

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

        if file_path:
            file_path = file_path.replace("/", os.path.sep)

        if operation == "current_path":
            # return the current script path
            scene_name = nuke.root().name()
            if scene_name == "Root":
                return ""
            return scene_name.replace("/", os.path.sep)

        elif operation == "open":
            # open the specified script
            nuke.scriptOpen(file_path)

            # reset any write node render paths:
            if self._reset_write_node_render_paths():
                # something changed so make sure to save the script again:
                nuke.scriptSave()
            return True

        elif operation == "save":
            # save the current script:
            nuke.scriptSave()

        elif operation == "save_as":
            old_path = nuke.root()["name"].value()
            try:
                # rename script:
                nuke.root()["name"].setValue(file_path)

                # reset all write nodes:
                self._reset_write_node_render_paths()

                # save script:
                nuke.scriptSaveAs(file_path, -1)
            except Exception, e:
                # something went wrong so reset to old path:
                nuke.root()["name"].setValue(old_path)
                raise TankError("Failed to save scene %s", e)
            return True

        elif operation == "scene_modified":
            """
            Returns True if the current scene is dirty
            """
            return nuke.root().modified()

        elif operation == "reset":
            """
            Reset the scene to an empty state.
            Does not check if saving is needed.
            """
            # now clear the script:
            nuke.scriptClear()
            nuke.createNode("Viewer")
            return True

        else:
            raise TankError("Don't know how to perform scene operation '%s'" % operation)


    def _reset_write_node_render_paths(self):
        """
        Use the tk-nuke-writenode app interface to find and reset
        the render path of any Tank write nodes in the current script
        """
        write_node_app = self.parent.engine.apps.get("tk-nuke-writenode")
        if not write_node_app:
            return

        write_nodes = write_node_app.get_write_nodes()
        for write_node in write_nodes:
            write_node_app.reset_node_render_path(write_node)

        return len(write_nodes) > 0


