# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'file_tile.ui'
#
#      by: pyside-uic 0.2.13 running on PySide 1.1.0
#
# WARNING! All changes made in this file will be lost!

from tank.platform.qt import QtCore, QtGui

class Ui_FileTile(object):
    def setupUi(self, FileTile):
        FileTile.setObjectName("FileTile")
        FileTile.resize(291, 76)
        FileTile.setStyleSheet("")
        self.horizontalLayout = QtGui.QHBoxLayout(FileTile)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.background = QtGui.QFrame(FileTile)
        self.background.setStyleSheet("#background {\n"
"background-color: rgb(135, 166, 185, 50);\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: rgb(66,174,241);\n"
"border-radius: 3px;\n"
"}")
        self.background.setFrameShape(QtGui.QFrame.StyledPanel)
        self.background.setFrameShadow(QtGui.QFrame.Plain)
        self.background.setLineWidth(2)
        self.background.setObjectName("background")
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.background)
        self.horizontalLayout_2.setContentsMargins(4, 4, 4, 4)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.thumbnail = QtGui.QLabel(self.background)
        self.thumbnail.setMinimumSize(QtCore.QSize(96, 64))
        self.thumbnail.setMaximumSize(QtCore.QSize(96, 64))
        self.thumbnail.setStyleSheet("")
        self.thumbnail.setText("")
        self.thumbnail.setTextFormat(QtCore.Qt.AutoText)
        self.thumbnail.setPixmap(QtGui.QPixmap(":/tk-multi-workfiles/thumb_empty.png"))
        self.thumbnail.setScaledContents(True)
        self.thumbnail.setAlignment(QtCore.Qt.AlignCenter)
        self.thumbnail.setObjectName("thumbnail")
        self.horizontalLayout_2.addWidget(self.thumbnail)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtGui.QSpacerItem(20, 0, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.label = QtGui.QLabel(self.background)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        spacerItem1 = QtGui.QSpacerItem(20, 0, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(2, 1)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout_2.setStretch(1, 1)
        self.horizontalLayout.addWidget(self.background)

        self.retranslateUi(FileTile)
        QtCore.QMetaObject.connectSlotsByName(FileTile)

    def retranslateUi(self, FileTile):
        FileTile.setWindowTitle(QtGui.QApplication.translate("FileTile", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("FileTile", "<b>Title</b>", None, QtGui.QApplication.UnicodeUTF8))

from . import resources_rc
