# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'work_files_form.ui'
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


from ..file_list_view import FileListView

from  . import resources_rc

class Ui_WorkFilesForm(object):
    def setupUi(self, WorkFilesForm):
        if not WorkFilesForm.objectName():
            WorkFilesForm.setObjectName(u"WorkFilesForm")
        WorkFilesForm.resize(823, 644)
        WorkFilesForm.setStyleSheet(u"")
        self.verticalLayout_8 = QVBoxLayout(WorkFilesForm)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, -1, 0)
        self.items_title_label_2 = QLabel(WorkFilesForm)
        self.items_title_label_2.setObjectName(u"items_title_label_2")
        self.items_title_label_2.setMinimumSize(QSize(0, 44))
        self.items_title_label_2.setStyleSheet(u"")
        self.items_title_label_2.setMargin(4)

        self.verticalLayout_6.addWidget(self.items_title_label_2)

        self.work_area_frame = QFrame(WorkFilesForm)
        self.work_area_frame.setObjectName(u"work_area_frame")
        self.work_area_frame.setMinimumSize(QSize(0, 0))
        self.work_area_frame.setMaximumSize(QSize(16777215, 16777215))
        self.work_area_frame.setCursor(QCursor(Qt.PointingHandCursor))
        self.work_area_frame.setStyleSheet(u"#work_area_frame {\n"
"border-style: solid;\n"
"border-radius: 2px;\n"
"border-width: 1px;\n"
"border-color: rgb(32,32,32);\n"
"}")
        self.work_area_frame.setFrameShape(QFrame.StyledPanel)
        self.work_area_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_20 = QVBoxLayout(self.work_area_frame)
#ifndef Q_OS_MAC
        self.verticalLayout_20.setSpacing(6)
