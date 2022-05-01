import QtQuick 2.15
import QtQuick.Controls 2.15

Item {
    width: 610
    height: 300

    Image {
        id: download
        x: -24
        y: -17
        source: "../../Components/Testing_view/Universal Robot/download.png"
        fillMode: Image.PreserveAspectFit

        UR_input_line {
            id: uR_input_line
            x: 70
            y: 266
            textInputText: "UR_data.csv"
        }

        Text {
            id: text1
            x: 70
            y: 256
            color: "#ffffff"
            text: qsTr("Name of ouput file")
            font.pixelSize: 10
            font.family: "Roboto"
        }

        Grid {
            id: grid
            x: 70
            y: 74
            width: 490
            height: 177
            spacing: -15
            columns: 3
            rows: 2


            Image {
                id: small
                source: "../../Components/Testing_view/Universal Robot/Small.png"
                fillMode: Image.PreserveAspectFit
            }

            Image {
                id: small1
                source: "../../Components/Testing_view/Universal Robot/Small.png"
                fillMode: Image.PreserveAspectFit

                UR_checkbox {
                    id: uR_checkbox10
                    x: 138
                    y: 35
                    checkState: Qt.Unchecked
                }

                UR_checkbox {
                    id: uR_checkbox11
                    x: -23
                    y: 35
                    checkState: Qt.Unchecked
                }
            }
            Image {
                id: small2
                source: "../../Components/Testing_view/Universal Robot/Small.png"
                fillMode: Image.PreserveAspectFit

                UR_checkbox {
                    id: uR_checkbox9
                    x: 137
                    y: 35
                    checkState: Qt.Unchecked
                }
            }

            Image {
                id: big
                source: "../../Components/Testing_view/Universal Robot/Big.png"
                fillMode: Image.PreserveAspectFit

                UR_checkbox {
                    id: uR_checkbox6
                    x: 138
                    y: 31
                    checkState: Qt.Unchecked
                }

                UR_checkbox {
                    id: uR_checkbox7
                    x: 138
                    y: 54
                    checkState: Qt.Unchecked
                }

                UR_checkbox {
                    id: uR_checkbox8
                    x: 138
                    y: 76
                    checkState: Qt.Unchecked
                }
            }

            Image {
                id: big1
                source: "../../Components/Testing_view/Universal Robot/Big.png"
                fillMode: Image.PreserveAspectFit

                UR_checkbox {
                    id: uR_checkbox3
                    x: 138
                    y: 31
                    checkState: Qt.Unchecked
                }

                UR_checkbox {
                    id: uR_checkbox4
                    x: 138
                    y: 54
                    checkState: Qt.Unchecked
                }

                UR_checkbox {
                    id: uR_checkbox5
                    x: 138
                    y: 76
                    checkState: Qt.Unchecked
                }
            }

            Image {
                id: big2
                source: "../../Components/Testing_view/Universal Robot/Big.png"
                fillMode: Image.PreserveAspectFit

                UR_checkbox {
                    id: uR_checkbox
                    x: 136
                    y: 31
                    checkState: Qt.Unchecked
                }

                UR_checkbox {
                    id: uR_checkbox1
                    x: 136
                    y: 54
                    checkState: Qt.Unchecked
                }

                UR_checkbox {
                    id: uR_checkbox2
                    x: 136
                    y: 76
                    checkState: Qt.Unchecked
                }
            }

        }

        TestScript_button {
            id: testScript_button
            x: 499
            y: 266
        }
    }

    Text {
        id: text2
        x: 83
        y: 89
        color: "#ffffff"
        text: qsTr("Timestamp")
        font.pixelSize: 10
        font.family: "Roboto"
    }

    Text {
        id: text3
        x: 245
        y: 89
        color: "#ffffff"
        text: qsTr("Frequency")
        font.pixelSize: 10
        font.family: "Roboto"
    }

    Text {
        id: text4
        x: 83
        y: 151
        color: "#ffffff"
        text: qsTr("TCP-Force")
        font.pixelSize: 10
        font.family: "Roboto"
    }

    Text {
        id: text5
        x: 83
        y: 173
        color: "#ffffff"
        text: qsTr("TCP-Position")
        font.pixelSize: 10
        font.family: "Roboto"
    }

    Text {
        id: text6
        x: 83
        y: 194
        color: "#ffffff"
        text: qsTr("TCP-Speed")
        font.pixelSize: 10
        font.family: "Roboto"
    }

    Text {
        id: text7
        x: 398
        y: 89
        color: "#ffffff"
        text: qsTr("Digital Outputs")
        font.pixelSize: 10
        font.family: "Roboto"
    }

    Text {
        id: text8
        x: 245
        y: 151
        color: "#ffffff"
        text: qsTr("Target TCP-Force")
        font.pixelSize: 10
        font.family: "Roboto"
    }

    Text {
        id: text9
        x: 245
        y: 173
        color: "#ffffff"
        text: qsTr("Target TCP-Position")
        font.pixelSize: 10
        font.family: "Roboto"
    }

    Text {
        id: text10
        x: 245
        y: 194
        color: "#ffffff"
        text: qsTr("Target TCP-Speed")
        font.pixelSize: 10
        font.family: "Roboto"
    }

    Text {
        id: text11
        x: 389
        y: 151
        color: "#ffffff"
        text: qsTr("Actual joint positions")
        font.pixelSize: 10
        font.family: "Roboto"
    }

    Text {
        id: text12
        x: 390
        y: 173
        color: "#ffffff"
        text: qsTr("Actual joint velocities")
        font.pixelSize: 10
        font.family: "Roboto"
    }

    Text {
        id: text13
        x: 390
        y: 194
        color: "#ffffff"
        text: qsTr("Actual joint accelerations")
        font.pixelSize: 10
        font.family: "Roboto"
    }

    Text {
        id: text14
        x: 8
        y: 0
        color: "#ffffff"
        text: qsTr("Data to be extracted from the UR")
        font.pixelSize: 30
        font.family: "Roboto"
    }

    Text {
        id: text15
        x: 13
        y: 37
        color: "#ffffff"
        text: qsTr("Check the boxes of the data you wishes to be extracted during the test")
        font.pixelSize: 12
        font.family: "Roboto"
    }
}

/*##^##
Designer {
    D{i:0;formeditorZoom:1.33}D{i:8}D{i:6}D{i:10}D{i:9}D{i:15}D{i:22}D{i:19}D{i:24}D{i:25}
D{i:26}D{i:27}D{i:28}
}
##^##*/
