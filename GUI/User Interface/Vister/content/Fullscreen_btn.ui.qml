

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
    width: 36
    height: 36
    leftPadding: 4
    rightPadding: 4

    text: ""
    display: AbstractButton.IconOnly

    Rectangle {
        id: rectangle
        x: 0
        y: 0
        width: 36
        height: 36
        color: "#161c28"

        Image {
            id: out
            x: 8
            y: 8
            width: 20
            height: 20
            source: "images/Out.png"
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

            PropertyChanges {
                target: rectangle
                color: "#707c8d"
            }
        }
    ]
}

/*##^##
Designer {
    D{i:0;formeditorZoom:6}
}
##^##*/

