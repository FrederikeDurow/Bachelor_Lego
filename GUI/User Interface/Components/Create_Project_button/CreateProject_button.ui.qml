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
    width: 407
    height: 472
    visible: true

    implicitWidth: Math.max(
                       buttonBackground ? buttonBackground.implicitWidth : 0,
                       textItem.implicitWidth + leftPadding + rightPadding)
    implicitHeight: Math.max(
                        buttonBackground ? buttonBackground.implicitHeight : 0,
                        textItem.implicitHeight + topPadding + bottomPadding)
    leftPadding: 4
    rightPadding: 4

    text: "My Button"
    highlighted: false
    flat: false


    Image {
        id: new_Project_Button
        x: -228
        y: -189
        source: "New_Project_Button.png"
        fillMode: Image.PreserveAspectFit
    }

    states: [
        State {
            name: "normal"
            when: !control.down

            PropertyChanges {
                target: control
                visible: true
                hoverEnabled: true
            }

            PropertyChanges {
                target: rectangle739
                visible: false
            }
        },
        State {
            name: "down"
            when: control.down

            PropertyChanges {
                target: control
                width: 437
                height: 502
            }

            PropertyChanges {
                target: rectangle739
                x: 16
                y: 13
                visible: true
                rotation: -180
            }

            PropertyChanges {
                target: new_Project_Button
                x: 0
                y: 0
            }
        }
    ]
    Image {
        id: rectangle739
        x: 118
        y: 46
        visible: false
        source: "Rectangle 739.png"
        fillMode: Image.PreserveAspectFit
    }
}

/*##^##
Designer {
    D{i:0;formeditorZoom:1.5}
}
##^##*/
