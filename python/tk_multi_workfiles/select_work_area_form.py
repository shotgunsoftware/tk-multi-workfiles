"""
Copyright (c) 2013 Shotgun Software, Inc
----------------------------------------------------
"""
import os
import sys
import threading

import tank
from tank.platform.qt import QtCore, QtGui

from .task_browser import TaskBrowserWidget
from .new_task import NewTaskDialog

class SelectWorkAreaForm(QtGui.QWidget):

    def __init__(self, app, handler, parent=None):
        """
        Construction
        """
        QtGui.QWidget.__init__(self, parent)

        self._app = app
        self._handler = handler

        self.change_context_mode = False

        self._exit_code = QtGui.QDialog.Rejected
        self._settings = QtCore.QSettings("Shotgun Software", "tk-multi-workfiles")

        # set up the UI
        from .ui.select_work_area_form import Ui_SelectWorkAreaForm
        self._ui = Ui_SelectWorkAreaForm()
        self._ui.setupUi(self)

        # set up the entity browser:
        self._ui.entity_browser.set_app(self._app)
        self._ui.entity_browser.selection_changed.connect(self._on_entity_selected)

        types_to_load = self._app.get_setting("sg_entity_types", [])
        types_str = "Entities"
        if types_to_load:
            types_nice_names = [ tank.util.get_entity_type_display_name(self._app.tank, x) for x in types_to_load ]

            plural_types = [ "%ss" % x for x in types_nice_names] # no fanciness (sheep, box, nucleus etc)
            if len(plural_types) == 1:
                # "Shots"
                types_str = plural_types[0]
            else:
                # "Shots, Assets & Sequences"
                types_str = ", ".join(plural_types[:-1])
                types_str += " & %s" % plural_types[-1]
        self._ui.entity_browser.set_label(types_str)

        # set up the task browser:
        self._ui.task_browser.set_app(self._app)
        self._ui.task_browser.selection_changed.connect(self._on_task_selected)
        self._ui.task_browser.action_requested.connect(self._on_context_selected)
        self._ui.task_browser.set_label("Tasks")

        # connect the buttons:
        self._ui.select_btn.clicked.connect(self._on_context_selected)
        self._ui.cancel_btn.clicked.connect(self._on_cancel)

        #TODO: implement task creation!
        can_create_tasks = self._app.get_setting("allow_task_creation")
        if can_create_tasks:
            self._ui.new_task_btn.clicked.connect( self._on_create_new_task )
        else:
            self._ui.new_task_btn.setVisible(False)

        # set up the 'Only Show My Tasks' checkbox:
        self._ui.mine_only_cb.toggled.connect(self._on_mine_only_cb_toggled)
        try:
            # this qsettings stuff seems super flaky on different platforms
            # - although setting is saved as an int, it can get loaded as either an
            # int or a string, hence the double casting to int and then bool.
            show_mine_only = bool(int(self._settings.value("show_mine_only", True)))
            self._ui.mine_only_cb.setChecked(show_mine_only)
        except Exception, e:
            self._app.log_warning("Cannot restore state of 'Only Show My Tasks' checkbox: %s" % e)

        # reload:
        ctx = self._handler.get_current_work_area()
        self._initial_task_to_select = ctx.task if ctx else None
        self._reload_entities(ctx.entity if ctx else None)

    @property
    def exit_code(self):
        return self._exit_code

    @property
    def context(self):
        return self._get_context()

    def closeEvent(self, event):
        """
        Make sure that the various background threads are closed
        """
        self._ui.entity_browser.destroy()
        self._ui.task_browser.destroy()
        # okay to close!
        event.accept()

    def _on_cancel(self):
        self._exit_code = QtGui.QDialog.Rejected
        self.close()

    def _on_context_selected(self):
        if self.change_context_mode:
            self._do_change_context()
        else:
            self._exit_code = QtGui.QDialog.Accepted
            self.close()

    def _on_create_new_task(self):
        """
        Called when new task button is clicked
        """
        curr_selection = self._ui.entity_browser.selected_entity
        if curr_selection is None:
                QtGui.QMessageBox.warning(self,
                                          "Please select an Entity!",
                                          "Please select an Entity that you want to add a Task to.")
                return

        # do new task
        new_task = NewTaskDialog(self._app, curr_selection, self)
        # need to keep the reference alive otherwise the window is destroyed
        if new_task.exec_() == QtGui.QDialog.Accepted:
            # do it!
            task_id = new_task.create_task()

            # refresh - in case they cancel the context set, the dialog is up to date.
            self._reload_tasks()

            # and set the context to point here!
            # self._on_context_selected()

    def _get_context(self):
        """
        Return a context for the current selection
        """

        # get the selected task:
        task = self._ui.task_browser.selected_task

        # try to create a context:
        ctx = None
        if task:
            ctx = self._app.tank.context_from_entity("Task", task.get("id"))
        else:
            # no task selected so use entity instead:
            entity = self._ui.entity_browser.selected_entity
            if entity:
                ctx = self._app.tank.context_from_entity(entity.get("type"), entity.get("id"))

        return ctx

    def _on_mine_only_cb_toggled(self):
        """
        Called when mine-only checkbox is toggled
        """
        # remember setting - save value as an int as this
        # can be handled across all operating systems!
        # - on Windows & Linux, boolean & int settings are
        # returned as strings when queried!
        show_mine_only = self._ui.mine_only_cb.isChecked()
        self._settings.setValue("show_mine_only", int(show_mine_only))

        # reload entity list:
        self._reload_entities()


    def _on_entity_selected(self):
        """
        Called when the selected entity is changed
        """
        self._reload_tasks()

    def _on_task_selected(self):
        """
        Called when the selected task is changed
        """
        self._update_ui()

    def _reload_entities(self, entity_to_select = None):
        """
        Called to reload the list of entities
        """
        if not entity_to_select:
            entity_to_select = self._ui.entity_browser.selected_entity
            self._initial_task_to_select = None

        # clear both entity and task lists:
        self._ui.entity_browser.clear()
        self._ui.task_browser.clear()

        # reload entities:
        d = {}
        d["own_tasks_only"] = self._ui.mine_only_cb.isChecked()
        d["entity"] = entity_to_select
        self._ui.entity_browser.load(d)

    def _reload_tasks(self):
        """
        Called to reload the list of tasks based on the
        currently selected entity
        """
        self._ui.task_browser.clear()

        curr_selection = self._ui.entity_browser.get_selected_item()
        if curr_selection is None:
            self._ui.task_browser.set_message("Please select an item in the listing to the left.")
            self._update_ui()
            return

        task_to_select = self._ui.task_browser.selected_task
        if not task_to_select:
            task_to_select = self._initial_task_to_select

        # pass in data to task retreiver
        d = {}
        d["own_tasks_only"] = self._ui.mine_only_cb.isChecked()
        d["entity"] = curr_selection.sg_data
        d["task"] = task_to_select

        # pass in the sg data dump for the entity to the task loader code
        self._ui.task_browser.load(d)

        self._update_ui()

    def _do_change_context(self):
        """
        Set context based on selected task
        """

        if not self.context.task:
            return

        task_id = self.context.task.get("id")
        try:
            ctx = self._app.tank.context_from_entity("Task", task_id)
        except Exception, e:
            QtGui.QMessageBox.critical(self,
                                       "Cannot Resolve Task!",
                                       "Cannot resolve this task into a context: %s" % e)
            return

        message = QtGui.QMessageBox()
        message.setIcon(QtGui.QMessageBox.Question)

        yes_new_scene_button = message.addButton("Yes And New Scene", QtGui.QMessageBox.YesRole)

        message.addButton(QtGui.QMessageBox.Yes)
        message.addButton(QtGui.QMessageBox.No)
        message.setDefaultButton(QtGui.QMessageBox.Yes)
        message.setEscapeButton(QtGui.QMessageBox.No)
        message.setWindowTitle("Change Context?")
        message.setText("This will switch your work area to the "
                      "selected Task. Are you sure you want to continue?")

        res = message.exec_()
        if res == QtGui.QMessageBox.No:
            return

        if message.clickedButton() == yes_new_scene_button:
            if not self._handler.reset_current_scene():
                self._app.log_debug("Unable to perform New Scene operation after failing to reset scene!")
                return

        # note - on nuke, we always start from a clean scene, so no need to check.

        # ok scene is clear. Now switch!

        # Try to create path for the context.
        try:
            self._handler.create_folders(ctx)
            self._handler.restart_engine(ctx)
        except Exception, e:
            QtGui.QMessageBox.critical(self,
                                       "Could not Switch!",
                                       "Could not change work area and start a new "
                                       "engine. This can be because the task doesn't "
                                       "have a step. Details: %s" % e)
            return


        # close dialog
        self.close()

    def _update_ui(self):
        """
        Update UI following a change
        """
        current_entity = self._ui.entity_browser.selected_entity
        self._ui.select_btn.setEnabled(current_entity is not None)
