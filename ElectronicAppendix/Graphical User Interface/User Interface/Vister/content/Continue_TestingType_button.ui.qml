

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
    width: 347
    height: 40

    leftPadding: 4
    rightPadding: 4

    Image {
        id: rectangle987
        x: -16
        y: -14
        source: "images/Rectangle 987.png"
        fillMode: Image.PreserveAspectFit

        Image {
            id: rectangle988
            x: 16
            y: 13
            visible: false
            source: "images/Rectangle 988.png"
            fillMode: Image.PreserveAspectFit
        }
    }

    Image {
        id: continue1
        x: 123
        y: 1
        source: "images/Continue.png"
        fillMode: Image.PreserveAspectFit
    }

    states: [
        State {
            name: "normal"
            when: !control.down

            PropertyChanges {
                target: control
                width: 347
                height: 40
            }

            PropertyChanges {
                target: rectangle987
                x: -16
                y: -14
            }

            PropertyChanges {
                target: continue1
                x: 123
                y: 1
            }

            PropertyChanges {
                target: rectangle988
                visible: false
            }
        },
        State {
            name: "down"
            when: control.down

            PropertyChanges {
                target: rectangle988
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

