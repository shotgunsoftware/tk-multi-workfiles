# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'save_as_form.ui'
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


from  . import resources_rc

class Ui_SaveAsForm(object):
    def setupUi(self, SaveAsForm):
        if not SaveAsForm.objectName():
            SaveAsForm.setObjectName(u"SaveAsForm")
        SaveAsForm.resize(510, 294)
        SaveAsForm.setMinimumSize(QSize(510, 0))
        SaveAsForm.setMaximumSize(QSize(16777215, 16777215))
        SaveAsForm.setFocusPolicy(Qt.ClickFocus)
        self.verticalLayout = QVBoxLayout(SaveAsForm)
        self.verticalLayout.setSpacing(4)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(16)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(12, 12, 12, 4)
        self.header_frame = QFrame(SaveAsForm)
        self.header_frame.setObjectName(u"header_frame")
        self.header_frame.setStyleSheet(u"#header_frame {\n"
"border-style: solid;\n"
"border-radius: 3;\n"
"border-width: 1;\n"
"border-color: rgb(32,32,32);\n"
"}")
        self.header_frame.setFrameShape(QFrame.StyledPanel)
        self.header_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.header_frame)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.header_frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(80, 80))
        self.label_2.setMaximumSize(QSize(80, 80))
        self.label_2.setPixmap(QPixmap(u":/res/save_as_icon.png"))
        self.label_2.setScaledContents(False)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.header_label = QLabel(self.header_frame)
        self.header_label.setObjectName(u"header_label")
        self.header_label.setWordWrap(True)

        self.horizontalLayout_2.addWidget(self.header_label)

        self.verticalLayout_2.addWidget(self.header_frame)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(16)
        self.gridLayout.setVerticalSpacing(10)
        self.name_layout = QHBoxLayout()
        self.name_layout.setObjectName(u"name_layout")
        self.name_layout.setContentsMargins(4, -1, -1, -1)
        self.name_edit = QLineEdit(SaveAsForm)
        self.name_edit.setObjectName(u"name_edit")
        self.name_edit.setMaximumSize(QSize(16777215, 16777215))
        self.name_edit.setFrame(True)

        self.name_layout.addWidget(self.name_edit)

        self.reset_version_cb = QCheckBox(SaveAsForm)
        self.reset_version_cb.setObjectName(u"reset_version_cb")

        self.name_layout.addWidget(self.reset_version_cb)

        self.gridLayout.addLayout(self.name_layout, 0, 1, 1, 1)

        self.name_label = QLabel(SaveAsForm)
        self.name_label.setObjectName(u"name_label")
        self.name_label.setMinimumSize(QSize(0, 0))
        self.name_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.name_label.setIndent(4)

        self.gridLayout.addWidget(self.name_label, 0, 0, 1, 1)

        self.filename_preview_label = QLabel(SaveAsForm)
        self.filename_preview_label.setObjectName(u"filename_preview_label")
        self.filename_preview_label.setIndent(4)

        self.gridLayout.addWidget(self.filename_preview_label, 1, 1, 1, 1)

        self.path_preview_edit = QTextEdit(SaveAsForm)
        self.path_preview_edit.setObjectName(u"path_preview_edit")
        self.path_preview_edit.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.path_preview_edit.sizePolicy().hasHeightForWidth())
        self.path_preview_edit.setSizePolicy(sizePolicy)
        self.path_preview_edit.setMinimumSize(QSize(0, 0))
        self.path_preview_edit.setMaximumSize(QSize(16777215, 60))
        self.path_preview_edit.setFocusPolicy(Qt.NoFocus)
        self.path_preview_edit.setStyleSheet(u"QTextEdit {\n"
"background-color: rgb(0,0,0,0);\n"
"border-style: none;\n"
"}")
        self.path_preview_edit.setFrameShape(QFrame.NoFrame)
        self.path_preview_edit.setFrameShadow(QFrame.Plain)
        self.path_preview_edit.setLineWidth(0)
        self.path_preview_edit.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.path_preview_edit.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.path_preview_edit.setReadOnly(True)
        self.path_preview_edit.setAcceptRichText(True)

        self.gridLayout.addWidget(self.path_preview_edit, 2, 1, 1, 1)

        self.preview_label = QLabel(SaveAsForm)
        self.preview_label.setObjectName(u"preview_label")
        self.preview_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.preview_label.setIndent(4)

        self.gridLayout.addWidget(self.preview_label, 1, 0, 1, 1)

        self.label_6 = QLabel(SaveAsForm)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.label_6.setMargin(4)
        self.label_6.setIndent(0)

        self.gridLayout.addWidget(self.label_6, 2, 0, 1, 1)

        self.gridLayout.setColumnStretch(1, 1)

        self.verticalLayout_2.addLayout(self.gridLayout)

        self.verticalLayout.addLayout(self.verticalLayout_2)

        self.verticalSpacer_2 = QSpacerItem(20, 1, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.break_line = QFrame(SaveAsForm)
        self.break_line.setObjectName(u"break_line")
        self.break_line.setFrameShape(QFrame.HLine)
        self.break_line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.break_line)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(12, 8, 12, 12)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.cancel_btn = QPushButton(SaveAsForm)
        self.cancel_btn.setObjectName(u"cancel_btn")

        self.horizontalLayout_3.addWidget(self.cancel_btn)

        self.continue_btn = QPushButton(SaveAsForm)
        self.continue_btn.setObjectName(u"continue_btn")

        self.horizontalLayout_3.addWidget(self.continue_btn)

        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.verticalLayout.setStretch(1, 1)
        QWidget.setTabOrder(self.name_edit, self.reset_version_cb)
        QWidget.setTabOrder(self.reset_version_cb, self.cancel_btn)
        QWidget.setTabOrder(self.cancel_btn, self.continue_btn)
        QWidget.setTabOrder(self.continue_btn, self.path_preview_edit)

        self.retranslateUi(SaveAsForm)

        self.continue_btn.setDefault(True)

        QMetaObject.connectSlotsByName(SaveAsForm)
    # setupUi

    def retranslateUi(self, SaveAsForm):
        SaveAsForm.setWindowTitle(QCoreApplication.translate("SaveAsForm", u"Form", None))
        self.label_2.setText("")
        self.header_label.setText(QCoreApplication.translate("SaveAsForm", u"Type in a name below and Shotgun will save the current scene", None))
        self.reset_version_cb.setText(QCoreApplication.translate("SaveAsForm", u"Reset Version No.?", None))
        self.name_label.setText(QCoreApplication.translate("SaveAsForm", u"<html><head/><body><p><span style=\" font-weight:600;\">Name:</span></p></body></html>", None))
        self.filename_preview_label.setText(QCoreApplication.translate("SaveAsForm", u"name.v001.ma", None))
        self.path_preview_edit.setHtml(QCoreApplication.translate("SaveAsForm", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Lucida Grande'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">/foo/bar/...</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">line 2</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">line 3</p></body></html>", None))
        self.preview_label.setText(QCoreApplication.translate("SaveAsForm", u"<html><head/><body><p><span style=\" font-weight:600;\">Preview:</span></p></body></html>", None))
        self.label_6.setText(QCoreApplication.translate("SaveAsForm", u"<html><head/><body><p><span style=\" font-weight:600;\">Work Area:</span></p></body></html>", None))
        self.cancel_btn.setText(QCoreApplication.translate("SaveAsForm", u"Cancel", None))
        self.continue_btn.setText(QCoreApplication.translate("SaveAsForm", u"Save", None))
    # retranslateUi
