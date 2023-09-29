from os import system
import sys
try:
    from PyQt5.QtWidgets import *
    from PyQt5.QtGui import *
    from PyQt5.QtCore import *
    from PyQt5.QtWebEngineWidgets import *
except ModuleNotFoundError:
    ls = ['pyqt5', 'pyqtwebengine']
    for any0 in ls:
        cmd = 'pip install ' + any0
        system(cmd)
except Exception as e:
    print(e)
    system(f"python3 {sys.argv[0]}")


class MyWebBrowser(QMainWindow):

    def __init__(self, *args, **kwargs):

        super(MyWebBrowser, self).__init__(*args, **kwargs)

        self.window = QWidget()
        self.window.setWindowTitle("Web Browser")

        self.layout = QVBoxLayout()
        self.horizontal = QHBoxLayout()

        self.url_bar = QTextEdit()
        self.url_bar.setMaximumHeight(30)

        self.go_btn = QPushButton("Go")
        self.go_btn.setMinimumHeight(30)

        self.back_btn = QPushButton("<-")
        self.back_btn.setMinimumHeight(30)

        self.forward_btn = QPushButton("->")
        self.forward_btn.setMinimumHeight(30)

        self.horizontal.addWidget(self.url_bar)
        self.horizontal.addWidget(self.go_btn)
        self.horizontal.addWidget(self.back_btn)
        self.horizontal.addWidget(self.forward_btn)

        self.browser = QWebEngineView()

        self.go_btn.clicked.connect(lambda: self.navigate(self.url_bar.toPlainText()))
        self.back_btn.clicked.connect(self.browser.back)
        self.forward_btn.clicked.connect(self.browser.forward)

        self.layout.addLayout(self.horizontal)
        self.layout.addWidget(self.browser)

        self.browser.setUrl(QUrl("http://google.com"))

        self.window.setLayout(self.layout)
        self.window.show()

    def navigate(self, url):
        if not url.startswith("http"):
            url = "https://" + url
            self.url_bar.setText(url)
        self.browser.setUrl(QUrl(url))


app = QApplication([])
window = MyWebBrowser()
app.exec_()
