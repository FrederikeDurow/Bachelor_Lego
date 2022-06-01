import QtQuick 2.15
import QtQuick.Controls 2.15

Item {
    id: item1
    width: 690
    height: 300

    Image {
        id: rectangle875
        x: -32
        y: -29
        source: "../../Components/Testing_view/Universal Robot/Rectangle 875.png"
        fillMode: Image.PreserveAspectFit

        Close_popup {
            id: close_popup
            x: 667
            y: 30
            enabled: true
            Connections {
            onClicked: selectTestingType_item.state = 'Unchecked'
            }
        }

        Continue_button {
            id: continue_button
            x: 34
            y: 285
            enabled: true
            Connections {
            onClicked: selectTestingType_item.state = 'Unchecked'
            }
        }
    }

    Image {
        id: connectiontotheURhasnotbeenestablished
        x: 185
        y: 104
        source: "../../Components/Testing_view/Universal Robot/Connection to the UR has not beenestablished. Please connect beforerunning the test.png"
        fillMode: Image.PreserveAspectFit
    }

    Image {
        id: info_fill
        x: 111
        y: 126
        source: "../../Components/Testing_view/Universal Robot/Info_fill.png"
        fillMode: Image.PreserveAspectFit
    }
    states: [
        State {
            name: "Normal"
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
    D{i:0;formeditorZoom:1.1}
}
##^##*/
