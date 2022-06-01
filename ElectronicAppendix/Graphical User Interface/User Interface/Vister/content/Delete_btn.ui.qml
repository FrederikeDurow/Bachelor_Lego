

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
    width: 37
    height: 40
    visible: true
    leftPadding: 4
    rightPadding: 4

    text: ""

    Image {
        id: rectangle679
        x: -8
        y: -10
        source: "../../Components/Setup_views/Rectangle 679.png"
        fillMode: Image.PreserveAspectFit
    }

    Image {
        id: trash1
        x: 11
        y: 12
        source: "../../Components/Setup_views/Trash-1.png"
        fillMode: Image.PreserveAspectFit
    }

    Image {
        id: rectangle733
        x: -2
        y: 0
        visible: false
        source: "../../Components/Setup_views/Rectangle 733.png"
        fillMode: Image.PreserveAspectFit
    }

    states: [
        State {
            name: "normal"
            when: !control.down

            PropertyChanges {
                target: control
                width: 37
                height: 40
                text: ""
            }

            PropertyChanges {
                target: rectangle679
                x: -8
                y: -10
            }
        },
        State {
            name: "down"
            when: control.down

            PropertyChanges {
                target: rectangle733
                visible: true
            }
        }
    ]
}

/*##^##
Designer {
    D{i:0;height:40;width:37}
}
##^##*/

