import QtQuick 2.15
import QtQuick.Controls 2.15

Item {
    width: 1920
    height: 1080

    Screen01 {
        id: screen01
        x: 0
        y: 0
    }

    Frame {
        id: frame
        x: 577
        y: 44
        width: 1313
        height: 687

        MouseArea {
            id: draw_area
            anchors.fill: parent
        }
    }

    Play_button {
        id: play_button
        x: 1660
        y: 744
    }

    Settings_button {
        id: settings_button
        x: 1529
        y: 744
    }



    Image {
        id: rectangle332
        x: 561
        y: 834
        source: "../../Components/Setup_views/Rectangle 332.png"
        fillMode: Image.PreserveAspectFit
    }

    Image {
        id: rectangle317
        x: 561
        y: 729
        source: "../../Components/Setup_views/Rectangle 317.png"
        fillMode: Image.PreserveAspectFit

        ToolBar {
            id: toolBar
            x: 19
            y: 16
            width: 935
            height: 82

            Image {
                id: rectangle3171
                x: -25
                y: -16
                source: "../../Components/Setup_views/Rectangle 317.png"
                fillMode: Image.PreserveAspectFit
            }

            ToolButton {
                id: toolButton
                x: -9
                y: -3
                width: 110
                height: 88
                text: qsTr("")
                display: AbstractButton.IconOnly

                Image {
                    id: arrow_top_long_light
                    x: 24
                    y: 14
                    source: "../../Components/Setup_views/Arrow_top_long_light.png"
                    fillMode: Image.PreserveAspectFit
                }
            }

            ToolSeparator {
                id: toolSeparator
                x: 95
                y: 24
                width: 14
                height: 36
            }

            ToolButton {
                Image {
                    id: move_alt_alt
                    x: 27
                    y: 16
                    source: "../../Components/Setup_views/Move_alt_alt.png"
                    fillMode: Image.PreserveAspectFit
                }
                id: toolButton1
                x: 103
                y: -3
                width: 110
                height: 88
                text: qsTr("")
                flat: true


                display: AbstractButton.IconOnly
            }

            ToolSeparator {
                id: toolSeparator1
                x: 207
                y: 24
                width: 14
                height: 36
            }

            ToolButton {
                id: toolButton2
                x: 215
                y: -3
                width: 110
                height: 88
                visible: true
                text: qsTr("")
                autoExclusive: false
                flat: false
                display: AbstractButton.IconOnly


                Image {
                    id: search_alt_light
                    x: 29
                    y: 18
                    source: "../../Components/Setup_views/Search_alt_light.png"
                    fillMode: Image.PreserveAspectFit
                }
            }

            ToolSeparator {
                id: toolSeparator2
                x: 702
                y: 24
                width: 14
                height: 36
            }

            ToolButton {
                id: toolButton3
                x: 709
                y: -3
                width: 110
                height: 88
                text: qsTr("")
                display: AbstractButton.IconOnly

                Image {
                    id: img_box_light
                    x: 26
                    y: 15
                    source: "../../Components/Setup_views/Img_box_light.png"
                    fillMode: Image.PreserveAspectFit
                }
            }

            ToolSeparator {
                id: toolSeparator3
                x: 813
                y: 24
                width: 14
                height: 36
            }


            ToolButton {
                id: toolButton4
                x: 821
                y: -3
                width: 110
                height: 88
                text: qsTr("")
                display: AbstractButton.IconOnly

                Image {
                    id: gps_fixed_light
                    x: 27
                    y: 16
                    source: "../../Components/Setup_views/Gps_fixed_light.png"
                    fillMode: Image.PreserveAspectFit
                }
            }


        }
    }






    Image {
        id: rectangle423
        x: 118
        y: 90
        source: "../../Components/Setup_views/Rectangle 423.png"
        fillMode: Image.PreserveAspectFit
    }

    Image {
        id: rectangle330
        x: 118
        y: 31
        source: "../../Components/Setup_views/Rectangle 330.png"
        fillMode: Image.PreserveAspectFit
    }

    Image {
        id: rectangle456
        x: 992
        y: 742
        source: "../../Components/Setup_views/Rectangle 456.png"
        fillMode: Image.PreserveAspectFit
    }








    Image {
        id: gps_fixed_light1
        x: 397
        y: 59
        width: 34
        height: 34
        source: "../../Components/Setup_views/Gps_fixed_light.png"
        fillMode: Image.PreserveAspectFit
    }

    Image {
        id: img_box_light1
        x: 319
        y: 58
        width: 36
        height: 36
        source: "../../Components/Setup_views/Img_box_light.png"
        fillMode: Image.PreserveAspectFit
    }

    Image {
        id: camera_light
        x: 244
        y: 64
        source: "../../Components/Setup_views/Camera_light.png"
        fillMode: Image.PreserveAspectFit
    }
    Image {
        id: group1750
        x: 296
        y: 44
        source: "../../Components/Setup_views/Group 1750.png"
        fillMode: Image.PreserveAspectFit
    }

    Image {
        id: rectangle470
        x: 118
        y: 228
        source: "../../Components/Rectangle 470.png"
        fillMode: Image.PreserveAspectFit
    }

    Image {
        id: rectangle472
        x: 118
        y: 639
        source: "../../Components/Rectangle 470.png"
        fillMode: Image.PreserveAspectFit
    }

    TrackingPoint {
        id: trackingPoint
        x: 137
        y: 652
    }




    ListView {
        id: listView_boundingbox
        x: 134
        y: 242
        width: 405
        height: 399
        clip: true
        cacheBuffer: 80
        delegate: Item{
            x: 5
            width: 80
            height: 40
            Row {
                id: row1
                spacing: 10
                Rectangle {
                    width: 40
                    height: 40
                    color: colorCode
                }

                /*
                Component.onCompleted: {
                         var component = Qt.createComponent("BoundingBox_element.qml");
                         for (var i=0; i<5; i++) {
                             var object = component.createObject(container);
                             object.x = (object.width + 10) * i;
                         }
                     }
                      */

                Text {
                    text: name
                    anchors.verticalCenter: parent.verticalCenter
                    font.bold: true
                }

            }

        }
        model: ListModel {
            ListElement {
                name: "Object 1"
                colorCode: "grey"
            }

            ListElement {
                name: "Object 2"
                colorCode: "red"
            }

            ListElement {
                name: "Object 3"
                colorCode: "blue"
            }

            ListElement {
                name: "Object 4"
                colorCode: "green"
            }
        }

        BoundingBox_element {
            id: boundingBox_element
            x: 538
            y: 71
        }
    }
}



/*##^##
Designer {
    D{i:0;formeditorZoom:0.9}D{i:31}
}
##^##*/
