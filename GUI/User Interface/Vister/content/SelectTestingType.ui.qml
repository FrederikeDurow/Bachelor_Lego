import QtQuick 2.15
import QtQuick.Layouts 1.15
import QtQuick.Controls 2.15
import Vister 1.0

Pane {
    width: 1125
    height: 815

    Image {
        id: path2838
        x: -62
        y: -42
        source: "../../Components/Select_type_section/Path 2838.png"
        fillMode: Image.PreserveAspectFit

        Text {
            id: text1
            x: 107
            y: 89
            color: "#ffffff"
            text: qsTr("Select Testing Type")
            font.pixelSize: 60
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
            y: 770
        }
    }
}

/*##^##
Designer {
    D{i:0;formeditorZoom:0.75}D{i:3}
}
##^##*/
