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
                x: -19
                y: -16
                source: "../../Components/Setup_views/Rectangle 317.png"
                fillMode: Image.PreserveAspectFit
            }

            ToolButton {
                id: toolButton
                x: 16
                y: -3
                width: 69
                height: 88
                text: qsTr("")
                display: AbstractButton.IconOnly

                Image {
                    id: arrow_top_long_light
                    x: 5
                    y: 11
                    source: "../../Components/Setup_views/Arrow_top_long_light.png"
                    fillMode: Image.PreserveAspectFit
                }
            }

            ToolSeparator {
                id: toolSeparator
                x: 101
                y: 24
            }

            ToolButton {
                id: toolButton1
                x: 127
                y: -3
                width: 69
                height: 88
                text: qsTr("")

                Image {
                    id: move_alt_alt
                    x: 6
                    y: 14
                    source: "../../Components/Setup_views/Move_alt_alt.png"
                    fillMode: Image.PreserveAspectFit
                }
                display: AbstractButton.IconOnly
            }

            ToolSeparator {
                id: toolSeparator1
                x: 212
                y: 24
            }

            ToolButton {
                id: toolButton2
                x: 239
                y: -3
                width: 69
                height: 88
                visible: true
                text: qsTr("")
                autoExclusive: false
                flat: false
                display: AbstractButton.IconOnly

                Image {
                    id: search_alt_light
                    x: 10
                    y: 15
                    source: "../../Components/Setup_views/Search_alt_light.png"
                    fillMode: Image.PreserveAspectFit
                }
            }

            ToolSeparator {
                id: toolSeparator2
                x: 709
                y: 24
            }

            ToolButton {
                id: toolButton3
                x: 736
                y: -3
                width: 69
                height: 88
                text: qsTr("")
                display: AbstractButton.IconOnly

                Image {
                    id: img_box_light
                    x: 6
                    y: 12
                    source: "../../Components/Setup_views/Img_box_light.png"
                    fillMode: Image.PreserveAspectFit
                }
            }

            ToolSeparator {
                id: toolSeparator3
                x: 820
                y: 24
            }


            ToolButton {
                id: toolButton4
                x: 847
                y: -3
                width: 69
                height: 88
                text: qsTr("")
                display: AbstractButton.IconOnly

                Image {
                    id: gps_fixed_light
                    x: 7
                    y: 13
                    source: "../../Components/Setup_views/Gps_fixed_light.png"
                    fillMode: Image.PreserveAspectFit
                }
            }


        }
    }

    Image {
        id: rectangle270
        x: 118
        y: 229
        source: "../../Components/Setup_views/Rectangle 270.png"
        fillMode: Image.PreserveAspectFit

        BoundingBox_element {
            id: boundingBox_element
            x: 18
            y: 14
        }

        TrackingPoint {
            id: trackingPoint
            x: 18
            y: 65
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
}

/*##^##
Designer {
    D{i:0;formeditorZoom:0.66}D{i:12}D{i:14}
}
##^##*/
