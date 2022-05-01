

/*
This is a UI file (.ui.qml) that is intended to be edited in Qt Design Studio only.
It is supposed to be strictly declarative and only uses a subset of QML. If you edit
this file manually, you might introduce QML code that is not supported by Qt Design Studio.
Check out https://doc.qt.io/qtcreator/creator-quick-ui-forms.html for details on .ui.qml files.
*/
import QtQuick 2.15
import QtQuick.Controls 2.15

Button {
    id: setting_control
    width: 119
    height: 84
    leftPadding: 4
    rightPadding: 4

    text: ""
    display: AbstractButton.IconOnly

    Image {
        id: settings_Button
        x: -15
        y: -15
        source: "images/Settings_Button.png"
        fillMode: Image.PreserveAspectFit
    }

    Image {
        id: rectangle740
        x: 1
        y: -2
        visible: false
        source: "images/Rectangle 740.png"
        fillMode: Image.PreserveAspectFit
    }

    states: [
        State {
            name: "normal"
            when: !setting_control.down
        },
        State {
            name: "down"
            when: setting_control.down

            PropertyChanges {
                target: rectangle740
                visible: true
            }
        }
    ]
}
