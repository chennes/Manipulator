# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/mau/Downloads/Manipulator-hdpi/Resources/ui/align-tool-docked-v1.9-highdpi.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DockWidget(object):
    def setupUi(self, DockWidget):
        DockWidget.setObjectName("DockWidget")
        DockWidget.resize(353, 330)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("/home/mau/Downloads/Manipulator-hdpi/Resources/ui/Center-Align.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        DockWidget.setWindowIcon(icon)
        DockWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        DockWidget.setFeatures(QtWidgets.QDockWidget.DockWidgetFloatable|QtWidgets.QDockWidget.DockWidgetMovable)
        DockWidget.setAllowedAreas(QtCore.Qt.LeftDockWidgetArea|QtCore.Qt.RightDockWidgetArea)
        self.dockWidgetContents = QtWidgets.QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.dockWidgetContents)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.AlignGroup = QtWidgets.QGroupBox(self.dockWidgetContents)
        self.AlignGroup.setTitle("Align on")
        self.AlignGroup.setObjectName("AlignGroup")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.AlignGroup)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout_12 = QtWidgets.QGridLayout()
        self.gridLayout_12.setSpacing(2)
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.cbX = QtWidgets.QCheckBox(self.AlignGroup)
        self.cbX.setMinimumSize(QtCore.QSize(48, 32))
        self.cbX.setMaximumSize(QtCore.QSize(64, 128))
        self.cbX.setToolTip("center on X")
        self.cbX.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("/home/mau/Downloads/Manipulator-hdpi/Resources/ui/Xaxis.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cbX.setIcon(icon1)
        self.cbX.setIconSize(QtCore.QSize(16, 16))
        self.cbX.setChecked(True)
        self.cbX.setObjectName("cbX")
        self.gridLayout_12.addWidget(self.cbX, 0, 1, 1, 1)
        self.cbZ = QtWidgets.QCheckBox(self.AlignGroup)
        self.cbZ.setMinimumSize(QtCore.QSize(48, 32))
        self.cbZ.setMaximumSize(QtCore.QSize(64, 128))
        self.cbZ.setToolTip("center on Z")
        self.cbZ.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("/home/mau/Downloads/Manipulator-hdpi/Resources/ui/Zaxis.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cbZ.setIcon(icon2)
        self.cbZ.setIconSize(QtCore.QSize(16, 16))
        self.cbZ.setChecked(True)
        self.cbZ.setObjectName("cbZ")
        self.gridLayout_12.addWidget(self.cbZ, 2, 1, 1, 1)
        self.cbY = QtWidgets.QCheckBox(self.AlignGroup)
        self.cbY.setMinimumSize(QtCore.QSize(48, 32))
        self.cbY.setMaximumSize(QtCore.QSize(64, 128))
        self.cbY.setToolTip("center on Y")
        self.cbY.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("/home/mau/Downloads/Manipulator-hdpi/Resources/ui/Yaxis.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cbY.setIcon(icon3)
        self.cbY.setIconSize(QtCore.QSize(16, 16))
        self.cbY.setChecked(True)
        self.cbY.setObjectName("cbY")
        self.gridLayout_12.addWidget(self.cbY, 1, 1, 1, 1)
        self.rbCenters = QtWidgets.QRadioButton(self.AlignGroup)
        self.rbCenters.setMinimumSize(QtCore.QSize(64, 32))
        self.rbCenters.setToolTip("Align Centers")
        self.rbCenters.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("/home/mau/Downloads/Manipulator-hdpi/Resources/ui/Centers.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.rbCenters.setIcon(icon4)
        self.rbCenters.setIconSize(QtCore.QSize(26, 26))
        self.rbCenters.setChecked(False)
        self.rbCenters.setObjectName("rbCenters")
        self.gridLayout_12.addWidget(self.rbCenters, 0, 0, 1, 1)
        self.rbPlanes = QtWidgets.QRadioButton(self.AlignGroup)
        self.rbPlanes.setMinimumSize(QtCore.QSize(64, 32))
        self.rbPlanes.setToolTip("Align Planes")
        self.rbPlanes.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("/home/mau/Downloads/Manipulator-hdpi/Resources/ui/Planes.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.rbPlanes.setIcon(icon5)
        self.rbPlanes.setIconSize(QtCore.QSize(26, 26))
        self.rbPlanes.setChecked(False)
        self.rbPlanes.setObjectName("rbPlanes")
        self.gridLayout_12.addWidget(self.rbPlanes, 1, 0, 1, 1)
        self.rbPlanesCenters = QtWidgets.QRadioButton(self.AlignGroup)
        self.rbPlanesCenters.setMinimumSize(QtCore.QSize(64, 32))
        self.rbPlanesCenters.setToolTip("Align Centers & Planes")
        self.rbPlanesCenters.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("/home/mau/Downloads/Manipulator-hdpi/Resources/ui/Planes-Centers.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.rbPlanesCenters.setIcon(icon6)
        self.rbPlanesCenters.setIconSize(QtCore.QSize(26, 26))
        self.rbPlanesCenters.setChecked(True)
        self.rbPlanesCenters.setObjectName("rbPlanesCenters")
        self.gridLayout_12.addWidget(self.rbPlanesCenters, 2, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_12)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.gridLayout_4.addWidget(self.AlignGroup, 0, 1, 1, 1)
        self.ReferenceGroup = QtWidgets.QGroupBox(self.dockWidgetContents)
        self.ReferenceGroup.setTitle("Reference")
        self.ReferenceGroup.setObjectName("ReferenceGroup")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.ReferenceGroup)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.rbBBox = QtWidgets.QRadioButton(self.ReferenceGroup)
        self.rbBBox.setMinimumSize(QtCore.QSize(64, 32))
        self.rbBBox.setToolTip("Center of\n"
"Boundig Box")
        self.rbBBox.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("/home/mau/Downloads/Manipulator-hdpi/Resources/ui/Bbox.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.rbBBox.setIcon(icon7)
        self.rbBBox.setIconSize(QtCore.QSize(26, 26))
        self.rbBBox.setChecked(False)
        self.rbBBox.setObjectName("rbBBox")
        self.gridLayout_3.addWidget(self.rbBBox, 0, 0, 1, 1)
        self.rbMass = QtWidgets.QRadioButton(self.ReferenceGroup)
        self.rbMass.setMinimumSize(QtCore.QSize(64, 32))
        self.rbMass.setToolTip("Center of\n"
"Mass")
        self.rbMass.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("/home/mau/Downloads/Manipulator-hdpi/Resources/ui/Mass.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.rbMass.setIcon(icon8)
        self.rbMass.setIconSize(QtCore.QSize(26, 26))
        self.rbMass.setObjectName("rbMass")
        self.gridLayout_3.addWidget(self.rbMass, 0, 1, 1, 1)
        self.rbNormal = QtWidgets.QRadioButton(self.ReferenceGroup)
        self.rbNormal.setMinimumSize(QtCore.QSize(64, 32))
        self.rbNormal.setToolTip("Alignment Normal")
        self.rbNormal.setText("")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("/home/mau/Downloads/Manipulator-hdpi/Resources/ui/Normal-Up.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.rbNormal.setIcon(icon9)
        self.rbNormal.setIconSize(QtCore.QSize(26, 26))
        self.rbNormal.setChecked(True)
        self.rbNormal.setObjectName("rbNormal")
        self.gridLayout_3.addWidget(self.rbNormal, 1, 0, 1, 1)
        self.rbNormal_Inv = QtWidgets.QRadioButton(self.ReferenceGroup)
        self.rbNormal_Inv.setMinimumSize(QtCore.QSize(64, 32))
        self.rbNormal_Inv.setToolTip("Alignment Normal\n"
"Inverted")
        self.rbNormal_Inv.setText("")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("/home/mau/Downloads/Manipulator-hdpi/Resources/ui/Normal-Down.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.rbNormal_Inv.setIcon(icon10)
        self.rbNormal_Inv.setIconSize(QtCore.QSize(26, 26))
        self.rbNormal_Inv.setChecked(False)
        self.rbNormal_Inv.setObjectName("rbNormal_Inv")
        self.gridLayout_3.addWidget(self.rbNormal_Inv, 1, 1, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout_3)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.gridLayout_4.addWidget(self.ReferenceGroup, 0, 0, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout_4, 1, 0, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.Label_Align_Gui = QtWidgets.QLabel(self.dockWidgetContents)
        self.Label_Align_Gui.setToolTip("Ctrl+Click to select\n"
"Faces/Planes or Edges/Axis")
        self.Label_Align_Gui.setObjectName("Label_Align_Gui")
        self.gridLayout_2.addWidget(self.Label_Align_Gui, 0, 4, 1, 1)
        self.dock_float = QtWidgets.QPushButton(self.dockWidgetContents)
        self.dock_float.setMaximumSize(QtCore.QSize(28, 28))
        self.dock_float.setText("")
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap("/home/mau/Downloads/Manipulator-hdpi/Resources/ui/un_dock.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.dock_float.setIcon(icon11)
        self.dock_float.setIconSize(QtCore.QSize(16, 16))
        self.dock_float.setObjectName("dock_float")
        self.gridLayout_2.addWidget(self.dock_float, 0, 0, 1, 1)
        self.dock_minimize = QtWidgets.QPushButton(self.dockWidgetContents)
        self.dock_minimize.setMaximumSize(QtCore.QSize(28, 28))
        self.dock_minimize.setText("")
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap("/home/mau/Downloads/Manipulator-hdpi/Resources/ui/minimize.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.dock_minimize.setIcon(icon12)
        self.dock_minimize.setIconSize(QtCore.QSize(24, 24))
        self.dock_minimize.setObjectName("dock_minimize")
        self.gridLayout_2.addWidget(self.dock_minimize, 0, 1, 1, 1, QtCore.Qt.AlignTop)
        self.close = QtWidgets.QPushButton(self.dockWidgetContents)
        self.close.setMaximumSize(QtCore.QSize(28, 28))
        self.close.setText("")
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap("/home/mau/Downloads/Manipulator-hdpi/Resources/ui/closeW.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.close.setIcon(icon13)
        self.close.setIconSize(QtCore.QSize(24, 24))
        self.close.setObjectName("close")
        self.gridLayout_2.addWidget(self.close, 0, 3, 1, 1, QtCore.Qt.AlignTop)
        self.Help_Align = QtWidgets.QPushButton(self.dockWidgetContents)
        self.Help_Align.setMaximumSize(QtCore.QSize(28, 28))
        self.Help_Align.setText("")
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap("/home/mau/Downloads/Manipulator-hdpi/Resources/ui/help.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Help_Align.setIcon(icon14)
        self.Help_Align.setIconSize(QtCore.QSize(24, 24))
        self.Help_Align.setObjectName("Help_Align")
        self.gridLayout_2.addWidget(self.Help_Align, 0, 2, 1, 1, QtCore.Qt.AlignTop)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem2, 0, 5, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout_2, 0, 0, 1, 1)
        self.gridLayout_6 = QtWidgets.QGridLayout()
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.ControlsGroup = QtWidgets.QGroupBox(self.dockWidgetContents)
        self.ControlsGroup.setTitle("Controls")
        self.ControlsGroup.setObjectName("ControlsGroup")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.ControlsGroup)
        self.gridLayout_7.setObjectName("gridLayout_7")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_7.addItem(spacerItem3, 0, 2, 1, 1)
        self.cbHierarchy = QtWidgets.QCheckBox(self.ControlsGroup)
        self.cbHierarchy.setMinimumSize(QtCore.QSize(52, 48))
        self.cbHierarchy.setMaximumSize(QtCore.QSize(64, 128))
        self.cbHierarchy.setToolTip("use Part and Body\n"
"hierarchy in Aligning")
        self.cbHierarchy.setText("")
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap("/home/mau/Downloads/Manipulator-hdpi/Resources/ui/hierarchy.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cbHierarchy.setIcon(icon15)
        self.cbHierarchy.setIconSize(QtCore.QSize(26, 26))
        self.cbHierarchy.setChecked(True)
        self.cbHierarchy.setObjectName("cbHierarchy")
        self.gridLayout_7.addWidget(self.cbHierarchy, 0, 1, 1, 1)
        self.gridLayout_14 = QtWidgets.QGridLayout()
        self.gridLayout_14.setSpacing(2)
        self.gridLayout_14.setObjectName("gridLayout_14")
        self.Align = QtWidgets.QPushButton(self.ControlsGroup)
        self.Align.setMinimumSize(QtCore.QSize(48, 48))
        self.Align.setMaximumSize(QtCore.QSize(64, 64))
        self.Align.setText("")
        self.Align.setIcon(icon)
        self.Align.setIconSize(QtCore.QSize(32, 32))
        self.Align.setCheckable(False)
        self.Align.setChecked(False)
        self.Align.setObjectName("Align")
        self.gridLayout_14.addWidget(self.Align, 0, 0, 1, 1)
        self.XRayBtn = QtWidgets.QPushButton(self.ControlsGroup)
        self.XRayBtn.setMinimumSize(QtCore.QSize(48, 48))
        self.XRayBtn.setMaximumSize(QtCore.QSize(64, 64))
        self.XRayBtn.setToolTip("XRay toggle")
        self.XRayBtn.setText("")
        icon16 = QtGui.QIcon()
        icon16.addPixmap(QtGui.QPixmap("/home/mau/Downloads/Manipulator-hdpi/Resources/ui/xray.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.XRayBtn.setIcon(icon16)
        self.XRayBtn.setIconSize(QtCore.QSize(24, 24))
        self.XRayBtn.setCheckable(False)
        self.XRayBtn.setChecked(False)
        self.XRayBtn.setObjectName("XRayBtn")
        self.gridLayout_14.addWidget(self.XRayBtn, 0, 4, 1, 1)
        self.Undo_Align = QtWidgets.QPushButton(self.ControlsGroup)
        self.Undo_Align.setMinimumSize(QtCore.QSize(48, 48))
        self.Undo_Align.setMaximumSize(QtCore.QSize(64, 64))
        self.Undo_Align.setText("")
        icon17 = QtGui.QIcon()
        icon17.addPixmap(QtGui.QPixmap("/home/mau/Downloads/Manipulator-hdpi/Resources/ui/Undo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Undo_Align.setIcon(icon17)
        self.Undo_Align.setIconSize(QtCore.QSize(24, 24))
        self.Undo_Align.setCheckable(False)
        self.Undo_Align.setChecked(False)
        self.Undo_Align.setObjectName("Undo_Align")
        self.gridLayout_14.addWidget(self.Undo_Align, 0, 3, 1, 1)
        self.Move = QtWidgets.QPushButton(self.ControlsGroup)
        self.Move.setMinimumSize(QtCore.QSize(48, 48))
        self.Move.setMaximumSize(QtCore.QSize(64, 64))
        self.Move.setText("")
        icon18 = QtGui.QIcon()
        icon18.addPixmap(QtGui.QPixmap("/home/mau/Downloads/Manipulator-hdpi/Resources/ui/Move.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Move.setIcon(icon18)
        self.Move.setIconSize(QtCore.QSize(24, 24))
        self.Move.setCheckable(False)
        self.Move.setChecked(False)
        self.Move.setObjectName("Move")
        self.gridLayout_14.addWidget(self.Move, 0, 2, 1, 1)
        self.gridLayout_7.addLayout(self.gridLayout_14, 0, 0, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_7.addItem(spacerItem4, 1, 0, 1, 1)
        self.gridLayout_6.addWidget(self.ControlsGroup, 0, 0, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout_6, 2, 0, 1, 1)
        DockWidget.setWidget(self.dockWidgetContents)

        self.retranslateUi(DockWidget)
        QtCore.QMetaObject.connectSlotsByName(DockWidget)

    def retranslateUi(self, DockWidget):
        _translate = QtCore.QCoreApplication.translate
        DockWidget.setWindowTitle(_translate("DockWidget", "Align tool"))
        self.Label_Align_Gui.setText(_translate("DockWidget", "<b>Ctrl+Click</b> to add selection:<br>Planes/Faces, Edges/Axis"))
        self.dock_float.setToolTip(_translate("DockWidget", "expand"))
        self.dock_minimize.setToolTip(_translate("DockWidget", "minimize"))
        self.close.setToolTip(_translate("DockWidget", "close"))
        self.Help_Align.setToolTip(_translate("DockWidget", "close"))
        self.Align.setToolTip(_translate("DockWidget", "Align objects"))
        self.Undo_Align.setToolTip(_translate("DockWidget", "Undo last Alignment"))
        self.Move.setToolTip(_translate("DockWidget", "Move selected"))