#endif
        self.verticalLayout_20.setContentsMargins(6, 6, 6, 6)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.project_pages = QStackedWidget(self.work_area_frame)
        self.project_pages.setObjectName(u"project_pages")
        self.project_pages.setLineWidth(0)
        self.project_page = QWidget()
        self.project_page.setObjectName(u"project_page")
        self.verticalLayout_10 = QVBoxLayout(self.project_page)
        self.verticalLayout_10.setSpacing(8)
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.project_frame = QFrame(self.project_page)
        self.project_frame.setObjectName(u"project_frame")
        self.project_frame.setFrameShape(QFrame.NoFrame)
        self.project_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.project_frame)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setSpacing(6)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.project_label = QLabel(self.project_frame)
        self.project_label.setObjectName(u"project_label")
        self.project_label.setMinimumSize(QSize(240, 0))
        self.project_label.setMaximumSize(QSize(240, 16777215))
        self.project_label.setStyleSheet(u"#project_label {\n"
"font-size: 12pt\n"
"}")

        self.verticalLayout_7.addWidget(self.project_label)

        self.project_line = QFrame(self.project_frame)
        self.project_line.setObjectName(u"project_line")
        self.project_line.setMinimumSize(QSize(0, 1))
        self.project_line.setMaximumSize(QSize(16777215, 1))
        self.project_line.setFrameShadow(QFrame.Plain)
        self.project_line.setFrameShape(QFrame.HLine)

        self.verticalLayout_7.addWidget(self.project_line)

        self.project_description = QLabel(self.project_frame)
        self.project_description.setObjectName(u"project_description")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.project_description.sizePolicy().hasHeightForWidth())
        self.project_description.setSizePolicy(sizePolicy)
        self.project_description.setMinimumSize(QSize(240, 0))
        self.project_description.setMaximumSize(QSize(240, 16777215))
        self.project_description.setStyleSheet(u"#project_description {\n"
"font-size: 9pt\n"
"}")
        self.project_description.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.project_description.setWordWrap(True)
        self.project_description.setTextInteractionFlags(Qt.NoTextInteraction)

        self.verticalLayout_7.addWidget(self.project_description)

        self.verticalLayout_7.setStretch(2, 1)

        self.horizontalLayout_3.addLayout(self.verticalLayout_7)

        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.project_thumbnail = QLabel(self.project_frame)
        self.project_thumbnail.setObjectName(u"project_thumbnail")
        self.project_thumbnail.setMinimumSize(QSize(100, 100))
        self.project_thumbnail.setMaximumSize(QSize(100, 100))
        self.project_thumbnail.setStyleSheet(u"#project_thumbnail {\n"
"background-color: rgb(0,0,0,32);\n"
"border-radius: 2px;\n"
"}")
        self.project_thumbnail.setFrameShape(QFrame.NoFrame)
        self.project_thumbnail.setLineWidth(0)
        self.project_thumbnail.setAlignment(Qt.AlignCenter)
        self.project_thumbnail.setMargin(0)
        self.project_thumbnail.setIndent(0)

        self.verticalLayout_11.addWidget(self.project_thumbnail)

        self.verticalSpacer_5 = QSpacerItem(20, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_11.addItem(self.verticalSpacer_5)

        self.horizontalLayout_3.addLayout(self.verticalLayout_11)

        self.horizontalLayout_3.setStretch(0, 1)

        self.verticalLayout_10.addWidget(self.project_frame)

        self.entity_pages = QStackedWidget(self.project_page)
        self.entity_pages.setObjectName(u"entity_pages")
        self.entity_pages.setStyleSheet(u"")
        self.entity_pages.setLineWidth(0)
        self.entity_page = QWidget()
        self.entity_page.setObjectName(u"entity_page")
        self.verticalLayout_5 = QVBoxLayout(self.entity_page)
        self.verticalLayout_5.setSpacing(8)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.entity_frame = QFrame(self.entity_page)
        self.entity_frame.setObjectName(u"entity_frame")
        self.entity_frame.setFrameShape(QFrame.NoFrame)
        self.entity_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.entity_frame)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.entity_label = QLabel(self.entity_frame)
        self.entity_label.setObjectName(u"entity_label")
        self.entity_label.setMinimumSize(QSize(240, 0))
        self.entity_label.setMaximumSize(QSize(240, 16777215))
        self.entity_label.setStyleSheet(u"#entity_label {\n"
"font-size: 12pt\n"
"}")

        self.verticalLayout_3.addWidget(self.entity_label)

        self.entity_line = QFrame(self.entity_frame)
        self.entity_line.setObjectName(u"entity_line")
        self.entity_line.setMinimumSize(QSize(0, 1))
        self.entity_line.setMaximumSize(QSize(16777215, 1))
        self.entity_line.setFrameShadow(QFrame.Plain)
        self.entity_line.setFrameShape(QFrame.HLine)

        self.verticalLayout_3.addWidget(self.entity_line)

        self.entity_description = QLabel(self.entity_frame)
        self.entity_description.setObjectName(u"entity_description")
        sizePolicy.setHeightForWidth(self.entity_description.sizePolicy().hasHeightForWidth())
        self.entity_description.setSizePolicy(sizePolicy)
        self.entity_description.setMinimumSize(QSize(240, 0))
        self.entity_description.setMaximumSize(QSize(240, 16777215))
        self.entity_description.setStyleSheet(u"#entity_description {\n"
"font-size: 9pt\n"
"}")
        self.entity_description.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.entity_description.setWordWrap(True)
        self.entity_description.setTextInteractionFlags(Qt.NoTextInteraction)

        self.verticalLayout_3.addWidget(self.entity_description)

        self.verticalLayout_3.setStretch(2, 1)

        self.horizontalLayout_4.addLayout(self.verticalLayout_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.entity_thumbnail = QLabel(self.entity_frame)
        self.entity_thumbnail.setObjectName(u"entity_thumbnail")
        self.entity_thumbnail.setMinimumSize(QSize(100, 100))
        self.entity_thumbnail.setMaximumSize(QSize(100, 100))
        self.entity_thumbnail.setStyleSheet(u"#entity_thumbnail {\n"
"background-color: rgb(0,0,0,32);\n"
"border-radius: 2px;\n"
"}")
        self.entity_thumbnail.setLineWidth(0)
        self.entity_thumbnail.setScaledContents(False)
        self.entity_thumbnail.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.entity_thumbnail)

        self.verticalSpacer_3 = QSpacerItem(20, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_3)

        self.horizontalLayout_4.addLayout(self.verticalLayout_4)

        self.horizontalLayout_4.setStretch(0, 1)

        self.verticalLayout_5.addWidget(self.entity_frame)

        self.task_pages = QStackedWidget(self.entity_page)
        self.task_pages.setObjectName(u"task_pages")
        self.task_pages.setLineWidth(0)
        self.task_page = QWidget()
        self.task_page.setObjectName(u"task_page")
        self.horizontalLayout_6 = QHBoxLayout(self.task_page)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.task_frame = QFrame(self.task_page)
        self.task_frame.setObjectName(u"task_frame")
        self.task_frame.setFrameShape(QFrame.NoFrame)
        self.task_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.task_frame)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.verticalLayout_21 = QVBoxLayout()
        self.verticalLayout_21.setSpacing(6)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.task_label = QLabel(self.task_frame)
        self.task_label.setObjectName(u"task_label")
        self.task_label.setMinimumSize(QSize(240, 0))
        self.task_label.setMaximumSize(QSize(240, 16777215))
        self.task_label.setStyleSheet(u"#task_label {\n"
"font-size: 12pt\n"
"}")

        self.verticalLayout_21.addWidget(self.task_label)

        self.task_line = QFrame(self.task_frame)
        self.task_line.setObjectName(u"task_line")
        self.task_line.setMinimumSize(QSize(0, 1))
        self.task_line.setMaximumSize(QSize(16777215, 1))
        self.task_line.setFrameShadow(QFrame.Plain)
        self.task_line.setFrameShape(QFrame.HLine)

        self.verticalLayout_21.addWidget(self.task_line)

        self.task_description = QLabel(self.task_frame)
        self.task_description.setObjectName(u"task_description")
        sizePolicy.setHeightForWidth(self.task_description.sizePolicy().hasHeightForWidth())
        self.task_description.setSizePolicy(sizePolicy)
        self.task_description.setMinimumSize(QSize(240, 0))
        self.task_description.setMaximumSize(QSize(240, 16777215))
        self.task_description.setStyleSheet(u"#task_description {\n"
"font-size: 9pt\n"
"}")
        self.task_description.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.task_description.setWordWrap(True)
        self.task_description.setTextInteractionFlags(Qt.NoTextInteraction)

        self.verticalLayout_21.addWidget(self.task_description)

        self.verticalLayout_21.setStretch(2, 1)

        self.horizontalLayout_5.addLayout(self.verticalLayout_21)

        self.verticalLayout_22 = QVBoxLayout()
        self.verticalLayout_22.setSpacing(0)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.task_thumbnail = QLabel(self.task_frame)
        self.task_thumbnail.setObjectName(u"task_thumbnail")
        self.task_thumbnail.setMinimumSize(QSize(100, 100))
        self.task_thumbnail.setMaximumSize(QSize(100, 100))
        self.task_thumbnail.setStyleSheet(u"#task_thumbnail {\n"
"background-color: rgb(0,0,0,32);\n"
"border-radius: 2px;\n"
"}")
        self.task_thumbnail.setFrameShape(QFrame.NoFrame)
        self.task_thumbnail.setLineWidth(0)
        self.task_thumbnail.setAlignment(Qt.AlignCenter)
        self.task_thumbnail.setMargin(0)
        self.task_thumbnail.setIndent(0)

        self.verticalLayout_22.addWidget(self.task_thumbnail)

        self.verticalSpacer_4 = QSpacerItem(20, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_22.addItem(self.verticalSpacer_4)

        self.horizontalLayout_5.addLayout(self.verticalLayout_22)

        self.horizontalLayout_5.setStretch(0, 1)

        self.horizontalLayout_6.addWidget(self.task_frame)

        self.task_pages.addWidget(self.task_page)
        self.no_task_page = QWidget()
        self.no_task_page.setObjectName(u"no_task_page")
        self.horizontalLayout_7 = QHBoxLayout(self.no_task_page)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.no_task_label = QLabel(self.no_task_page)
        self.no_task_label.setObjectName(u"no_task_label")
        self.no_task_label.setStyleSheet(u"#no_task_label {\n"
"font-size: 14pt;\n"
"border-style: dashed;\n"
"border-width: 2px;\n"
"border-radius: 3px;\n"
"}")
        self.no_task_label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_7.addWidget(self.no_task_label)

        self.task_pages.addWidget(self.no_task_page)

        self.verticalLayout_5.addWidget(self.task_pages)

        self.entity_pages.addWidget(self.entity_page)
        self.no_entity_page = QWidget()
        self.no_entity_page.setObjectName(u"no_entity_page")
        self.horizontalLayout_10 = QHBoxLayout(self.no_entity_page)
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.no_entity_label = QLabel(self.no_entity_page)
        self.no_entity_label.setObjectName(u"no_entity_label")
        self.no_entity_label.setStyleSheet(u"#no_entity_label {\n"
"font-size: 14pt;\n"
"border-style: dashed;\n"
"border-width: 2px;\n"
"border-radius: 3px;\n"
"}")
        self.no_entity_label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_10.addWidget(self.no_entity_label)

        self.entity_pages.addWidget(self.no_entity_page)

        self.verticalLayout_10.addWidget(self.entity_pages)

        self.project_pages.addWidget(self.project_page)
        self.no_project_page = QWidget()
        self.no_project_page.setObjectName(u"no_project_page")
        self.horizontalLayout_16 = QHBoxLayout(self.no_project_page)
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.no_project_label = QLabel(self.no_project_page)
        self.no_project_label.setObjectName(u"no_project_label")
        self.no_project_label.setStyleSheet(u"#no_project_label {\n"
"font-size: 14pt;\n"
"border-style: dashed;\n"
"border-width: 2px;\n"
"border-radius: 3px;\n"
"}")
        self.no_project_label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_16.addWidget(self.no_project_label)

        self.project_pages.addWidget(self.no_project_page)

        self.verticalLayout_20.addWidget(self.project_pages)

        self.no_change_frame = QFrame(self.work_area_frame)
        self.no_change_frame.setObjectName(u"no_change_frame")
        self.no_change_frame.setFrameShape(QFrame.NoFrame)
        self.no_change_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.no_change_frame)
