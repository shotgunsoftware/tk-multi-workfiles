"""
Copyright (c) 2012 Shotgun Software, Inc
----------------------------------------------------
"""
import tank
import os
import sys
import threading

from tank.platform.qt import QtCore, QtGui
from .ui.new_task import Ui_NewTask

class NewTaskDialog(QtGui.QDialog):

    
    def __init__(self, app, entity, parent):
        QtGui.QDialog.__init__(self, parent)
        self._app = app
        # set up the UI
        self.ui = Ui_NewTask() 
        self.ui.setupUi(self)
        
        self._entity = entity
        
        # populate entity name
        entity_name = "%s %s" % (self._entity["type"], self._entity["code"])
        self.ui.entity.setText(entity_name)
        
        # populate user
        self._curr_user = tank.util.get_shotgun_user(self._app.shotgun)
        if self._curr_user is None:
            username = "<unassigned>"
        else:
            username = self._curr_user["name"]
        self.ui.assigned_to.setText(username)
        
        # populate pipeline steps
        data = self._app.shotgun.find("Step", 
                                      [["entity_type", "is", self._entity["type"]]],
                                      ["code", "id"])
        
        self._pipeline_step_dict = {}
        for x in data:
            step_name = x.get("code")
            if step_name is None:
                step_name = "Unnamed Step"
            self.ui.pipeline_step.addItem(step_name, step_name)
            self._pipeline_step_dict[x.get("code", "")] = x.get("id")
        
        # try to figure out a default pipeline step and task name
        if self._app.context.step:
            step_name = self._app.context.step["name"]
            idx = self.ui.pipeline_step.findData(step_name)
            if idx != -1:
                self.ui.pipeline_step.setCurrentIndex(idx)
            self.ui.task_name.setText(step_name)
        
        
    def create_task(self):
        
        # creates a new task. returns the task id or none on failure
        
        # get pipeline step id from the dropdown
        pipeline_step_id = self._pipeline_step_dict[self.ui.pipeline_step.currentText()]
        pipeline_step = {"type": "Step", "id": pipeline_step_id}
        
        data = {}
        data["step"] = pipeline_step
        data["project"] = self._app.context.project
        data["entity"] = self._entity
        data["content"] = self.ui.task_name.text()
        if self._curr_user:
            data["task_assignees"] = [self._curr_user]
        
        e = self._app.shotgun.create("Task", data) 
        
        # try to set it to IP
        # not all studios use IP
        try:
            self._app.shotgun.update("Task", e["id"], {"sg_status_list": "ip"})
        except:
            pass
        
        return e["id"]