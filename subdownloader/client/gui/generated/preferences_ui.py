# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/maarten/programming/subdownloader_old/scripts/gui/ui/preferences.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_PreferencesDialog(object):
    def setupUi(self, PreferencesDialog):
        PreferencesDialog.setObjectName("PreferencesDialog")
        PreferencesDialog.setWindowModality(QtCore.Qt.WindowModal)
        PreferencesDialog.resize(719, 528)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(PreferencesDialog)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.tabsPreferences = QtWidgets.QTabWidget(PreferencesDialog)
        self.tabsPreferences.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabsPreferences.setObjectName("tabsPreferences")
        self.tabSearch = QtWidgets.QWidget()
        self.tabSearch.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tabSearch.setObjectName("tabSearch")
        self.horizontalLayout_3 = QtWidgets.QVBoxLayout(self.tabSearch)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.groupBoxSearchLanguages = QtWidgets.QGroupBox(self.tabSearch)
        self.groupBoxSearchLanguages.setObjectName("groupBoxSearchLanguages")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.groupBoxSearchLanguages)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.scrollAreaSearch = QtWidgets.QScrollArea(self.groupBoxSearchLanguages)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollAreaSearch.sizePolicy().hasHeightForWidth())
        self.scrollAreaSearch.setSizePolicy(sizePolicy)
        self.scrollAreaSearch.setMinimumSize(QtCore.QSize(0, 150))
        self.scrollAreaSearch.setWidgetResizable(True)
        self.scrollAreaSearch.setObjectName("scrollAreaSearch")
        self.scrollAreaWidgetSearch = QtWidgets.QWidget()
        self.scrollAreaWidgetSearch.setGeometry(QtCore.QRect(0, 0, 655, 372))
        self.scrollAreaWidgetSearch.setObjectName("scrollAreaWidgetSearch")
        self.vbox_B = QtWidgets.QVBoxLayout(self.scrollAreaWidgetSearch)
        self.vbox_B.setObjectName("vbox_B")
        self.scrollAreaWidgetLayoutSearch = QtWidgets.QGridLayout()
        self.scrollAreaWidgetLayoutSearch.setObjectName("scrollAreaWidgetLayoutSearch")
        self.vbox_B.addLayout(self.scrollAreaWidgetLayoutSearch)
        self.scrollAreaSearch.setWidget(self.scrollAreaWidgetSearch)
        self.verticalLayout_6.addWidget(self.scrollAreaSearch)
        self.horizontalLayout_3.addWidget(self.groupBoxSearchLanguages)
        self.tabsPreferences.addTab(self.tabSearch, "")
        self.tabDownload = QtWidgets.QWidget()
        self.tabDownload.setObjectName("tabDownload")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.tabDownload)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBoxDlDestinationFolder = QtWidgets.QGroupBox(self.tabDownload)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.groupBoxDlDestinationFolder.setFont(font)
        self.groupBoxDlDestinationFolder.setObjectName("groupBoxDlDestinationFolder")
        self.verticalLayout_B = QtWidgets.QVBoxLayout(self.groupBoxDlDestinationFolder)
        self.verticalLayout_B.setObjectName("verticalLayout_B")
        self.optionDlDestinationSame = QtWidgets.QRadioButton(self.groupBoxDlDestinationFolder)
        self.optionDlDestinationSame.setChecked(True)
        self.optionDlDestinationSame.setObjectName("optionDlDestinationSame")
        self.verticalLayout_B.addWidget(self.optionDlDestinationSame)
        self.optionDlDestinationAsk = QtWidgets.QRadioButton(self.groupBoxDlDestinationFolder)
        self.optionDlDestinationAsk.setObjectName("optionDlDestinationAsk")
        self.verticalLayout_B.addWidget(self.optionDlDestinationAsk)
        self.layoutPredefinedFolder = QtWidgets.QHBoxLayout()
        self.layoutPredefinedFolder.setObjectName("layoutPredefinedFolder")
        self.optionDlDestinationUser = QtWidgets.QRadioButton(self.groupBoxDlDestinationFolder)
        self.optionDlDestinationUser.setObjectName("optionDlDestinationUser")
        self.layoutPredefinedFolder.addWidget(self.optionDlDestinationUser)
        self.inputDlDestinationUser = QtWidgets.QLineEdit(self.groupBoxDlDestinationFolder)
        self.inputDlDestinationUser.setObjectName("inputDlDestinationUser")
        self.layoutPredefinedFolder.addWidget(self.inputDlDestinationUser)
        self.buttonDlDestinationUser = QtWidgets.QPushButton(self.groupBoxDlDestinationFolder)
        self.buttonDlDestinationUser.setDefault(False)
        self.buttonDlDestinationUser.setFlat(False)
        self.buttonDlDestinationUser.setObjectName("buttonDlDestinationUser")
        self.layoutPredefinedFolder.addWidget(self.buttonDlDestinationUser)
        self.verticalLayout_B.addLayout(self.layoutPredefinedFolder)
        self.verticalLayout.addWidget(self.groupBoxDlDestinationFolder)
        self.groupBoxSubFn = QtWidgets.QGroupBox(self.tabDownload)
        self.groupBoxSubFn.setObjectName("groupBoxSubFn")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBoxSubFn)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.optionSubFnSame = QtWidgets.QRadioButton(self.groupBoxSubFn)
        self.optionSubFnSame.setChecked(True)
        self.optionSubFnSame.setObjectName("optionSubFnSame")
        self.verticalLayout_2.addWidget(self.optionSubFnSame)
        self.optionSubFnSameLang = QtWidgets.QRadioButton(self.groupBoxSubFn)
        self.optionSubFnSameLang.setChecked(False)
        self.optionSubFnSameLang.setObjectName("optionSubFnSameLang")
        self.verticalLayout_2.addWidget(self.optionSubFnSameLang)
        self.optionSubFnSameLangUploader = QtWidgets.QRadioButton(self.groupBoxSubFn)
        self.optionSubFnSameLangUploader.setChecked(False)
        self.optionSubFnSameLangUploader.setObjectName("optionSubFnSameLangUploader")
        self.verticalLayout_2.addWidget(self.optionSubFnSameLangUploader)
        self.optionSubFnOnline = QtWidgets.QRadioButton(self.groupBoxSubFn)
        self.optionSubFnOnline.setObjectName("optionSubFnOnline")
        self.verticalLayout_2.addWidget(self.optionSubFnOnline)
        self.verticalLayout.addWidget(self.groupBoxSubFn)
        self.tabsPreferences.addTab(self.tabDownload, "")
        self.tabUpload = QtWidgets.QWidget()
        self.tabUpload.setObjectName("tabUpload")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.tabUpload)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.uploadFrame = QtWidgets.QFrame(self.tabUpload)
        self.uploadFrame.setObjectName("uploadFrame")
        self.formLayout_2 = QtWidgets.QFormLayout(self.uploadFrame)
        self.formLayout_2.setObjectName("formLayout_2")
        self.textUlDefaultLanguage = QtWidgets.QLabel(self.uploadFrame)
        self.textUlDefaultLanguage.setMinimumSize(QtCore.QSize(339, 0))
        self.textUlDefaultLanguage.setObjectName("textUlDefaultLanguage")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.textUlDefaultLanguage)
        self.optionUlDefaultLanguage = LanguageComboBox(self.uploadFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.optionUlDefaultLanguage.sizePolicy().hasHeightForWidth())
        self.optionUlDefaultLanguage.setSizePolicy(sizePolicy)
        self.optionUlDefaultLanguage.setFrame(True)
        self.optionUlDefaultLanguage.setObjectName("optionUlDefaultLanguage")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.optionUlDefaultLanguage)
        self.verticalLayout_7.addWidget(self.uploadFrame)
        self.tabsPreferences.addTab(self.tabUpload, "")
        self.tabProviders = QtWidgets.QWidget()
        self.tabProviders.setObjectName("tabProviders")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.tabProviders)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.providerComboBox = QtWidgets.QComboBox(self.tabProviders)
        self.providerComboBox.setObjectName("providerComboBox")
        self.verticalLayout_9.addWidget(self.providerComboBox)
        self.providerStack = QtWidgets.QStackedWidget(self.tabProviders)
        self.providerStack.setObjectName("providerStack")
        self.verticalLayout_9.addWidget(self.providerStack)
        self.tabsPreferences.addTab(self.tabProviders, "")
        self.tabOthers = QtWidgets.QWidget()
        self.tabOthers.setObjectName("tabOthers")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.tabOthers)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.groupInterface = QtWidgets.QGroupBox(self.tabOthers)
        self.groupInterface.setObjectName("groupInterface")
        self.gridLayout = QtWidgets.QGridLayout(self.groupInterface)
        self.gridLayout.setObjectName("gridLayout")
        self.textInterfaceLanguage = QtWidgets.QLabel(self.groupInterface)
        self.textInterfaceLanguage.setMinimumSize(QtCore.QSize(224, 0))
        self.textInterfaceLanguage.setObjectName("textInterfaceLanguage")
        self.gridLayout.addWidget(self.textInterfaceLanguage, 0, 0, 1, 1)
        self.optionInterfaceLanguage = InterfaceLanguageComboBox(self.groupInterface)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.optionInterfaceLanguage.sizePolicy().hasHeightForWidth())
        self.optionInterfaceLanguage.setSizePolicy(sizePolicy)
        self.optionInterfaceLanguage.setObjectName("optionInterfaceLanguage")
        self.gridLayout.addWidget(self.optionInterfaceLanguage, 0, 1, 1, 1)
        self.buttonHelpTranslation = QtWidgets.QPushButton(self.groupInterface)
        self.buttonHelpTranslation.setObjectName("buttonHelpTranslation")
        self.gridLayout.addWidget(self.buttonHelpTranslation, 0, 2, 1, 1)
        self.verticalLayout_3.addWidget(self.groupInterface)
        self.groupVieoApp = QtWidgets.QGroupBox(self.tabOthers)
        self.groupVieoApp.setObjectName("groupVieoApp")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupVieoApp)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.buttonVideoAppLocationChoose = QtWidgets.QPushButton(self.groupVieoApp)
        self.buttonVideoAppLocationChoose.setObjectName("buttonVideoAppLocationChoose")
        self.gridLayout_3.addWidget(self.buttonVideoAppLocationChoose, 0, 2, 1, 1)
        self.inputVideoAppLocation = QtWidgets.QLineEdit(self.groupVieoApp)
        self.inputVideoAppLocation.setObjectName("inputVideoAppLocation")
        self.gridLayout_3.addWidget(self.inputVideoAppLocation, 0, 1, 1, 1)
        self.textVideoAppParams = QtWidgets.QLabel(self.groupVieoApp)
        self.textVideoAppParams.setObjectName("textVideoAppParams")
        self.gridLayout_3.addWidget(self.textVideoAppParams, 1, 0, 1, 1)
        self.inputVideoAppParams = QtWidgets.QLineEdit(self.groupVieoApp)
        self.inputVideoAppParams.setObjectName("inputVideoAppParams")
        self.gridLayout_3.addWidget(self.inputVideoAppParams, 1, 1, 1, 1)
        self.textVideoAppLocation = QtWidgets.QLabel(self.groupVieoApp)
        self.textVideoAppLocation.setObjectName("textVideoAppLocation")
        self.gridLayout_3.addWidget(self.textVideoAppLocation, 0, 0, 1, 1)
        self.textVideoAppHelp = QtWidgets.QLabel(self.groupVieoApp)
        self.textVideoAppHelp.setObjectName("textVideoAppHelp")
        self.gridLayout_3.addWidget(self.textVideoAppHelp, 2, 1, 1, 2)
        self.verticalLayout_3.addWidget(self.groupVieoApp)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.tabsPreferences.addTab(self.tabOthers, "")
        self.verticalLayout_5.addWidget(self.tabsPreferences)
        self.layoutPreferencesDialogButtons = QtWidgets.QHBoxLayout()
        self.layoutPreferencesDialogButtons.setObjectName("layoutPreferencesDialogButtons")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.layoutPreferencesDialogButtons.addItem(spacerItem1)
        self.buttonApplyChanges = QtWidgets.QPushButton(PreferencesDialog)
        self.buttonApplyChanges.setObjectName("buttonApplyChanges")
        self.layoutPreferencesDialogButtons.addWidget(self.buttonApplyChanges)
        self.buttonCancel = QtWidgets.QPushButton(PreferencesDialog)
        self.buttonCancel.setObjectName("buttonCancel")
        self.layoutPreferencesDialogButtons.addWidget(self.buttonCancel)
        self.verticalLayout_5.addLayout(self.layoutPreferencesDialogButtons)

        self.retranslateUi(PreferencesDialog)
        self.providerStack.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(PreferencesDialog)
        PreferencesDialog.setTabOrder(self.tabsPreferences, self.scrollAreaSearch)
        PreferencesDialog.setTabOrder(self.scrollAreaSearch, self.optionDlDestinationSame)
        PreferencesDialog.setTabOrder(self.optionDlDestinationSame, self.optionDlDestinationAsk)
        PreferencesDialog.setTabOrder(self.optionDlDestinationAsk, self.optionDlDestinationUser)
        PreferencesDialog.setTabOrder(self.optionDlDestinationUser, self.inputDlDestinationUser)
        PreferencesDialog.setTabOrder(self.inputDlDestinationUser, self.buttonDlDestinationUser)
        PreferencesDialog.setTabOrder(self.buttonDlDestinationUser, self.optionSubFnSame)
        PreferencesDialog.setTabOrder(self.optionSubFnSame, self.optionSubFnSameLang)
        PreferencesDialog.setTabOrder(self.optionSubFnSameLang, self.optionSubFnSameLangUploader)
        PreferencesDialog.setTabOrder(self.optionSubFnSameLangUploader, self.optionSubFnOnline)
        PreferencesDialog.setTabOrder(self.optionSubFnOnline, self.optionUlDefaultLanguage)
        PreferencesDialog.setTabOrder(self.optionUlDefaultLanguage, self.optionInterfaceLanguage)
        PreferencesDialog.setTabOrder(self.optionInterfaceLanguage, self.buttonHelpTranslation)
        PreferencesDialog.setTabOrder(self.buttonHelpTranslation, self.inputVideoAppLocation)
        PreferencesDialog.setTabOrder(self.inputVideoAppLocation, self.buttonVideoAppLocationChoose)
        PreferencesDialog.setTabOrder(self.buttonVideoAppLocationChoose, self.inputVideoAppParams)
        PreferencesDialog.setTabOrder(self.inputVideoAppParams, self.buttonApplyChanges)
        PreferencesDialog.setTabOrder(self.buttonApplyChanges, self.buttonCancel)

    def retranslateUi(self, PreferencesDialog):
        _translate = QtCore.QCoreApplication.translate
        PreferencesDialog.setWindowTitle(_("Settings"))
        self.groupBoxSearchLanguages.setTitle(_("Filter search results by these languages:"))
        self.tabsPreferences.setTabText(self.tabsPreferences.indexOf(self.tabSearch), _("Search"))
        self.groupBoxDlDestinationFolder.setTitle(_("Destination folder:"))
        self.optionDlDestinationSame.setText(_("Same folder as video file"))
        self.optionDlDestinationAsk.setText(_("Always ask user"))
        self.optionDlDestinationUser.setText(_("Predefined folder:"))
        self.buttonDlDestinationUser.setText(_("Browse..."))
        self.groupBoxSubFn.setTitle(_("Filename of the Subtitle:"))
        self.optionSubFnSame.setText(_("Same name as video file"))
        self.optionSubFnSameLang.setText(_("Same name as video file + language code (ex: StarWarsCD1.eng.srt)"))
        self.optionSubFnSameLangUploader.setText(_("Same name as video file + language code + Uploader name (ex: StarWarsCD1.eng.JohnDoe.srt)"))
        self.optionSubFnOnline.setText(_("Same name as the online subtitle"))
        self.tabsPreferences.setTabText(self.tabsPreferences.indexOf(self.tabDownload), _("Download"))
        self.textUlDefaultLanguage.setText(_("Default language of uploaded subtitles"))
        self.tabsPreferences.setTabText(self.tabsPreferences.indexOf(self.tabUpload), _("Upload"))
        self.tabsPreferences.setTabText(self.tabsPreferences.indexOf(self.tabProviders), _("Providers"))
        self.groupInterface.setTitle(_("Interface"))
        self.textInterfaceLanguage.setText(_("Interface Language:"))
        self.buttonHelpTranslation.setText(_("Translate This Application..."))
        self.groupVieoApp.setTitle(_("External application for video playback"))
        self.buttonVideoAppLocationChoose.setText(_("Browse..."))
        self.textVideoAppParams.setText(_("Parameters:"))
        self.textVideoAppLocation.setText(_("Video Player:"))
        self.textVideoAppHelp.setText(_("{0} = video file path; {1} = subtitle path"))
        self.tabsPreferences.setTabText(self.tabsPreferences.indexOf(self.tabOthers), _("Others"))
        self.buttonApplyChanges.setText(_("Save"))
        self.buttonCancel.setText(_("Cancel"))


from subdownloader.client.gui.views.language import InterfaceLanguageComboBox, LanguageComboBox
