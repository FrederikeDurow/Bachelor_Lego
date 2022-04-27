

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
    width: 401
    height: 467
    opacity: 1
    visible: true
    hoverEnabled: true
    layer.format: ShaderEffectSource.RGBA
    font.pointSize: 0
    display: AbstractButton.IconOnly
    leftPadding: 4
    rightPadding: 4

    clip: false

    Image {
        id: load_Project_Button
        x: -19
        y: -14
        visible: true
        source: "images/Load_Project_Button.png"
        fillMode: Image.PreserveAspectFit

        Image {
            id: rectangle739
            x: 16
            y: 13
            visible: false
            source: "images/Rectangle 739.png"
            fillMode: Image.PreserveAspectFit
        }
    }

    states: [
        State {
            name: "normal"
            when: !control.down

            PropertyChanges {
                target: load_Project_Button
                x: -19
                y: -14
            }

            PropertyChanges {
                target: control
                width: 401
                height: 467
                hoverEnabled: true
            }
        },
        State {
            name: "down"
            when: control.down

            PropertyChanges {
                target: rectangle739
                visible: true
                rotation: -180
            }

            PropertyChanges {
                target: control
                hoverEnabled: true
                clip: false
            }
        },
        State {
            name: "hover"
            when: control.hovered

            PropertyChanges {
                target: rectangle739
                visible: true
                rotation: 0
            }

            PropertyChanges {
                target: control
                visible: true
                enabled: true
                hoverEnabled: true
                highlighted: false
                clip: false
            }
        }
    ]
}

/*##^##
Designer {
    D{i:0;formeditorZoom:1.75}
}
##^##*/

