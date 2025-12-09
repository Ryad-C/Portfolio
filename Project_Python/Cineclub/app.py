

from PySide6 import QtWidgets
from movie import get_movies, Movie


class App(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ciné Club")
        self.setup_ui()
        self.populate_movies()
        self.setup_connections()

    def setup_ui(self):
        self.layout_ = QtWidgets.QVBoxLayout(self)

        self.le_titleMovie = QtWidgets.QLineEdit()
        self.btn_addMovie = QtWidgets.QPushButton("Ajouter un film")
        self.lw_listMovie = QtWidgets.QListWidget()
        self.lw_listMovie.setSelectionMode(QtWidgets.QListWidget.SelectionMode.ExtendedSelection)
        self.btn_removeMovie = QtWidgets.QPushButton("Supprimer le(s) film(s)")

        self.layout_.addWidget(self.le_titleMovie)
        self.layout_.addWidget(self.btn_addMovie)
        self.layout_.addWidget(self.lw_listMovie)
        self.layout_.addWidget(self.btn_removeMovie)

    def setup_connections(self):
        self.le_titleMovie.returnPressed.connect(self.add_movie)
        self.btn_addMovie.clicked.connect(self.add_movie)
        self.btn_removeMovie.clicked.connect(self.remove_movie)

    def populate_movies(self):
        list_movies = get_movies()
        for movie in list_movies:
            self.lw_listMovie.addItem(str(movie))

    def add_movie(self):
        movie = self.le_titleMovie.text()        
        self.lw_listMovie.clear()
        Movie(movie).add_to_movies()
        self.populate_movies()
        self.le_titleMovie.clear()

    def remove_movie(self):
        for items in self.lw_listMovie.selectedItems():
            Movie(items.text()).remove_from_movies()
        self.lw_listMovie.clear()
        self.populate_movies()
        

if __name__ == "__main__":
    app = QtWidgets.QApplication([]) 
    win = App()
    win.show()
    app.exec()
