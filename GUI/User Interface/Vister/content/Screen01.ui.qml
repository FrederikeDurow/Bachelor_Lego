/*
This is a UI file (.ui.qml) that is intended to be edited in Qt Design Studio only.
It is supposed to be strictly declarative and only uses a subset of QML. If you edit
this file manually, you might introduce QML code that is not supported by Qt Design Studio.
Check out https://doc.qt.io/qtcreator/creator-quick-ui-forms.html for details on .ui.qml files.
*/

import QtQuick
import QtQuick.Controls
import Vister

Rectangle {
    width: Constants.width
    height: Constants.height

    color: Constants.backgroundColor

    Image {
        id: edit_dropdown
        x: 0
        y: 0
        source: "C:/Users/rasm4/OneDrive/Dokumenter/Test/Edit_dropdown.svg"
        fillMode: Image.PreserveAspectFit
    }

    Image {
        id: edit_dropdown1
        x: 265
        y: 351
        width: 430
        height: 195
        source: "images/Edit_dropdown.svg"
        fillMode: Image.PreserveAspectFit
    }

    Image {
        id: load_Project_Button
        x: 0
        y: 0
        source: "C:/Users/rasm4/OneDrive/Dokumenter/Test/Load_Project_Button.svg"
        fillMode: Image.PreserveAspectFit
    }

    Image {
        id: load_Project_Button1
        x: 265
        y: 215
        source: "images/Load_Project_Button.svg"
        fillMode: Image.PreserveAspectFit
    }
}

/*##^##
Designer {
    D{i:0;formeditorZoom:1.1}
}
##^##*/
