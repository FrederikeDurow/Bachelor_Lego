/*
This is a UI file (.ui.qml) that is intended to be edited in Qt Design Studio only.
It is supposed to be strictly declarative and only uses a subset of QML. If you edit
this file manually, you might introduce QML code that is not supported by Qt Design Studio.
Check out https://doc.qt.io/qtcreator/creator-quick-ui-forms.html for details on .ui.qml files.
*/

import QtQuick
import QtQuick.Controls
import Vister
import QtQuick.Studio.Components 1.0

Rectangle {
    id: background
    width: Constants.width
    height: Constants.height
    color: "#1b2330"

    border.width: 0
    transformOrigin: Item.Center

    Image {
        id: edit_dropdown
        x: 0
        y: 0
        source: "C:/Users/rasm4/OneDrive/Dokumenter/Test/Edit_dropdown.svg"
        fillMode: Image.PreserveAspectFit
    }

    Image {
        id: load_Project_Button
        x: 0
        y: 0
        source: "C:/Users/rasm4/OneDrive/Dokumenter/Test/Load_Project_Button.svg"
        fillMode: Image.PreserveAspectFit
    }

    Image {
        id: load_Project_Button1
        x: 265
        y: 215
        source: "images/Load_Project_Button.svg"
        fillMode: Image.PreserveAspectFit
    }

    Rectangle {
        id: rectangle
        x: 0
        y: 0
        width: 100
        height: 112
        color: "#c9e0fe"
        border.width: 0
    }

    Rectangle {
        id: toolbar
        x: 100
        y: 0
        width: 1820
        height: 36
        color: "#161c28"
        border.width: 0
        antialiasing: true

        Row {
            id: row
            width: 495
            height: 36
            anchors.verticalCenter: parent.verticalCenter
            anchors.left: parent.left
            spacing: 40
            padding: 40
            topPadding: 0
            anchors.leftMargin: 0

            Text {
                id: file_toolbar
                color: "#ffffff"
                text: qsTr("File")
                anchors.verticalCenter: parent.verticalCenter
                anchors.left: parent.left
                font.pixelSize: 16
                anchors.leftMargin: 50
            }

            Text {
                id: edit_toolbar
                color: "#ffffff"
                text: qsTr("Edit")
                anchors.verticalCenter: parent.verticalCenter
                anchors.left: file_toolbar.right
                font.pixelSize: 16
                anchors.leftMargin: 50
            }

            Text {
                id: view_toolbar
                color: "#ffffff"
                text: qsTr("View")
                anchors.verticalCenter: parent.verticalCenter
                anchors.left: edit_toolbar.right
                font.pixelSize: 16
                anchors.leftMargin: 50
            }

            Text {
                id: help_toolbar
                color: "#ffffff"
                text: qsTr("Help")
                anchors.verticalCenter: parent.verticalCenter
                anchors.left: view_toolbar.right
                font.pixelSize: 16
                anchors.leftMargin: 50
            }
        }

        Row {
            id: row1
            x: 1687
            y: 0
            width: 133
            height: 36
            rightPadding: 21
            topPadding: 8
            spacing: 16
            layoutDirection: Qt.RightToLeft

            Image {
                id: dell
                width: 19
                source: "images/Dell.png"
                fillMode: Image.PreserveAspectFit
            }

            Image {
                id: out
                source: "images/Out.png"
                fillMode: Image.PreserveAspectFit
            }

            Image {
                id: creditcard
                y: 10
                source: "images/Credit card.png"
                fillMode: Image.PreserveAspectFit
            }
        }
    }

    Text {
        id: v_text
        x: 34
        y: 56
        width: 32
        height: 19
        text: "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\np, li { white-space: pre-wrap; }\n</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Uni Sans'; font-size:12pt; font-weight:700;\">V</span></p></body></html>"
        horizontalAlignment: Text.AlignHCenter
        lineHeight: 0.3
        textFormat: Text.RichText
        font.pointSize: 12
        font.weight: Font.Normal
        font.family: "Arial"
    }

    Text {
        id: version_text
        x: 34
        y: 81
        width: 32
        height: 24
        text: "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\np, li { white-space: pre-wrap; }\n</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Poppins'; font-size:12pt;\">1.0</span></p></body></html>"
        horizontalAlignment: Text.AlignHCenter
        lineHeight: 0.3
        font.styleName: "#000000"
        textFormat: Text.RichText
        font.pointSize: 12
        font.weight: Font.Bold
        font.family: "Arial"
    }

    Image {
        id: logoRezisedto256x256
        x: 30
        y: 10
        width: 40
        source: "../../../Simple Tests/PartOne/Graphical_elements/LogoRezisedto256x256.svg"
        fillMode: Image.PreserveAspectFit
    }


    Rectangle {
        id: rectangle1
        x: 1901
        y: 36
        width: 19
        height: 1044
        color: "#252d3a"
        border.width: 0
    }

    GroupItem {
        id: groupItem
        x: 273
        y: 121
    }

    Rectangle {
        id: rectangle2
        x: 0
        y: 112
        width: 100
        height: 968
        color: "#161c28"
        border.color: "#161c28"
        border.width: 0
    }

    Column {
        id: column
        x: 0
        y: 112
        width: 100
        height: 935
        topPadding: 200
        rightPadding: 30
        leftPadding: 33
        spacing: 80





        Image {
            id: home_light
            source: "../../Components/Base/Home_light.png"
            fillMode: Image.PreserveAspectFit
        }

        Image {
            id: filter1
            y: 399
            source: "../../Components/Base/Filter-1.png"
            fillMode: Image.PreserveAspectFit
        }

        Image {
            id: stop_and_play_light
            source: "../../Components/Base/Stop_and_play_light.png"
            fillMode: Image.PreserveAspectFit
        }


        Image {
            id: desk_alt_light
            source: "../../Components/Base/Desk_alt_light.png"
            fillMode: Image.PreserveAspectFit
        }
    }

    Image {
        id: info_fill
        x: 39
        y: 991
        width: 23
        height: 23
        source: "images/Info_fill.png"
        fillMode: Image.PreserveAspectFit
    }
}

/*##^##
Designer {
    D{i:0;formeditorZoom:0.5;height:1080;width:1920}
}
##^##*/
