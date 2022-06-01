import QtQuick 2.15
import QtQuick.Controls 2.15

Item {
    width: 338
    height: 33

    Image {
        id: rectangle983
        x: -19
        y: -13
        source: "images/Rectangle 983.png"
        fillMode: Image.PreserveAspectFit

        TextInput {
            id: textInput
            x: 48
            y: 24
            width: 273
            height: 14
            color: "#ffffff"
            text: qsTr("Please type project name here")
            font.pixelSize: 12
            maximumLength: 40
            font.family: "Arial"
        }
    }
}

/*##^##
Designer {
    D{i:0;height:33;width:338}D{i:2}
}
##^##*/
