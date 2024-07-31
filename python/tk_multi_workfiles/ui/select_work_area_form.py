# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'select_work_area_form.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from tank.platform.qt import QtCore
for name, cls in QtCore.__dict__.items():
    if isinstance(cls, type): globals()[name] = cls

from tank.platform.qt import QtGui
for name, cls in QtGui.__dict__.items():
    if isinstance(cls, type): globals()[name] = cls


from ..entity_browser import EntityBrowserWidget
from ..task_browser import TaskBrowserWidget

class Ui_SelectWorkAreaForm(object):
    def setupUi(self, SelectWorkAreaForm):
        if not SelectWorkAreaForm.objectName():
            SelectWorkAreaForm.setObjectName(u"SelectWorkAreaForm")
        SelectWorkAreaForm.resize(1012, 837)
        self.verticalLayout = QVBoxLayout(SelectWorkAreaForm)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.mine_only_cb = QCheckBox(SelectWorkAreaForm)
        self.mine_only_cb.setObjectName(u"mine_only_cb")
        self.mine_only_cb.setChecked(True)

        self.horizontalLayout_2.addWidget(self.mine_only_cb)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)

        self.entity_browser = EntityBrowserWidget(SelectWorkAreaForm)
        self.entity_browser.setObjectName(u"entity_browser")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.entity_browser.sizePolicy().hasHeightForWidth())
        self.entity_browser.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.entity_browser, 0, 0, 1, 1)

        self.task_browser = TaskBrowserWidget(SelectWorkAreaForm)
        self.task_browser.setObjectName(u"task_browser")
        sizePolicy.setHeightForWidth(self.task_browser.sizePolicy().hasHeightForWidth())
        self.task_browser.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.task_browser, 0, 1, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.new_task_btn = QPushButton(SelectWorkAreaForm)
        self.new_task_btn.setObjectName(u"new_task_btn")

        self.horizontalLayout.addWidget(self.new_task_btn)

        self.horizontalSpacer = QSpacerItem(0, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.cancel_btn = QPushButton(SelectWorkAreaForm)
        self.cancel_btn.setObjectName(u"cancel_btn")

        self.horizontalLayout.addWidget(self.cancel_btn)

        self.select_new_btn = QPushButton(SelectWorkAreaForm)
        self.select_new_btn.setObjectName(u"select_new_btn")

        self.horizontalLayout.addWidget(self.select_new_btn)

        self.select_btn = QPushButton(SelectWorkAreaForm)
        self.select_btn.setObjectName(u"select_btn")
        self.select_btn.setAutoDefault(False)

        self.horizontalLayout.addWidget(self.select_btn)

        self.horizontalLayout.setStretch(1, 1)

        self.gridLayout.addLayout(self.horizontalLayout, 1, 1, 1, 1)

        self.verticalLayout.addLayout(self.gridLayout)

        self.retranslateUi(SelectWorkAreaForm)

        self.select_btn.setDefault(True)

        QMetaObject.connectSlotsByName(SelectWorkAreaForm)
    # setupUi

    def retranslateUi(self, SelectWorkAreaForm):
        SelectWorkAreaForm.setWindowTitle(QCoreApplication.translate("SelectWorkAreaForm", u"Form", None))
        self.mine_only_cb.setText(QCoreApplication.translate("SelectWorkAreaForm", u"Only Show My Tasks", None))
        self.new_task_btn.setText(QCoreApplication.translate("SelectWorkAreaForm", u"New Task...", None))
        self.cancel_btn.setText(QCoreApplication.translate("SelectWorkAreaForm", u"Cancel", None))
        self.select_new_btn.setText(QCoreApplication.translate("SelectWorkAreaForm", u"Start New Scene", None))
        self.select_btn.setText(QCoreApplication.translate("SelectWorkAreaForm", u"Change Work Area", None))
    # retranslateUi
