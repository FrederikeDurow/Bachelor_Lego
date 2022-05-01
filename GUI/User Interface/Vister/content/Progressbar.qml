import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Timeline 1.0

Item {
    width: 1235
    height: 94
    property alias timelineAnimationProperty: timelineAnimation.property
    property alias timelineStartFrame: timeline.startFrame
    property alias timelineEndFrame: timeline.endFrame
    property alias timelineCurrentFrame: timeline.currentFrame



    Image {
        id: rectangle359
        x: -16
        y: 28
        source: "images/Rectangle 359.png"
        fillMode: Image.PreserveAspectFit
    }

    Rectangle {
        id: rectangle
        x: 0
        y: 41
        width: 38
        height: 51
        color: "#ffffff"
        radius: 20
    }

    Timeline {
        id: timeline
        animations: [
            TimelineAnimation {
                id: timelineAnimation
                paused: false
                alwaysRunToEnd: true
                loops: 1
                duration: 1000
                running: true
                to: 1000
                from: 0
            }
        ]
        endFrame: 100
        startFrame: 0
        enabled: true

        KeyframeGroup {
            target: line1
            property: "x"
            Keyframe {
                value: 1201
                frame: 100
            }

            Keyframe {
                value: 6
                frame: 0
            }
        }

        KeyframeGroup {
            target: path2839
            property: "x"
            Keyframe {
                value: 1198
                frame: 100
            }

            Keyframe {
                value: 3
                frame: 0
            }
        }

        KeyframeGroup {
            target: detail
            property: "x"
            Keyframe {
                value: 1183
                frame: 100
            }

            Keyframe {
                value: -11
                frame: 0
            }
        }

        KeyframeGroup {
            target: rectangle
            property: "width"
            Keyframe {
                value: 1234
                frame: 100
            }
        }

        KeyframeGroup {
            target: rectangle
            property: "height"
            Keyframe {
                value: 51
                frame: 100
            }
        }

        KeyframeGroup {
            target: rectangle
            property: "x"
            Keyframe {
                value: 0
                frame: 100
            }
        }

        KeyframeGroup {
            target: rectangle
            property: "color"
            Keyframe {
                value: "#00732b"
                frame: 0
            }

            Keyframe {
                value: "#00ff5f"
                frame: 100
            }
        }

        KeyframeGroup {
            target: text1
            property: "x"
            Keyframe {
                frame: 100
                value: 1205
            }

            Keyframe {
                frame: 0
                value: 20
            }
        }

        KeyframeGroup {
            target: text1
            property: "y"
            Keyframe {
                frame: 100
                value: 6
            }

            Keyframe {
                frame: 0
                value: 6
            }
        }

        KeyframeGroup {
            target: text2
            property: "x"
            Keyframe {
                frame: 100
                value: 1239
            }

            Keyframe {
                frame: 0
                value: 39
            }
        }

        KeyframeGroup {
            target: text2
            property: "y"
            Keyframe {
                frame: 100
                value: 6
            }

            Keyframe {
                frame: 0
                value: 6
            }
        }
    }

    Image {
        id: line1
        x: 5
        y: 31
        source: "images/Line 1.png"
        fillMode: Image.PreserveAspectFit
    }

    Image {
        id: path2839
        x: 2
        y: 28
        source: "images/Path 2839.png"
        fillMode: Image.PreserveAspectFit
    }



    Image {
        id: detail
        x: -12
        y: -14
        source: "images/Detail.png"
        fillMode: Image.PreserveAspectFit
    }


    Text {
        id: text1
        x: 25
        y: 6
        color: "#ffffff"
        text: timeline.currentFrame
        font.pixelSize: 12
        font.family: "roboto"
    }

    Text {
        id: text2
        x: 43
        y: 6
        color: "#ffffff"
        text: "%"
        font.pixelSize: 12
        font.family: "roboto"
    }
}

/*##^##
Designer {
    D{i:0;formeditorZoom:1.5;height:94;width:1235}D{i:3}D{i:39}
}
##^##*/