#ifndef Q_OS_MAC
        self.verticalLayout_19.setSpacing(6)
#endif
        self.verticalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.no_change_line = QFrame(self.no_change_frame)
        self.no_change_line.setObjectName(u"no_change_line")
        self.no_change_line.setMinimumSize(QSize(0, 1))
        self.no_change_line.setMaximumSize(QSize(16777215, 1))
        self.no_change_line.setStyleSheet(u"#no_change_line {\n"
"background-color: rgb(32,32,32);\n"
"}")
        self.no_change_line.setFrameShadow(QFrame.Plain)
        self.no_change_line.setLineWidth(1)
        self.no_change_line.setMidLineWidth(0)
        self.no_change_line.setFrameShape(QFrame.HLine)

        self.verticalLayout_19.addWidget(self.no_change_line)

        self.no_change_label = QLabel(self.no_change_frame)
        self.no_change_label.setObjectName(u"no_change_label")
        self.no_change_label.setStyleSheet(u"#no_change_label {\n"
"font-size: 9pt\n"
"}")
        self.no_change_label.setIndent(0)

        self.verticalLayout_19.addWidget(self.no_change_label)

        self.verticalLayout_20.addWidget(self.no_change_frame)

        self.verticalLayout_6.addWidget(self.work_area_frame)

        self.items_title_label_3 = QLabel(WorkFilesForm)
        self.items_title_label_3.setObjectName(u"items_title_label_3")
        self.items_title_label_3.setMinimumSize(QSize(0, 44))
        self.items_title_label_3.setStyleSheet(u"")
        self.items_title_label_3.setMargin(4)

        self.verticalLayout_6.addWidget(self.items_title_label_3)

        self.files_filter_frame = QFrame(WorkFilesForm)
        self.files_filter_frame.setObjectName(u"files_filter_frame")
        self.files_filter_frame.setStyleSheet(u"#files_filter_frame {\n"
"border-style: solid;\n"
"border-radius: 2px;\n"
"border-width: 1px;\n"
"border-color: rgb(32,32,32);\n"
"}")
        self.files_filter_frame.setFrameShape(QFrame.StyledPanel)
        self.files_filter_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.files_filter_frame)
        self.verticalLayout.setContentsMargins(6, 6, 6, 6)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.filter_combo = QComboBox(self.files_filter_frame)
        self.filter_combo.setObjectName(u"filter_combo")
        self.filter_combo.setMinimumSize(QSize(0, 0))

        self.verticalLayout.addWidget(self.filter_combo)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_2)

        self.show_in_fs_label = QLabel(self.files_filter_frame)
        self.show_in_fs_label.setObjectName(u"show_in_fs_label")
        self.show_in_fs_label.setCursor(QCursor(Qt.PointingHandCursor))
        self.show_in_fs_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.show_in_fs_label.setTextInteractionFlags(Qt.NoTextInteraction)

        self.horizontalLayout_8.addWidget(self.show_in_fs_label)

        self.verticalLayout.addLayout(self.horizontalLayout_8)

        self.verticalLayout_6.addWidget(self.files_filter_frame)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer)

        self.verticalLayout_6.setStretch(4, 1)

        self.horizontalLayout.addLayout(self.verticalLayout_6)

        self.file_list = FileListView(WorkFilesForm)
        self.file_list.setObjectName(u"file_list")
        self.file_list.setStyleSheet(u"#file_list {\n"
"background-color: rgb(255, 128, 0);\n"
"}")

        self.horizontalLayout.addWidget(self.file_list)

        self.horizontalLayout.setStretch(1, 1)

        self.verticalLayout_8.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.new_file_btn = QPushButton(WorkFilesForm)
        self.new_file_btn.setObjectName(u"new_file_btn")
        self.new_file_btn.setMinimumSize(QSize(80, 0))

        self.horizontalLayout_2.addWidget(self.new_file_btn)

        self.open_file_btn = QPushButton(WorkFilesForm)
        self.open_file_btn.setObjectName(u"open_file_btn")
        self.open_file_btn.setMinimumSize(QSize(80, 0))

        self.horizontalLayout_2.addWidget(self.open_file_btn)

        self.verticalLayout_8.addLayout(self.horizontalLayout_2)

        self.retranslateUi(WorkFilesForm)

        self.project_pages.setCurrentIndex(0)
        self.entity_pages.setCurrentIndex(0)
        self.task_pages.setCurrentIndex(0)

        QMetaObject.connectSlotsByName(WorkFilesForm)
    # setupUi

    def retranslateUi(self, WorkFilesForm):
        WorkFilesForm.setWindowTitle(QCoreApplication.translate("WorkFilesForm", u"Form", None))
        self.items_title_label_2.setText(QCoreApplication.translate("WorkFilesForm", u"<big>Select a Work Area</big>", None))
