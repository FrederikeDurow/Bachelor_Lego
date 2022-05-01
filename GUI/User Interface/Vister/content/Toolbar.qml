import QtQuick 2.15
import QtQuick.Controls 2.15

Item {
    width: 940
    height: 80

    Image {
        id: rectangle317
        x: -17
        y: -15
        source: "../../Components/Setup_views/Rectangle 317.png"
        fillMode: Image.PreserveAspectFit
    }

    Image {
        id: gps_fixed_light
        x: 556
        y: 12
        source: "../../Components/Setup_views/Gps_fixed_light.png"
        fillMode: Image.PreserveAspectFit
    }

    Image {
        id: img_box_light
        x: 468
        y: 11
        source: "../../Components/Setup_views/Img_box_light.png"
        fillMode: Image.PreserveAspectFit
    }

    Image {
        id: move_alt_alt
        x: 98
        y: 16
        source: "../../Components/Setup_views/Move_alt_alt.png"
        fillMode: Image.PreserveAspectFit
    }

    Image {
        id: search_alt_light
        x: 179
        y: 14
        source: "../../Components/Setup_views/Search_alt_light.png"
        fillMode: Image.PreserveAspectFit
    }

    Image {
        id: arrow_top_long_light
        x: 18
        y: 15
        source: "../../Components/Setup_views/Arrow_top_long_light.png"
        fillMode: Image.PreserveAspectFit
    }

    ToolButton {
        id: toolButton
        x: 234
        y: -150
        text: qsTr("Tool Button")
        checkable: false
        flat: false
    }
}

/*##^##
Designer {
    D{i:0;formeditorZoom:0.9}
}
##^##*/
