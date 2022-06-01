

/*
This is a UI file (.ui.qml) that is intended to be edited in Qt Design Studio only.
It is supposed to be strictly declarative and only uses a subset of QML. If you edit
this file manually, you might introduce QML code that is not supported by Qt Design Studio.
Check out https://doc.qt.io/qtcreator/creator-quick-ui-forms.html for details on .ui.qml files.
*/
import QtQuick 2.15
import QtQuick.Controls 2.15

Button {
    id: ur_control
    width: 620
    height: 304

    leftPadding: 4
    rightPadding: 4

    text: ""
    display: AbstractButton.IconOnly

    Image {
        id: universalRobots
        x: -17
        y: -16
        source: "images/Universal Robots.png"
        fillMode: Image.PreserveAspectFit
    }

    Image {
        id: rectangle739
        x: -1
        y: -4
        width: 621
        height: 312
        visible: false
        source: "images/Rectangle 739.png"
        fillMode: Image.Stretch
    }

    states: [
        State {
            name: "normal"
            when: !ur_control.down
        },
        State {
            name: "down"
            when: ur_control.down

            PropertyChanges {
                target: rectangle739
                visible: true
            }
        }
    ]
}

/*##^##
Designer {
    D{i:0;formeditorZoom:1.66}
}
##^##*/
