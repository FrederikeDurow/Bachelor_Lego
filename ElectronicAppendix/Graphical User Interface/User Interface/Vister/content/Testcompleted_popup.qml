import QtQuick 2.15
import QtQuick.Controls 2.15

Item {
    width: 690
    height: 290

    Image {
        id: rectangle875
        x: -34
        y: -34
        source: "../../Components/Testing_view/Universal Robot/Rectangle 875.png"
        fillMode: Image.PreserveAspectFit

        Continue_button {
            id: continue_button
            x: 34
            y: 285
        }
    }

    Image {
        id: done_ring_round_fill
        x: 152
        y: 102
        width: 44
        height: 44
        source: "../../Components/Testing_view/Universal Robot/Done_ring_round_fill.png"
        fillMode: Image.PreserveAspectFit
    }

    Image {
        id: succesfullycompletedthetest
        x: 216
        y: 92
        source: "../../Components/Testing_view/Universal Robot/Succesfully completed the test.Press continue to see the results.png"
        fillMode: Image.PreserveAspectFit
    }
}

/*##^##
Designer {
    D{i:0;formeditorZoom:1.1}
}
##^##*/
