import QtQuick 2.15
import QtQuick.Controls 2.5

ApplicationWindow {
    id: appWindow
    width: 480
    height: 640
    visible: true
    title: qsTr("Test deploy use pyinstaller for pyqt5")

    Text {
        anchors.centerIn: parent
        text: qsTr("Hello, World")
    }
}
