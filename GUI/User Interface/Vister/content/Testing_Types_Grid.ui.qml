

/*
This is a UI file (.ui.qml) that is intended to be edited in Qt Design Studio only.
It is supposed to be strictly declarative and only uses a subset of QML. If you edit
this file manually, you might introduce QML code that is not supported by Qt Design Studio.
Check out https://doc.qt.io/qtcreator/creator-quick-ui-forms.html for details on .ui.qml files.
*/
import QtQuick 2.15

GridView {

    width: 544
    height: 520
    property string property0: "none.none"
    layer.enabled: false
    layoutDirection: Qt.LeftToRight
    preferredHighlightEnd: 100

    contentWidth: 0
    clip: true

    cellWidth: 180
    cellHeight: 180

    model: TestingTypes_model {}

    highlight: Rectangle {
        width: 120
        height: 120
        color: "#ffffff"
        radius: 6
        border.color: "#ffffff"
        border.width: 8
    }

    delegate: Testing_Types_GridDelegate {}
}

/*##^##
Designer {
    D{i:0;height:520;width:544}
}
##^##*/

