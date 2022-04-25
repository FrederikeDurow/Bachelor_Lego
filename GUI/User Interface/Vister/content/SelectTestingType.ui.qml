import QtQuick 2.15
import QtQuick.Layouts 1.15
import QtQuick.Controls 2.15
import Vister 1.0

Item {
    id: selectTestingType_item
    width: 1125
    height: 815

    Image {
        id: path2838
        x: -62
        y: -36
        source: "../../Components/Select_type_section/Path 2838.png"
        fillMode: Image.PreserveAspectFit

        Image {
            id: rectangle960
            x: 74
            y: 207
            source: "images/Rectangle 960.png"
            fillMode: Image.PreserveAspectFit
        }

        Text {
            id: text2
            x: 107
            y: 166
            color: "#bccbe0"
            text: qsTr("Select between the following testing types")
            font.pixelSize: 20
        }

        Continue_TestingType_button {
            id: continue_TestingType_button
            x: 768
            y: 757
        }

        Close_popup {
            id: close_popup
            x: 1132
            y: 30
            enabled: true
            Connections {
                onClicked: selectTestingType_item.state = 'Unchecked'
            }
        }

        Select_type_scrollbar {
            id: select_type_scrollbar
            x: 689
            y: 220
        }

        Project_name_input {
            id: project_name_input
            x: 773
            y: 674
        }

        Text {
            id: text3
            x: 787
            y: 668
            color: "#ffffff"
            text: qsTr("Project Name")
            font.pixelSize: 10
            font.family: "Arial"
        }

        Testing_Types_Grid {
            id: testing_Types_Grid
            x: 146
            y: 258
            anchors.top: select_type_scrollbar.value
            contentItem.objectName: selectTestingType_item.text
        }

        Text {
            id: text1
            x: 107
            y: 89
            color: "#ffffff"
            text: qsTr("Select Testing Type")
            font.pixelSize: 60
        }

        Text {
            id: selectedType
            x: 768
            y: 231
            color: "#ffffff"
            font.pixelSize: 40
        }
    }
    states: [
        State {
            name: "Normal"
            when: selectTestingType_item.enabled

            PropertyChanges {
                target: selectTestingType_item
                visible: true
                enabled: true
            }
        },
        State {
            name: "Unchecked"
            when: !selectTestingType_item.enabled

            PropertyChanges {
                target: selectTestingType_item
                visible: false
                enabled: false
            }
        }
    ]
}

/*##^##
Designer {
    D{i:0;formeditorZoom:0.75}D{i:12}
}
##^##*/

