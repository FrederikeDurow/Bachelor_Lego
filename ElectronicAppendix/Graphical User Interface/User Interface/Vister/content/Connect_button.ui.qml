/*
This is a UI file (.ui.qml) that is intended to be edited in Qt Design Studio only.
It is supposed to be strictly declarative and only uses a subset of QML. If you edit
this file manually, you might introduce QML code that is not supported by Qt Design Studio.
Check out https://doc.qt.io/qtcreator/creator-quick-ui-forms.html for details on .ui.qml files.
*/

import QtQuick 2.15
import QtQuick.Controls 2.15

Button {
    id: control
    width: 163
    height: 160

    leftPadding: 4
    rightPadding: 4

    text: ""
    display: AbstractButton.IconOnly


    Image {
        id: rectangle902
        x: -19
        y: -17
        source: "images/Rectangle 902.png"
        fillMode: Image.PreserveAspectFit

        Text {
            id: text1
            x: 72
            y: 151
            color: "#ffffff"
            text: qsTr("Connect")
            font.pixelSize: 16
            font.family: "roboto"
        }

        Image {
            id: rectangle957
            x: 16
            y: 13
            source: "images/Rectangle 957.png"
            fillMode: Image.PreserveAspectFit
        }
    }

    states: [
        State {
            name: "normal"
            when: !control.down
        },
        State {
            name: "down"
            when: control.down
        }
    ]
    Image {
        id: uR
        x: 32
        y: 5
        source: "images/UR.png"
        fillMode: Image.PreserveAspectFit
    }
}

/*##^##
Designer {
    D{i:0;formeditorZoom:1.75}
}
##^##*/
