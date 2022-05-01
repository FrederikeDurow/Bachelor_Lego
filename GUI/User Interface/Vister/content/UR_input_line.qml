import QtQuick 2.15
import QtQuick.Controls 2.15

Item {
    width: 220
    height: 34
    property alias textInputText: textInput.text
    clip: false

    Image {
        id: rectangle899
        x: -21
        y: -14
        source: "../../Components/Testing_view/Universal Robot/Rectangle 899.png"
        fillMode: Image.PreserveAspectFit

        TextInput {
            id: textInput
            x: 25
            y: 19
            width: 213
            height: 25
            color: "#ffffff"
            text: qsTr("Text Input")
            font.pixelSize: 12
            horizontalAlignment: Text.AlignHCenter
            clip: true
            font.family: "Roboto"
        }
    }
}

/*##^##
Designer {
    D{i:0;height:34;width:220}
}
##^##*/
