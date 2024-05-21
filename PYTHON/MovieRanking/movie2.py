import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QTableWidget, QTableWidgetItem
from PyQt5.QtGui import QPixmap
from bs4 import BeautifulSoup
import urllib.request

class MovieRankingApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("영화 순위")
        self.setGeometry(100, 100, 800, 600)

        self.initUI()

    def initUI(self):
        self.tableWidget = QTableWidget(self)
        self.tableWidget.setGeometry(50, 50, 700, 500)
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setHorizontalHeaderLabels(["순위", "제목", "예매율"])

        self.updateMovieRanking()

    def updateMovieRanking(self):
        movieUrl = "https://m.moviechart.co.kr/rank/realtime/index/image"

        htmlObject = urllib.request.urlopen(movieUrl)
        webPage = htmlObject.read()
        bsObject = BeautifulSoup(webPage, 'html.parser')
        tag = bsObject.find('ul', {'class':'movieBox-list'})
        all_movies = tag.findAll('li', {'class':'movieBox-item'})

        for idx, movie in enumerate(all_movies, start=1):
            title = movie.find("div", {"class":"movie-title"}).find("a").text
            ticketing = movie.find("li", {"class":"ticketing"}).find("span").text
            self.tableWidget.insertRow(idx-1)
            self.tableWidget.setItem(idx-1, 0, QTableWidgetItem(str(idx)))
            self.tableWidget.setItem(idx-1, 1, QTableWidgetItem(title))
            self.tableWidget.setItem(idx-1, 2, QTableWidgetItem(ticketing))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    movieRankingApp = MovieRankingApp()
    movieRankingApp.show()
    sys.exit(app.exec_())
