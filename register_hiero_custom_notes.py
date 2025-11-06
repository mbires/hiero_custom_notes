# -*- coding: utf-8 -*-

import nuke
import os

from hiero.ui import registerAction

if nuke.NUKE_VERSION_MAJOR > 15:
    from PySide6.QtGui import QIcon, QAction
else:
    from PySide2.QtGui import QIcon
    from PySide2.QtWidgets import QAction

gizmo_path = os.path.dirname(__file__)
nuke.pluginAddPath(gizmo_path)

try:
    nuke.load("{}/{}".format(gizmo_path, 'MB_hiero_custom_notes.gizmo'))
    print("Gizmo 'MB_hiero_custom_notes' loaded")
except Exception as e:
    print(f"Failed to load gizmo MB_hiero_custom_notes: {e}")

# This creates an action with an icon and effect
custom_notes = QAction(QIcon("icons:LUT.png"), "MB Custom Notes", None)

# Soft effect actions can be found by prefixing the QAction's objectName with: 'foundry.timeline.effect'
custom_notes.setObjectName("foundry.timeline.effect.CustomNotes")
custom_notes.setData('MB_hiero_custom_notes')

# This registers your custom action with the Effects Menu
registerAction(custom_notes)
