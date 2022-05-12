

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
        id: rectangle3
        x: 100
        y: 0
        width: 1820
        height: 36
        color: "#161c28"
        border.width: 0

        Fullscreen_btn {
            id: fullscreen_btn
            x: 1748
            y: 0
        }

        Minimizescreen_btn {
            id: minimizescreen_btn
            x: 1712
            y: 0
        }
    }

    MenuBar {
        id: menuBar
        x: 100
        y: 0
        width: 359
        height: 36

        Menu {
            title: qsTr("File")
            id: file
            Action {
                id: newprojectAction
                text: qsTr("&New project")
                shortcut: StandardKey.New
            }
            Action {
                id: loadprojectAction
                text: qsTr("&Load project")
                shortcut: StandardKey.Open
            }
            Action {
                id: saveAction
                text: qsTr("&Save File")
                shortcut: StandardKey.Save
            }
            Action {
                id: saveasAction
                text: qsTr("&Save As...")
                shortcut: StandardKey.SaveAs
            }
        }
        Menu {
            title: qsTr("Edit")
            id: edit
            Action {
                id: undoAction
                text: qsTr("&Undo")
                shortcut: StandardKey.Undo
            }

            Action {
                id: redoAction
                text: qsTr("&Redo")
            }
            Action {
                id: cutAction
                text: qsTr("&Cut")
                shortcut: StandardKey.Cut
            }
            Action {
                id: copyAction
                text: qsTr("&Copy")
                shortcut: StandardKey.Copy
            }
            Action {
                id: pasteAction
                text: qsTr("&Paste")
                shortcut: StandardKey.Paste
            }
        }
        Menu {
            title: qsTr("View")
            id: view
            Action {
                id: zoominAction
                text: qsTr("&Zoom in")
                shortcut: StandardKey.ZoomIn
            }
            Action {
                id: zoomoutAction
                text: qsTr("&Zoom out")
                shortcut: StandardKey.ZoomOut
            }
            Menu {
                title: qsTr("Hide Objects")
                Action {
                    text: qsTr("Bounding Box")
                    checkable: true
                    checked: true
                }
                Action {
                    text: qsTr("Point Tracker")
                    checkable: true
                    checked: true
                }
            }
        }
        Menu {
            title: qsTr("Help")
            id: help
            Action {
                id: quickGuideAction
                text: qsTr("Quick Guide")
            }
            Action {
                id: documentationAction
                text: qsTr("Documentation")
            }
        }

        delegate: MenuBarItem {
            id: menuBarItem
            leftPadding: 20
            font.pointSize: 12

            contentItem: Text {
                text: menuBarItem.text
                font.family: "Roboto"
                opacity: enabled ? 1.0 : 0.3
                color: menuBarItem.highlighted ? "#ffffff" : "#ffffff"
                horizontalAlignment: Text.AlignLeft
                verticalAlignment: Text.AlignVCenter
                elide: Text.ElideRight
            }

            background: Rectangle {
                implicitWidth: 40
                implicitHeight: 40
                opacity: enabled ? 1 : 0.3
                color: menuBarItem.highlighted ? "#707c8d" : "transparent"
            }
        }

        background: Rectangle {
            implicitWidth: 40
            implicitHeight: 40
            color: "#161c28"
        }
    }

    Text {
        id: v_text
        x: 34
        y: 63
        width: 32
        height: 19
        text: "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\np, li { white-space: pre-wrap; }\n</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Roboto'; font-size:10pt;\">V</span></p></body></html>"
        horizontalAlignment: Text.AlignHCenter
        lineHeight: 0.3
        textFormat: Text.RichText
        font.pointSize: 10
        font.weight: Font.Normal
        font.family: "roboto"
    }

    Text {
        id: version_text
        x: 34
        y: 81
        width: 32
        height: 24
        text: "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\np, li { white-space: pre-wrap; }\n</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Roboto'; font-size:10pt;\">1.0</span></p></body></html>"
        horizontalAlignment: Text.AlignHCenter
        lineHeight: 0.3
        font.styleName: "#000000"
        textFormat: Text.RichText
        font.pointSize: 12
        font.weight: Font.Bold
        font.family: " Roboto"
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

    Closewindow_btn {
        id: closewindow_btn
        x: 1884
        y: 0
    }
}

/*##^##
Designer {
    D{i:0;formeditorZoom:0.5;height:1080;width:1920}
}
##^##*/

