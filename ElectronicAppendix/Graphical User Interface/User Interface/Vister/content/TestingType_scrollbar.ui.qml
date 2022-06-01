

/*
This is a UI file (.ui.qml) that is intended to be edited in Qt Design Studio only.
It is supposed to be strictly declarative and only uses a subset of QML. If you edit
this file manually, you might introduce QML code that is not supported by Qt Design Studio.
Check out https://doc.qt.io/qtcreator/creator-quick-ui-forms.html for details on .ui.qml files.
*/
import QtQuick 2.15
import QtQuick.Controls 2.15

Slider {
    id: control
    value: 0.5

    background: background_rec

    Rectangle {
        x: control.leftPadding
        y: control.topPadding + control.availableHeight / 2 - height / 2
        implicitWidth: 200
        implicitHeight: 4
        parent: control.background
        id: backgroundRect

        width: control.availableWidth
        height: implicitHeight
        radius: 2
        color: "#bdbebf"
    }

    handle: Item {
        x: control.leftPadding + control.visualPosition * (control.availableWidth - width)
        y: control.topPadding + control.availableHeight / 2 - height / 2
        height: handleItem.height
        width: handleItem.width
    }

    Image {
        id: background_rec
        x: control.leftPadding
        y: control.topPadding + control.availableHeight / 2 - height / 2
        implicitWidth: 200
        implicitHeight: 4

        parent: control.background
        source: "images/Rectangle 979.png"
        fillMode: Image.PreserveAspectFit
    }
    states: [
        State {
            name: "normal"
            when: !control.pressed
        },
        State {
            name: "pressed"
            when: control.pressed

            PropertyChanges {
                target: control
                orientation: Qt.Vertical
            }
        }
    ]
}
