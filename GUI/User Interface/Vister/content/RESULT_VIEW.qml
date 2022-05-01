import QtQuick 2.15
import QtQuick.Controls 2.15

Item {
    width: 1920
    height: 1080

    Image {
        id: result_section
        x: 106
        y: 38
        source: "../../Components/Result_section/Result_section.png"
        fillMode: Image.PreserveAspectFit

        Rectangle {
            id: rectangle
            x: 0
            y: 0
            width: 1792
            height: 1040
            opacity: 0.504
            color: "#000000"
        }
    }


}

/*##^##
Designer {
    D{i:0;formeditorZoom:0.5}
}
##^##*/
