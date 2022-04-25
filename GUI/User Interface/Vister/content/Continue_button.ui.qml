

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
    width: 693
    height: 41

    implicitWidth: Math.max(
                       buttonBackground ? buttonBackground.implicitWidth : 0,
                       textItem.implicitWidth + leftPadding + rightPadding)
    implicitHeight: Math.max(
                        buttonBackground ? buttonBackground.implicitHeight : 0,
                        textItem.implicitHeight + topPadding + bottomPadding)
    leftPadding: 4
    rightPadding: 4

    text: ""
    display: AbstractButton.IconOnly

    Image {
        id: rectangle889
        x: -18
        y: -13
        height: 74
        source: "images/Rectangle 889.png"
        fillMode: Image.PreserveAspectFit

        Image {
            id: continue1
            x: 314
            y: 16
            source: "images/Continue.png"
            fillMode: Image.PreserveAspectFit
        }
    }

    Image {
        id: rectangle890
        x: -2
        y: 0
        visible: false
        source: "images/Rectangle 890.png"
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
                target: rectangle890
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

