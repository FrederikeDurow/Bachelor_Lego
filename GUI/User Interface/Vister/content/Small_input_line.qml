import QtQuick 2.15
import QtQuick.Controls 2.15

Item {
    id: item1
    width: 95
    height: 29
    property alias textInputText: textInput.text

    Image {
        id: rectangle854
        width: 132
        anchors.verticalCenter: parent.verticalCenter
        source: "../../Components/Testing_view/Rectangle 854.png"
        anchors.verticalCenterOffset: 3
        anchors.horizontalCenterOffset: 0
        anchors.horizontalCenter: parent.horizontalCenter
        fillMode: Image.PreserveAspectFit

        TextInput {
            id: textInput
            x: 26
            y: 24
            width: 80
            height: 14
            color: "#ffffff"
            text: qsTr("1000")
            font.pixelSize: 11
            horizontalAlignment: Text.AlignHCenter
            maximumLength: 10
            font.family: "roboto"
        }
    }
}

/*##^##
Designer {
    D{i:0;height:29;width:95}D{i:1}
}
##^##*/
