import QtQuick 2.15
import QtQuick.Controls 2.15

Item {
    id: item1
    width: 400
    height: 40
    property alias text1Text: text1.text

    Image {
        id: rectangle713
        x: -12
        y: -9
        source: "../../Components/Setup_views/Rectangle 713.png"
        fillMode: Image.PreserveAspectFit

        Eye_btn {
            id: eye_btn
            x: 13
            y: 10
        }

        Delete_btn {
            id: delete_btn
            x: 374
            y: 10
        }

        Text {
            id: text1
            x: 106
            y: 19
            color: "#ffffff"
            text: qsTr("Tracking Point (1)")
            font.pixelSize: 14
            font.family: "Roboto"
        }
    }

    Image {
        id: rectangle731
        x: 0
        y: 0
        visible: false
        source: "../../Components/Setup_views/Rectangle 731.png"
        fillMode: Image.PreserveAspectFit
    }

    Image {
        id: gps_fixed_light2
        x: 47
        y: 3
        source: "../../Components/Setup_views/Gps_fixed_light2.png"
        fillMode: Image.PreserveAspectFit
    }
    states: [
        State {
            name: "Selected"

            PropertyChanges {
                target: rectangle731
                visible: true
            }
        },
        State {
            name: "Unselected"
        }
    ]
}

/*##^##
Designer {
    D{i:0;formeditorZoom:2}
}
##^##*/