#if QT_CONFIG(tooltip)
        self.work_area_frame.setToolTip(QCoreApplication.translate("WorkFilesForm", u"Click to Change Work Area...", None))
#endif // QT_CONFIG(tooltip)
        self.project_label.setText(QCoreApplication.translate("WorkFilesForm", u"Project:", None))
        self.project_description.setText("")
        self.project_thumbnail.setText("")
        self.entity_label.setText(QCoreApplication.translate("WorkFilesForm", u"Shot:", None))
        self.entity_description.setText("")
        self.entity_thumbnail.setText("")
        self.task_label.setText(QCoreApplication.translate("WorkFilesForm", u"Task:", None))
        self.task_description.setText("")
        self.task_thumbnail.setText("")
        self.no_task_label.setText(QCoreApplication.translate("WorkFilesForm", u"Click to Select a Task", None))
        self.no_entity_label.setText(QCoreApplication.translate("WorkFilesForm", u"Click to Select a Work Area", None))
        self.no_project_label.setText(QCoreApplication.translate("WorkFilesForm", u"Click to Select a Work Area", None))
        self.no_change_label.setText(QCoreApplication.translate("WorkFilesForm", u"<html><head/><body><p><span style=\" font-style:italic;\">(Note: The Work Area is locked and cannot be changed)</span></p></body></html>", None))
        self.items_title_label_3.setText(QCoreApplication.translate("WorkFilesForm", u"<big>Choose Which Files to Display</big>", None))
#if QT_CONFIG(tooltip)
        self.filter_combo.setToolTip(QCoreApplication.translate("WorkFilesForm", u"Choose where to find the list of available files", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.show_in_fs_label.setToolTip(QCoreApplication.translate("WorkFilesForm", u"Show the selected location in the file system", None))
#endif // QT_CONFIG(tooltip)
        self.show_in_fs_label.setText(QCoreApplication.translate("WorkFilesForm", u"<html><head/><body><p><span style=\" text-decoration: underline;\">Show in File System</span></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.new_file_btn.setToolTip(QCoreApplication.translate("WorkFilesForm", u"Start a New file in the selected Work Area", None))
#endif // QT_CONFIG(tooltip)
        self.new_file_btn.setText(QCoreApplication.translate("WorkFilesForm", u"New File", None))
#if QT_CONFIG(tooltip)
        self.open_file_btn.setToolTip(QCoreApplication.translate("WorkFilesForm", u"Open the selected file", None))
#endif // QT_CONFIG(tooltip)
        self.open_file_btn.setText(QCoreApplication.translate("WorkFilesForm", u"Open File", None))
    # retranslateUi
