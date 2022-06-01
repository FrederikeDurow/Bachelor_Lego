import QtQuick 2.15
import QtQuick.Controls 2.15

Item {
    id: item1
    width: 337
    height: 33

    states: [
        State {
            name: "Normal"
        }
    ]
    Image {
        id: rectangle983
        x: -28
        y: -23
        source: "../../Components/Select_type_section/Rectangle 983.png"
        fillMode: Image.PreserveAspectFit
    }
    TextField{
        id: nameinput
        label: "project_name"
        x: 0
        y: 0
        width: 321
        height: 16
        accpetableInput:  10 < text.length > 3
        validator: RegExpValidator { regExp: /^[0-9\+\-\#\*\ ]{3,}$/ }
        placeholderTextColor: "#000000"
        placeholderText: "Enter project name"
        background: "transparent"
    }
}
