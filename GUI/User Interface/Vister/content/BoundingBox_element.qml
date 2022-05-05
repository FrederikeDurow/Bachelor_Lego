import QtQuick 2.15
import QtQuick.Controls 2.15

Item {
    id: instance_bounding_box
    width: 400
    height: 45
    property alias text1Text: text1.text

    Image {
        id: rectangle678
        x: -3
        y: -1
        source: "../../Components/Setup_views/Rectangle 678.png"
        fillMode: Image.PreserveAspectFit

        Delete_btn {
            id: delete_btn
            x: 365
            y: 3
        }
    }

    Text {
        id: text1
        x: 90
        y: 13
        color: "#ffffff"
        text: qsTr("Object (1)")
        font.pixelSize: 14
        font.family: "Roboto"
    }

    Image {
        id: img_box_light2
        x: 50
        y: 5
        source: "../../Components/Setup_views/Img_box_light2.png"
        fillMode: Image.PreserveAspectFit
    }

    Eye_btn {
        id: eye_btn
        x: 1
        y: 4
    }

    Image {
        id: rectangle731
        x: 0
        y: 0
        visible: false
        source: "../../Components/Setup_views/Rectangle 731.png"
        fillMode: Image.PreserveAspectFit
    }
    states: [
        State {
            name: "Unselected"
        },
        State {
            name: "Selected"

            PropertyChanges {
                target: rectangle731
                visible: true
            }
        }
    ]
}

/*##^##
Designer {
    D{i:0;height:45;width:400}
}
##^##*/
