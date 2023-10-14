from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtGui import QPixmap, QIcon

class MyWebBrowser():
    def __init__(self):

        self.window = QWidget()
        self.window.setWindowTitle("Squirrel Web Browser")

        self.url_history = ["https://www.omar-cruz-rmz.com"]
        self.current_url_index = 0

        self.layout = QVBoxLayout()
        self.horizontal = QHBoxLayout()

        self.pixmap = QPixmap("Ardilla.png")
        self.icon = QIcon(self.pixmap)
        self.window.setWindowIcon(self.icon)

        self.url_bar = QLineEdit("https://www.omar-cruz-rmz.com")
        self.url_bar.setMaximumHeight(30)

        self.go_btn = QPushButton("Go")
        self.go_btn.setMinimumHeight(30)

        self.back_btn = QPushButton("<")
        self.back_btn.setMinimumHeight(30)

        self.forward_btn = QPushButton(">")
        self.forward_btn.setMinimumHeight(30)

        self.horizontal.addWidget(self.url_bar)
        self.horizontal.addWidget(self.go_btn)
        self.horizontal.addWidget(self.back_btn)
        self.horizontal.addWidget(self.forward_btn)

        self.browser = QWebEngineView()
        self.go_btn.clicked.connect(lambda: self.navigate(self.url_bar.text()))
        self.back_btn.clicked.connect(self.navigate_back)
        self.forward_btn.clicked.connect(self.navigate_forward)

        self.layout.addLayout(self.horizontal)
        self.layout.addWidget(self.browser)

        self.browser.setUrl(QUrl("https://www.omar-cruz-rmz.com"))

        self.url_bar.returnPressed.connect(self.go_btn.click)

        self.window.setLayout(self.layout)
        self.window.show()

    def navigate(self, url):
        if not url.startswith("http"):
            url = "http://www." + url
            self.url_bar.setText(url)
        self.browser.setUrl(QUrl(url))
        self.url_history = self.url_history[:self.current_url_index + 1]
        self.url_history.append(url)
        self.current_url_index += 1

    def navigate_back(self):
        if self.current_url_index > 0:
            self.current_url_index -= 1
            previous_url = self.url_history[self.current_url_index]
            self.url_bar.setText(previous_url)
            self.browser.setUrl(QUrl(previous_url))

    def navigate_forward(self):
        if self.current_url_index < len(self.url_history) - 1:
            self.current_url_index += 1
            next_url = self.url_history[self.current_url_index]
            self.url_bar.setText(next_url)
            self.browser.setUrl(QUrl(next_url))

app = QApplication([])
window = MyWebBrowser()
app.exec_()