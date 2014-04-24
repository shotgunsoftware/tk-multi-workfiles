"""
Copyright (c) 2013 Shotgun Software, Inc
----------------------------------------------------

"""
import os
import c4d

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
            doc = c4d.documents.GetActiveDocument()
            scene_path = os.path.join(doc.GetDocumentPath(),
                                      doc.GetDocumentName())
            return scene_path

        elif operation == "open":
            # do new scene as Maya doesn't like opening
            # the scene it currently has open!
            c4d.documents.LoadFile(file_path)

        elif operation == "save":
            # save the current scene:
            doc = c4d.documents.GetActiveDocument()
            scene_path = os.path.join(doc.GetDocumentPath(),
                                      doc.GetDocumentName())
            c4d.documents.SaveDocument(c4d.documents.GetActiveDocument(),
                                       scene_path, c4d.SAVEDOCUMENTFLAGS_0,
                                       c4d.FORMAT_C4DEXPORT)

        elif operation == "save_as":
            # first rename the scene as file_path:
            c4d.documents.SaveDocument(c4d.documents.GetActiveDocument(),
                                       file_path, c4d.SAVEDOCUMENTFLAGS_0,
                                       c4d.FORMAT_C4DEXPORT)
            c4d.documents.LoadFile(file_path)

        elif operation == "reset":
            """
            Reset the scene to an empty state
            """
            doc = c4d.documents.GetActiveDocument()
            while doc.GetChanged():
                # changes have been made to the scene
                res = QtGui.QMessageBox.question(None,
                                                 "Save your scene?",
                                                 "Your scene has unsaved "
                                                 "changes. Save before "
                                                 "proceeding?",
                                                 QtGui.QMessageBox.Yes |
                                                 QtGui.QMessageBox.No |
                                                 QtGui.QMessageBox.Cancel)

                if res == QtGui.QMessageBox.Cancel:
                    return False
                elif res == QtGui.QMessageBox.No:
                    break
                else:
                    scene_name = doc.GetDocumentName()
                    if not scene_name:
                        c4d.documents.SaveDocument(
                            c4d.documents.GetActiveDocument(), "",
                            c4d.SAVEDOCUMENTFLAGS_SAVEAS, c4d.FORMAT_C4DEXPORT)
                    else:
                        doc = c4d.documents.GetActiveDocument()
                        scene_path = os.path.join(doc.GetDocumentPath(),
                                                  doc.GetDocumentName())
                        c4d.documents.SaveDocument(
                            c4d.documents.GetActiveDocument(), scene_path,
                            c4d.SAVEDOCUMENTFLAGS_0, c4d.FORMAT_C4DEXPORT)

            # do new file:
            c4d.documents.KillDocument(c4d.documents.GetActiveDocument())
            return True
        else:
            raise TankError("Don't know how to perform scene operation "
                            "'%s'" % operation)
