

/*
This is a UI file (.ui.qml) that is intended to be edited in Qt Design Studio only.
It is supposed to be strictly declarative and only uses a subset of QML. If you edit
this file manually, you might introduce QML code that is not supported by Qt Design Studio.
Check out https://doc.qt.io/qtcreator/creator-quick-ui-forms.html for details on .ui.qml files.
*/
import QtQuick 2.15
import QtQuick.Controls 2.15

Slider {
    id: slider
    padding: 4
    leftPadding: 4
    topPadding: 4
    bottomPadding: 4
    orientation: Qt.Vertical
    value: 0

    stepSize: 0
    to: 100
    snapMode: Slider.NoSnap

    background: Image {
        id: rectangle979
        height: slider.availableHeight
        y: slider.topPadding
        source: "../../Components/Select_type_section/Rectangle 979.png"
        fillMode: Image.PreserveAspectFit
    }

    handle: Image {
        id: component801
        x: slider.width - slider.leftPadding - width
        source: "images/Component 80 – 1.png"
        fillMode: Image.PreserveAspectFit
        y: slider.visualPosition * (slider.availableHeight - 190)
    }

    states: [
        State {
            name: "normal"
            when: !control.pressed
        },
        State {
            name: "pressed"
            when: control.pressed
        }
    ]
}

/*##^##
Designer {
    D{i:0;formeditorZoom:1.75}
}
##^##*/

