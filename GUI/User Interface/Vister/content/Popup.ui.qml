

/*
This is a UI file (.ui.qml) that is intended to be edited in Qt Design Studio only.
It is supposed to be strictly declarative and only uses a subset of QML. If you edit
this file manually, you might introduce QML code that is not supported by Qt Design Studio.
Check out https://doc.qt.io/qtcreator/creator-quick-ui-forms.html for details on .ui.qml files.
*/
import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Layouts 1.0
import QtQuick.Studio.EventSystem 1.0

Item {
    id: item1
    width: 760
    height: 362
    enabled: true
    focus: true

    Image {
        id: rectangle886
        x: 0
        y: 0
        visible: true
        source: "images/Rectangle 886.png"
        fillMode: Image.PreserveAspectFit

        RowLayout {
            anchors.verticalCenter: parent.verticalCenter
            anchors.horizontalCenter: parent.horizontalCenter

            Image {
                id: info_fill
                source: "images/Info_fill.png"
                fillMode: Image.PreserveAspectFit
            }

            Text {
                id: text1
                color: "#ffffff"
                text: qsTr("This feature has not been implemented yet")
                font.pixelSize: 25
                Layout.leftMargin: 11
                font.family: "Arial"
            }
        }

        Close_popup {
            id: close_popup
            x: 668
            y: 29
            enabled: true
            Connections {
                onClicked: item1.state = 'Unchecked'
            }
        }

        Continue_button {
            id: continue_button
            x: 34
            y: 285
            enabled: true
            Connections {
                onClicked: item1.state = 'Unchecked'
            }
        }
    }

    states: [
        State {
            name: "Normal"
            when: item1.enabled

            PropertyChanges {
                target: item1
                visible: true
                enabled: true
            }
        },
        State {
            name: "Unchecked"
            when: !item1.enabled

            PropertyChanges {
                target: item1
                visible: false
                enabled: false
            }
        }
    ]
}

/*##^##
Designer {
    D{i:0;formeditorZoom:1.25;height:362;width:760}
}
##^##*/

