"""
Copyright (c) 2013 Shotgun Software, Inc
----------------------------------------------------

Multi Publish

"""

import os
import tank
from tank import TankError

class MultiWorkFiles(tank.platform.Application):

    def init_app(self):
        """
        Called as the application is being initialized
        """

        tk_multi_workfiles = self.import_module("tk_multi_workfiles")

        # register commands:
        self._work_files_handler = tk_multi_workfiles.WorkFiles(self)
        self.engine.register_command("Tank File Manager...", self._work_files_handler.show_dlg)

        self._save_as_handler = tk_multi_workfiles.SaveAs
        self._versioning_handler = tk_multi_workfiles.Versioning

        # other commands are only valid if we have valid work and publish templates:
        if self.can_save_as():
            cmd = lambda app=self: app.show_save_as_dlg()
            self.engine.register_command("Tank Save As...", cmd)

            cmd = lambda app=self: app.show_change_version_dlg()
            self.engine.register_command("Version up Current Scene...", cmd)

    def destroy_app(self):
        self.log_debug("Destroying tk-multi-workfiles")
        self._work_files_handler = None
        self._save_as_handler = None
        self._versioning_handler = None

    def show_save_as_dlg(self):
        """
        If save as is available, will show the save as dialog.
        """
        if self.can_save_as():
            return self._save_as_handler.show_save_as_dlg(self)
        return False

    def show_change_version_dlg(self):
        """
        If save as is available, will show the change version dialog.
        """
        if self.can_save_as():
            return self._versioning_handler.show_change_version_dlg(self)
        return False

    def can_save_as(self):
        """
        Returns True if save as is available, False otherwise.
        """
        if self.get_template("template_work") and self.get_template("template_publish"):
            return True
        return False
