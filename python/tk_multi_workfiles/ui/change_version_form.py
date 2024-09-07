# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'change_version_form.ui'
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


class Ui_ChangeVersionForm(object):
    def setupUi(self, ChangeVersionForm):
        if not ChangeVersionForm.objectName():
            ChangeVersionForm.setObjectName(u"ChangeVersionForm")
        ChangeVersionForm.resize(320, 190)
        ChangeVersionForm.setMinimumSize(QSize(320, 190))
        ChangeVersionForm.setMaximumSize(QSize(16777215, 16777215))
        ChangeVersionForm.setFocusPolicy(Qt.TabFocus)
        self.verticalLayout = QVBoxLayout(ChangeVersionForm)
        self.verticalLayout.setSpacing(4)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(20)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(12, 12, 12, 4)
        self.label = QLabel(ChangeVersionForm)
        self.label.setObjectName(u"label")
        self.label.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.label)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(30, -1, -1, -1)
        self.gridLayout = QGridLayout()
        self.gridLayout.setSpacing(8)
        self.gridLayout.setObjectName(u"gridLayout")
        self.new_version_edit = QLineEdit(ChangeVersionForm)
        self.new_version_edit.setObjectName(u"new_version_edit")
        self.new_version_edit.setMaximumSize(QSize(60, 16777215))
        self.new_version_edit.setMaxLength(32767)
        self.new_version_edit.setFrame(True)

        self.gridLayout.addWidget(self.new_version_edit, 1, 1, 1, 1)

        self.label_3 = QLabel(ChangeVersionForm)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)

        self.label_2 = QLabel(ChangeVersionForm)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(140, 0))

        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)

        self.current_version_label = QLabel(ChangeVersionForm)
        self.current_version_label.setObjectName(u"current_version_label")

        self.gridLayout.addWidget(self.current_version_label, 0, 1, 1, 1)

        self.gridLayout.setColumnStretch(0, 1)

        self.horizontalLayout_2.addLayout(self.gridLayout)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        self.horizontalLayout_2.setStretch(1, 1)

        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.verticalLayout.addLayout(self.verticalLayout_2)

        self.verticalSpacer = QSpacerItem(20, 1, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.break_line = QFrame(ChangeVersionForm)
        self.break_line.setObjectName(u"break_line")
        self.break_line.setFrameShape(QFrame.HLine)
        self.break_line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.break_line)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(12, 8, 12, 12)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.cancel_btn = QPushButton(ChangeVersionForm)
        self.cancel_btn.setObjectName(u"cancel_btn")

        self.horizontalLayout.addWidget(self.cancel_btn)

        self.change_version_btn = QPushButton(ChangeVersionForm)
        self.change_version_btn.setObjectName(u"change_version_btn")

        self.horizontalLayout.addWidget(self.change_version_btn)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalLayout.setStretch(2, 1)
        QWidget.setTabOrder(self.new_version_edit, self.change_version_btn)
        QWidget.setTabOrder(self.change_version_btn, self.cancel_btn)

        self.retranslateUi(ChangeVersionForm)
        self.new_version_edit.returnPressed.connect(self.change_version_btn.click)

        self.change_version_btn.setDefault(True)

        QMetaObject.connectSlotsByName(ChangeVersionForm)
    # setupUi

    def retranslateUi(self, ChangeVersionForm):
        ChangeVersionForm.setWindowTitle(QCoreApplication.translate("ChangeVersionForm", u"Form", None))
        self.label.setText(QCoreApplication.translate("ChangeVersionForm", u"Below you can change the version number of your current scene without doing a publish", None))
#if QT_CONFIG(tooltip)
        self.new_version_edit.setToolTip(QCoreApplication.translate("ChangeVersionForm", u"Enter a new version for your work file", None))
#endif // QT_CONFIG(tooltip)
        self.new_version_edit.setInputMask("")
        self.label_3.setText(QCoreApplication.translate("ChangeVersionForm", u"<html><head/><body><p><span style=\" font-weight:600;\">New Version:</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("ChangeVersionForm", u"<html><head/><body><p><span style=\" font-weight:600;\">Current Version:</span></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.current_version_label.setToolTip(QCoreApplication.translate("ChangeVersionForm", u"The current version of your work file", None))
#endif // QT_CONFIG(tooltip)
        self.current_version_label.setText(QCoreApplication.translate("ChangeVersionForm", u"?", None))
        self.cancel_btn.setText(QCoreApplication.translate("ChangeVersionForm", u"Cancel", None))
        self.change_version_btn.setText(QCoreApplication.translate("ChangeVersionForm", u"Change Version", None))
    # retranslateUi
