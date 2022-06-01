import QtQuick 2.15
import QtQuick.Controls 2.15

Item {
    id: item1
    width: 609
    height: 300

    Image {
        id: download
        x: -21
        y: -18
        source: "images/download.png"
        fillMode: Image.PreserveAspectFit

        Close_popup {
            id: close_popup
            x: 575
            y: 15
                enabled: true
                Connections {
                    onClicked: selectTestingType_item.state = 'Unchecked'
                }
        }

        Guide_button {
            id: guide_button
            x: 556
            y: 244
        }

        Connect_button {
            id: connect_button
            x: 360
            y: 66
        }

        UR_input_line {
            id: uR_input_line
            x: 87
            y: 66
            textInputText: "192.9.0.1243"
        }

        UR_input_line {
            id: uR_input_line1
            x: 87
            y: 133
            textInputText: "3004"
        }

        UR_input_line {
            id: uR_input_line2
            x: 87
            y: 192
            textInputText: "home/test/spring"
        }

        Text {
            id: text3
            x: 92
            y: 183
            color: "#ffffff"
            text: qsTr("URP-Script")
            font.pixelSize: 10
        }

        Text {
            id: text4
            x: 92
            y: 124
            color: "#ffffff"
            text: qsTr("Port Number")
            font.pixelSize: 10
        }

        Text {
            id: text5
            x: 92
            y: 56
            color: "#ffffff"
            text: qsTr("IP-Address of the Robot")
            font.pixelSize: 10
        }
    }

    Image {
        id: done_ring_round_fill
        x: 0
        y: 0
        visible: false
        source: "../../Components/Testing_view/Universal Robot/Done_ring_round_fill.png"
        fillMode: Image.PreserveAspectFit
    }

    Image {
        id: dell_fill
        x: 0
        y: 0
        visible: false
        source: "../../Components/Testing_view/Universal Robot/Dell_fill.png"
        fillMode: Image.PreserveAspectFit
    }

    Text {
        id: text2
        x: 298
        y: 253
        visible: false
        text: qsTr("Text")
        font.pixelSize: 12
    }

    Text {
        id: text1
        x: 273
        y: 238
        visible: false
        text: qsTr("Text")
        font.pixelSize: 12
    }
    states: [
        State {
            name: "Normal"

            PropertyChanges {
                target: text1
                visible: false
            }

            PropertyChanges {
                target: text2
                visible: false
            }

            PropertyChanges {
                target: dell_fill
                visible: false
            }

            PropertyChanges {
                target: done_ring_round_fill
                visible: false
            }
        },
        State {
            name: "Connection_suc"

            PropertyChanges {
                target: done_ring_round_fill
                x: 180
                y: 244
                visible: true
            }

            PropertyChanges {
                target: dell_fill
                x: 180
                y: 244
                visible: false
            }

            PropertyChanges {
                target: text2
                x: 241
                y: 271
                visible: true
                color: "#b7c5db"
                text: qsTr("Continues in 3 seconds...")
            }

            PropertyChanges {
                target: text1
                x: 211
                y: 243
                visible: true
                color: "#b2c0d6"
                text: qsTr("Connection Established!")
                font.pixelSize: 20
                font.family: "Roboto"
                clip: true
            }
        },
        State {
            name: "Connection_fail"

            PropertyChanges {
                target: dell_fill
                x: 188
                y: 244
                visible: true
            }

            PropertyChanges {
                target: text2
                x: 224
                y: 242
                visible: true
                color: "#ffffff"
                text: qsTr("Connection Failed!")
                font.pixelSize: 20
            }

            PropertyChanges {
                target: done_ring_round_fill
                x: 188
                y: 244
                visible: false
            }

            PropertyChanges {
                target: text1
                visible: false
            }
        },
        State {
            name: "Unchecked"

            PropertyChanges {
                target: item1
                visible: false
            }
        }
    ]
}

/*##^##
Designer {
    D{i:0;formeditorZoom:1.66}D{i:7}D{i:8}D{i:10}D{i:11}D{i:14}
}
##^##*/
