import QtQuick 2.15
import QtQuick.Layouts 1.15
import QtQuick.Controls 2.15
import Vister 1.0

Item {
    id: item1
    width: Constants.width
    height: Constants.height


    Screen01 {
        id: screen01
        x: 0
        y: 0

        MouseArea {
            id: home_area
            x: 0
            y: 295
            width: 100
            height: 78
            Connections {
                onClicked: item1.state = 'home'
            }
        }
        MouseArea {
            id: setup_area
            x: 0
            y: 412
            width: 100
            height: 78
            Connections {
                onClicked: item1.state = 'setup'
            }
        }
        MouseArea {
            id: run_area
            x: 0
            y: 521
            width: 100
            height: 78
            Connections {
                onClicked: item1.state = 'run'
            }
        }
        MouseArea {
            id: result_area
            x: 0
            y: 632
            width: 100
            height: 78
            Connections {
                onClicked: item1.state = 'result'
            }
        }
    }

    states: [
        State {
            name: "home"

            PropertyChanges {
                target: stackLayout
                currentIndex: 3
            }

            PropertyChanges {
                target: hOME_VIEW
                x: 0
                y: -1080
            }
        },
        State {
            name: "setup"

            PropertyChanges {
                target: stage_indicator
                x: 0
                y: 399
            }

            PropertyChanges {
                target: stackLayout
                y: 0
                anchors.rightMargin: 0
                anchors.bottomMargin: 1080
                anchors.leftMargin: 0
                currentIndex: 2
            }
        },
        State {
            name: "run"

            PropertyChanges {
                target: stage_indicator
                x: 0
                y: 506
            }

            PropertyChanges {
                target: stackLayout
                currentIndex: 1
            }

            PropertyChanges {
                target: tESTING_VIEWS
                x: 0
                y: -1080
            }
        },
        State {
            name: "result"

            PropertyChanges {
                target: stage_indicator
                x: 0
                y: 621
            }

            PropertyChanges {
                target: stackLayout
                currentIndex: 0
            }

            PropertyChanges {
                target: rESULT_VIEW
                x: 0
                y: -1080
            }
        }
    ]
    StackLayout {
        id: stackLayout
        width: 100
        anchors.top: tabBar.bottom
        anchors.right: parent.right
        anchors.left: parent.left
        anchors.bottom: parent.bottom
        currentIndex: 3

        Item {

            RESULT_VIEW {
                id: rESULT_VIEW
            }
        }

        Item {

            TESTING_VIEWS {
                id: tESTING_VIEWS
                x: -8
                y: 14
            }
        }

        Item {

            SETUP_VIEWS {
                id: sETUP_VIEWS
                x: 0
                y: 0
            }
        }

        Item {

            HOME_VIEW {
                id: hOME_VIEW
                x: 0
                y: -1080
            }
        }
    }

    Image {
        id: stage_indicator
        x: 0
        y: 283
        source: "images/Group 1746.png"
        fillMode: Image.PreserveAspectFit
    }
}

/*##^##
Designer {
    D{i:0;formeditorZoom:0.33}
}
##^##*/

