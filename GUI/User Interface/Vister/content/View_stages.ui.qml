import QtQuick 2.15
import QtQuick.Layouts 1.15
import QtQuick.Controls 2.15
import Vister 1.0

Item {
    width: Constants.width
    height: Constants.height

    StackLayout {
        id: stackLayout
        width: 100
        anchors.top: tabBar.bottom
        anchors.right: parent.right
        anchors.left: parent.left
        anchors.bottom: parent.bottom
        currentIndex: 0

        Item {
            Label {
                text: qsTr("Page 01")
                anchors.centerIn: parent
                font: Constants.largeFont
            }

            RESULT_VIEW {
                id: rESULT_VIEW
            }
        }

        Item {
            Label {
                text: qsTr("Page 02")
                anchors.centerIn: parent
                font: Constants.largeFont
            }

            TESTING_VIEWS {
                id: tESTING_VIEWS
                x: -8
                y: 14
            }
        }

        Item {
            Label {
                text: qsTr("Page 02")
                anchors.centerIn: parent
                font: Constants.largeFont
            }

            SETUP_VIEWS {
                id: sETUP_VIEWS
                x: 0
                y: 0
            }
        }

        Item {
            Label {
                text: qsTr("Page 03")
                styleColor: "#ffffff"
                anchors.verticalCenterOffset: 486
                anchors.horizontalCenterOffset: 926
                anchors.centerIn: parent
                font: Constants.largeFont
            }

            HOME_VIEW {
                id: hOME_VIEW
                x: 0
                y: 0
            }
        }
    }

    Screen01 {
        id: screen01
        x: 0
        y: 0

        Image {
            id: stage_indicator
            x: 0
            y: 283
            source: "images/Group 1746.png"
            fillMode: Image.PreserveAspectFit
        }
    }
}

/*##^##
Designer {
    D{i:0;formeditorZoom:0.33}
}
##^##*/

