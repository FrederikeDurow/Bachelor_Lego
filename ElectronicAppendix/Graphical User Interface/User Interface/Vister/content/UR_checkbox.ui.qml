

/*
This is a UI file (.ui.qml) that is intended to be edited in Qt Design Studio only.
It is supposed to be strictly declarative and only uses a subset of QML. If you edit
this file manually, you might introduce QML code that is not supported by Qt Design Studio.
Check out https://doc.qt.io/qtcreator/creator-quick-ui-forms.html for details on .ui.qml files.
*/
import QtQuick 2.15
import QtQuick.Controls 2.15

CheckBox {
    id: control
    width: 10
    height: 10
    text: qsTr("CheckBox")
    checked: true

    indicator: indicatorRectangle
    Rectangle {
        id: indicatorRectangle
        x: 0
        y: 0
        implicitWidth: 26
        implicitHeight: 26
        width: 10
        height: 10
        color: "#2a3541"
        radius: 3
        border.color: "#3d434d"

        Rectangle {
            id: rectangle
            width: 14
            height: 14
            x: 6
            y: 6
            radius: 2
            visible: false
            color: "#047eff"
        }
    }
    states: [
        State {
            name: "checked"
            when: control.checked

            PropertyChanges {
                target: rectangle
                x: 3
                y: 3
                width: 4
                height: 4
                visible: true
                color: "#395c34"
                border.color: "#4fa93e"
            }

            PropertyChanges {
                target: indicatorRectangle
                color: "#2a3541"
                border.color: "#3d434d"
            }
        },
        State {
            name: "unchecked"
            when: !control.checked

            PropertyChanges {
                target: rectangle
                visible: false
            }

            PropertyChanges {
                target: indicatorRectangle
                color: "#2a3541"
                border.color: "#3d434d"
            }
        }
    ]
}

/*##^##
Designer {
    D{i:0;formeditorZoom:8}
}
##^##*/
