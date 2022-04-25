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
    width: 61
    height: 42

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
        id: rectangle887
        anchors.verticalCenter: parent.verticalCenter
        source: "images/Rectangle 887.png"
        anchors.verticalCenterOffset: 3
        anchors.horizontalCenterOffset: 0
        anchors.horizontalCenter: parent.horizontalCenter
        fillMode: Image.PreserveAspectFit

        Image {
            id: dell
            x: 31
            y: 21
            source: "images/Dell.png"
            fillMode: Image.PreserveAspectFit
        }
    }

    Image {
        id: rectangle888
        x: -1
        y: -2
        visible: false
        source: "images/Rectangle 888.png"
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
                target: rectangle888
                visible: true
                rotation: -180
            }
        }
    ]
}
