import QtQuick 2.15
import QtQuick.Controls 2.15

import QtQuick.Layouts 1.15
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
    }
    Image {
        id: rectangle960
        x: -12
        y: 187
        source: "images/Rectangle 960.png"
        fillMode: Image.PreserveAspectFit
    }

    Text {
        id: text2
        x: 21
        y: 146
        color: "#bccbe0"
        text: qsTr("Select between the following testing types")
        font.pixelSize: 20
    }

    Continue_TestingType_button {
        id: continue_TestingType_button
        x: 709
        y: 731
    }

    Close_popup {
        id: close_popup
        x: 1071
        y: -6
        enabled: true

        Connections {
            target: close_popup
            onClicked: selectTestingType_item.state ="Unckecked"
        }
    }

    Select_type_scrollbar {
        id: select_type_scrollbar
        x: 603
        y: 200
    }

    Project_name_input {
        id: project_name_input
        x: 714
        y: 648
    }

    Text {
        id: text3
        x: 728
        y: 642
        color: "#ffffff"
        text: qsTr("Project Name")
        font.pixelSize: 10
        font.family: "Arial"
    }

    Testing_Types_Grid {
        id: testing_Types_Grid
        x: 60
        y: 238
        clip: true
    }

    Text {
        id: text1
        x: 21
        y: 69
        color: "#ffffff"
        text: qsTr("Select Testing Type")
        font.pixelSize: 60
    }

    Text {
        id: selectedType
        text: "fgge"
        x: 672
        y: 214
        color: "#ffffff"
        font.pixelSize: 40
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
    D{i:0;formeditorZoom:0.5}
}
##^##*/
