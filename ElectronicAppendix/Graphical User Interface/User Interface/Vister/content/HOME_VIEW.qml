import QtQuick 2.15
import QtQuick.Controls 2.15

Item {
    width: 1920
    height: 1080

    Image {
        id: logo_big
        x: 372
        y: 131
        height: 300
        source: "images/LogoRezisedto256x256.svg"
        fillMode: Image.PreserveAspectFit
    }

    Text {
        id: headline_txt
        x: 766
        y: 157
        color: "#ffffff"
        text: qsTr("Welcome To Vister")
        font.pixelSize: 80
        font.family: "Arial"
    }

    Text {
        id: about_txt
        x: 766
        y: 298
        color: "#bccbe0"
        text: qsTr("Vister is a Computer Vision based program that enables you to create various experiment using only a Camera
    and a UR.

    Vistor allows you to extract essential information from the UR robot while in operation simountanous applying
    Computer Vision algorithms to each element to detect how they behave under different circumstances ")
        font.pixelSize: 16
    }

    Update_section {
        id: update_section
        x: 1022
        y: 578
    }

    Loadproject_button {
        id: loadproject_button
        x: 582
        y: 577
        Connections {
            target: loadproject_button
            onClicked: popup.state = 'Normal'
        }
    }

    Createproject_button {
        id: createproject_button
        x: 140
        y: 577
        Connections {
            target: createproject_button
            onClicked: selectTestingType.state = 'Normal'
        }
    }

    SelectTestingType {
        id: selectTestingType
        x: 356
        y: 133
        visible: false
        enabled: false
    }






}

/*##^##
Designer {
    D{i:0;formeditorZoom:0.5}
}
##^##*/
