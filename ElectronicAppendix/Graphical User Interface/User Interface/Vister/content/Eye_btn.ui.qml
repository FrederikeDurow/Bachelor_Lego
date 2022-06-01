

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
    width: 38
    height: 37
    visible: true
    leftPadding: 4
    rightPadding: 4

    text: ""
    display: AbstractButton.IconOnly


    states: [
        State {
            name: "normal"
            when: !control.down

            PropertyChanges {
                target: rectangle733
                visible: false
            }
        },
        State {
            name: "down"
            when: control.down

            PropertyChanges {
                target: rectangle733
                x: -1
                y: -2
                visible: true
            }
        }
    ]

    Image {
        id: rectangle679
        x: -8
        y: -11
        source: "../../Components/Setup_views/Rectangle 679.png"
        fillMode: Image.PreserveAspectFit
    }
    Image {
        id: eye_fill
        x: 0
        y: 4
        source: "../../Components/Setup_views/Eye_fill.png"
        fillMode: Image.PreserveAspectFit
    }

    Image {
        id: rectangle733
        x: -1
        y: -2
        visible: false
        source: "../../Components/Setup_views/Rectangle 733.png"
        fillMode: Image.PreserveAspectFit
    }
}

/*##^##
Designer {
    D{i:0;formeditorZoom:3;height:37;width:38}
}
##^##*/

