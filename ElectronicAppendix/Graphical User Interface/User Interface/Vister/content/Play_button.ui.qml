

/*
This is a UI file (.ui.qml) that is intended to be edited in Qt Design Studio only.
It is supposed to be strictly declarative and only uses a subset of QML. If you edit
this file manually, you might introduce QML code that is not supported by Qt Design Studio.
Check out https://doc.qt.io/qtcreator/creator-quick-ui-forms.html for details on .ui.qml files.
*/
import QtQuick 2.15
import QtQuick.Controls 2.15

Button {
    id: play_control
    width: 230
    height: 84

    leftPadding: 4
    rightPadding: 4

    text: ""
    display: AbstractButton.IconOnly

    Image {
        id: play_Button
        x: -16
        y: -15
        source: "images/Play_Button.png"
        fillMode: Image.PreserveAspectFit
    }

    Image {
        id: rectangle741
        x: 0
        y: -2
        visible: false
        source: "images/Rectangle 741.png"
        fillMode: Image.PreserveAspectFit
    }

    states: [
        State {
            name: "normal"
            when: !play_control.down
        },
        State {
            name: "down"
            when: play_control.down

            PropertyChanges {
                target: play_Button
                x: -16
                y: -15
            }

            PropertyChanges {
                target: rectangle741
                x: 0
                y: -2
                width: 233
                height: 88
                visible: true
            }
        }
    ]
}

/*##^##
Designer {
    D{i:0;formeditorZoom:0.75}
}
##^##*/

