# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'file_item_form.ui'
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


from .thumbnail_label import ThumbnailLabel

from  . import resources_rc

class Ui_FileItemForm(object):
    def setupUi(self, FileItemForm):
        if not FileItemForm.objectName():
            FileItemForm.setObjectName(u"FileItemForm")
        FileItemForm.resize(324, 69)
        FileItemForm.setMaximumSize(QSize(16777215, 69))
        self.horizontalLayout_2 = QHBoxLayout(FileItemForm)
        self.horizontalLayout_2.setContentsMargins(2, 2, 2, 2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.background = QFrame(FileItemForm)
        self.background.setObjectName(u"background")
        self.background.setStyleSheet(u"#background {\n"
"border-radius: 3px;\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color: rgb(32,32,32);\n"
"}")
        self.background.setFrameShape(QFrame.StyledPanel)
        self.background.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.background)
        self.horizontalLayout.setSpacing(8)
        self.horizontalLayout.setContentsMargins(4, 4, 4, 4)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.thumbnail = ThumbnailLabel(self.background)
        self.thumbnail.setObjectName(u"thumbnail")
        self.thumbnail.setMinimumSize(QSize(80, 55))
        self.thumbnail.setMaximumSize(QSize(80, 55))
        self.thumbnail.setStyleSheet(u"")
        self.thumbnail.setPixmap(QPixmap(u":/res/thumb_empty.png"))
        self.thumbnail.setScaledContents(False)
        self.thumbnail.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.thumbnail)

        self.details = QLabel(self.background)
        self.details.setObjectName(u"details")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.details.sizePolicy().hasHeightForWidth())
        self.details.setSizePolicy(sizePolicy)
        self.details.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.details.setWordWrap(True)

        self.horizontalLayout.addWidget(self.details)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer = QSpacerItem(0, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.locked_label = QLabel(self.background)
        self.locked_label.setObjectName(u"locked_label")
        self.locked_label.setMinimumSize(QSize(12, 14))
        self.locked_label.setMaximumSize(QSize(12, 14))
        self.locked_label.setPixmap(QPixmap(u":/res/padlock.png"))
        self.locked_label.setScaledContents(False)

        self.verticalLayout.addWidget(self.locked_label)

        self.verticalLayout.setStretch(0, 1)

        self.horizontalLayout.addLayout(self.verticalLayout)

        self.horizontalLayout.setStretch(1, 1)

        self.horizontalLayout_2.addWidget(self.background)

        self.retranslateUi(FileItemForm)

        QMetaObject.connectSlotsByName(FileItemForm)
    # setupUi

    def retranslateUi(self, FileItemForm):
        FileItemForm.setWindowTitle(QCoreApplication.translate("FileItemForm", u"Form", None))
        self.thumbnail.setText("")
        self.details.setText(QCoreApplication.translate("FileItemForm", u"content", None))
        self.locked_label.setText("")
    # retranslateUi
