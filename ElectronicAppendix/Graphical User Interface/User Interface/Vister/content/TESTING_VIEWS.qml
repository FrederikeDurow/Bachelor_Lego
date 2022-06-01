import QtQuick 2.15
import QtQuick.Controls 2.15

Item {
    id: item1
    width: 1920
    height: 1080


        Progressbar {
            id: progressbar
            x: 120
            y: 952
            timelineCurrentFrame: 1
        }

    states: [
        State {
            name: "Activation_Test_state"
        },
        State {
            name: "Motion_Traking_Test_state"

        }
    ]
    Play_button {
        id: play_button
        x: 1655
        y: 960
    }

    Stop_button {
        id: stop_button
        x: 1521
        y: 961
    }

    Settings_button {
        id: settings_button
        x: 1379
        y: 960
    }

    Universial_btn {
        id: universial_btn
        x: 124
        y: 50
    }

    Testcompleted_popup {
        id: testcompleted_popup
        x: 1952
        y: 436
    }

    UR_popup {
        id: uR_popup
        x: 1952
        y: 772
    }

    Frame {
        id: frame
        x: 765
        y: 50
        width: 1120
        height: 597
    }
    UR_data_extract {
        id: uR_data_extract
        x: -632
        y: 0
    }

    Image {
        id: rectangle332
        x: 1233
        y: 648
        source: "../../Components/Testing_view/Rectangle 332.png"
        fillMode: Image.PreserveAspectFit
    }

    Image {
        id: rectangle372
        x: 106
        y: 360
        source: "../../Components/Testing_view/Rectangle 372.png"
        fillMode: Image.PreserveAspectFit

        Small_input_line {
            id: small_input_line
            x: 70
            y: 62
        }
    }

    Image {
        id: rectangle437
        x: 107
        y: 500
        source: "../../Components/Testing_view/Rectangle 437.png"
        fillMode: Image.PreserveAspectFit

        Toggle {
            id: toggle
            x: 98
            y: 344
            controlChecked: true
        }

        Toggle {
            id: toggle1
            x: 495
            y: 93
        }

        Toggle {
            id: toggle2
            x: 383
            y: 93
        }

        Toggle {
            id: toggle3
            x: 273
            y: 93
            controlChecked: true
        }

        Toggle {
            id: toggle4
            x: 250
            y: 344
            controlChecked: true
        }

        Text {
            id: text9
            x: 345
            y: 823
            color: "#ffffff"
            text: qsTr("Record Malfunctions")
            font.pixelSize: 12
        }
    }

    Image {
        id: rectangle946
        x: 332
        y: 360
        source: "../../Components/Testing_view/Rectangle 946.png"
        fillMode: Image.PreserveAspectFit
    }

    Image {
        id: rectangle371
        x: 748
        y: 648
        source: "../../Components/Testing_view/Rectangle 371.png"
        fillMode: Image.PreserveAspectFit
    }

    Small_input_line {
        id: small_input_line1
        x: 400
        y: 422
        textInputText: "1"
    }

    Image {
        id: line51
        x: 151
        y: 553
        source: "../../Components/Testing_view/Line 51.png"
        fillMode: Image.PreserveAspectFit
    }

    Image {
        id: line52
        x: 151
        y: 639
        source: "../../Components/Testing_view/Line 51.png"
        fillMode: Image.PreserveAspectFit
    }

    Image {
        id: line53
        x: 151
        y: 714
        source: "../../Components/Testing_view/Line 51.png"
        fillMode: Image.PreserveAspectFit
    }

    Image {
        id: line54
        x: 151
        y: 800
        source: "../../Components/Testing_view/Line 51.png"
        fillMode: Image.PreserveAspectFit
    }

    Image {
        id: line48
        x: 469
        y: 815
        source: "../../Components/Testing_view/Line 48.png"
        fillMode: Image.PreserveAspectFit
    }

    Small_input_line {
        id: small_input_line2
        x: 590
        y: 422
        textInputText: "MPG4"
    }

    Text {
        id: text1
        x: 163
        y: 544
        color: "#ffffff"
        text: qsTr("Bounding Box Elements")
        font.pixelSize: 10
    }

    Text {
        id: pos_lap_txt
        x: 390
        y: 570
        color: "#ffffff"
        text: qsTr("Positions")
        font.pixelSize: 12
    }

    Text {
        id: text3
        x: 508
        y: 570
        color: "#ffffff"
        text: qsTr("Areal")
        font.pixelSize: 12
    }

    Text {
        id: text4
        x: 185
        y: 815
        color: "#ffffff"
        text: qsTr("Record Malfunctions")
        font.pixelSize: 12
    }

    Text {
        id: text5
        x: 607
        y: 570
        color: "#ffffff"
        text: qsTr("Differencies")
        font.pixelSize: 12
    }

    Text {
        id: text6
        x: 182
        y: 410
        color: "#ffffff"
        text: qsTr("Number of laps")
        font.pixelSize: 10
    }

    Text {
        id: text7
        x: 405
        y: 410
        color: "#ffffff"
        text: qsTr("Record every (*) laps")
        font.pixelSize: 10
    }

    Text {
        id: text8
        x: 597
        y: 410
        color: "#ffffff"
        text: qsTr("Video file format")
        font.pixelSize: 10
    }

    Text {
        id: text10
        x: 338
        y: 815
        color: "#ffffff"
        text: qsTr("Record Whole Video")
        font.pixelSize: 12
    }





}



/*##^##
Designer {
    D{i:0;formeditorZoom:1.33}D{i:39}
}
##^##*/
