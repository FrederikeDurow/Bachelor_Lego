

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
    width: 72
    height: 70

    leftPadding: 4
    rightPadding: 4

    text: ""
    display: AbstractButton.IconOnly

    Image {
        id: rectangle903
        x: -18
        y: -17
        source: "images/Rectangle 903.png"
        fillMode: Image.PreserveAspectFit
    }

    Image {
        id: file_dock_fill
        x: 15
        y: 0
        source: "../../Components/Testing_view/Universal Robot/File_dock_fill.png"
        fillMode: Image.PreserveAspectFit

        Text {
            id: text1
            x: 9
            y: 57
            color: "#ffffff"
            text: qsTr("Guide")
            font.pixelSize: 10
        }
    }

    Image {
        id: rectangle958
        x: -2
        y: -4
        visible: false
        source: "images/Rectangle 958.png"
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
                target: rectangle958
                visible: true
            }
        }
    ]
}

/*##^##
Designer {
    D{i:0;formeditorZoom:2}
}
##^##*/

