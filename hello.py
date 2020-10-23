from PyQt5.QtQml import QQmlApplicationEngine, qmlRegisterType
from PyQt5.QtGui import QGuiApplication, QIcon
from PyQt5.QtCore import QUrl, Qt
import resources

if __name__ == '__main__':
    QGuiApplication.setAttribute(Qt.AA_EnableHighDpiScaling);

    app = QGuiApplication(sys.argv)

    engine = QQmlApplicationEngine()
    engine.load(":/main.qml")
    if not engine.rootObjects():
        sys.exit(-1)

    try:
        exitCode = app.exec_()

        del engine
        
        sys.exit(exitCode)
    except:
        print("exiting")
