/****************************************************************************
**
** Copyright (C) 2021 The Qt Company Ltd.
** Contact: https://www.qt.io/licensing/
**
** This file is part of Qt Quick Studio Components.
**
** $QT_BEGIN_LICENSE:GPL$
** Commercial License Usage
** Licensees holding valid commercial Qt licenses may use this file in
** accordance with the commercial license agreement provided with the
** Software or, alternatively, in accordance with the terms contained in
** a written agreement between you and The Qt Company. For licensing terms
** and conditions see https://www.qt.io/terms-conditions. For further
** information use the contact form at https://www.qt.io/contact-us.
**
** GNU General Public License Usage
** Alternatively, this file may be used under the terms of the GNU
** General Public License version 3 or (at your option) any later version
** approved by the KDE Free Qt Foundation. The licenses are as published by
** the Free Software Foundation and appearing in the file LICENSE.GPL3
** included in the packaging of this file. Please review the following
** information to ensure the GNU General Public License requirements will
** be met: https://www.gnu.org/licenses/gpl-3.0.html.
**
** $QT_END_LICENSE$
**
****************************************************************************/

import QtQuick
import QtQuick.Window
import Vister

Window {
    width: homeScreen.width
    height: homeScreen.height
    opacity: 1

    visible: true
    title: "Vister"
    
    Screen01 {
        id: homeScreen

        Image {
            id: logo_big
            x: 372
            y: 131
            height: 300
            source: "images/LogoRezisedto256x256.svg"
            fillMode: Image.PreserveAspectFit
        }

        Text {
            id: text1
            x: 766
            y: 157
            color: "#ffffff"
            text: qsTr("Welcome To Vister")
            font.pixelSize: 80
            font.family: "Arial"
        }

        Loadproject_button {
            id: loadproject_button
            x: 582
            y: 577
            checkable: true
            autoExclusive: true

            Connections {
                target: loadproject_button
                onClicked: popup.state = 'Normal'
            }
        }

        Createproject_button {
            id: createproject_button
            x: 140
            y: 577

            Connections {
                target: createproject_button
                onClicked: selectTestingType.state = 'Normal'
            }
        }



        Text {
            id: text2
            x: 766
            y: 298
            color: "#bccbe0"
            text: qsTr("Vister is a Computer Vision based program that enables you to create various experiment using only a Camera
and a UR.

Vistor allows you to extract essential information from the UR robot while in operation simountanous applying
Computer Vision algorithms to each element to detect how they behave under different circumstances ")
            font.pixelSize: 16
        }

        Popup {
            id: popup
            x: 538
            y: 304
            visible: false
            enabled: false
        }

        SelectTestingType {
            id: selectTestingType
            x: 356
            y: 133
            visible: false
            enabled: false
        }
    }

    Screen01 {
        id: setupScreen
        x: 0
        y: 1124
    }

}


/*##^##
Designer {
    D{i:0;formeditorZoom:0.5}
}
##^##*/
