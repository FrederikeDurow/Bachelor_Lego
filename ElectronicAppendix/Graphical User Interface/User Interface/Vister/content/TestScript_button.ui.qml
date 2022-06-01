

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
    width: 110
    height: 34
    leftPadding: 4
    rightPadding: 4

    text: ""
    display: AbstractButton.IconOnly

    Image {
        id: rectangle911
        x: -22
        y: -8
        source: "../../Components/Testing_view/Universal Robot/Rectangle 911.png"
        fillMode: Image.PreserveAspectFit

        Image {
            id: testscript
            x: 44
            y: 15
            source: "images/Test script.png"
            fillMode: Image.PreserveAspectFit
        }
    }

    Image {
        id: rectangle912
        x: -12
        y: -1
        visible: false
        source: "../../Components/Testing_view/Universal Robot/Rectangle 912.png"
        fillMode: Image.PreserveAspectFit
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
                target: rectangle912
                visible: true
            }
        }
    ]
}

/*##^##
Designer {
    D{i:0;formeditorZoom:1.75}
}
##^##*/

