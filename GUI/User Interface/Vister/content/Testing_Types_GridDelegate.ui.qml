import QtQuick 2.15

Item {
    id: delegate
    width: 140
    height: 140

    Image {
        id: component811
        x: -11
        y: -8
        source: "../../Components/Select_type_section/Component 81 – 1.png"
        fillMode: Image.PreserveAspectFit
    }

    Text {
        id: label
        color: "#ffffff"
        anchors.top: parent.top
        anchors.horizontalCenter: parent.horizontalCenter

        font.family: Constants.largeFont.family
        text: name
        anchors.margins: 24
        font.pointSize: 8
        anchors.horizontalCenterOffset: 0
        anchors.topMargin: 111
    }
    MouseArea {
        id: mouseArea
        anchors.fill: parent
        anchors.rightMargin: 0
        anchors.bottomMargin: 5
        anchors.leftMargin: 0
        anchors.topMargin: 3
        onClicked: delegate.GridView.view.currentIndex = index
    }

    Image {
        id: rectangle962
        x: -1
        y: -1
        width: 141
        height: 142
        visible: false
        source: "../../Components/Select_type_section/Rectangle 962.png"
        fillMode: Image.PreserveAspectFit
    }

    states: [
        State {
            name: "Highlighted"

            when: delegate.GridView.isCurrentItem
            PropertyChanges {
                target: label
                y: -8
                color: "#efefef"
                anchors.horizontalCenterOffset: 0
                anchors.topMargin: 108
            }

            PropertyChanges {
                target: rectangle962
                x: 4
                y: 3
                width: 130
                height: 132
                visible: true
            }

            PropertyChanges {
                target: component811
                x: -11
                y: -8
            }

            PropertyChanges {
                target: mouseArea
                y: -8
            }
        }
    ]
}

/*##^##
Designer {
    D{i:0;formeditorZoom:3}
}
##^##*/
