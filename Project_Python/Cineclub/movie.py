#api

from pathlib import Path
import json
import logging

logger = logging.basicConfig(level=logging.WARNING)

DATA_DIR = Path.cwd() / "data" / "movies.json"
   
def get_movies():
    movies_instances = []
    with open(DATA_DIR, "r") as f:
        movies = json.load(f)
        for movie_title in movies:
            movies_instances.append(Movie(movie_title))

        return movies_instances

class Movie:
    def __init__(self, title):
        self.title = title.title()

    def __str__(self):
        return self.title
    
    def _get_movies(self):
        with open(DATA_DIR, "r") as f:
            return json.load(f)

    def _write_movies(self, movies):
        with open(DATA_DIR, "w") as f:
            json.dump(movies, f, indent = 4)
    
    def add_to_movies(self):
        movie = self._get_movies()
        if self.title in movie:
            logging.warning(f"Le film {self.title} est déja présent dans la liste")
            return True
        else:
            movie.append(self.title)
            self._write_movies(movie)
            return False
    
    def remove_from_movies(self):
        movie = self._get_movies()
        if self.title in movie:
            movie.remove(self.title)
            self._write_movies(movie)
            return True
        else:
            logging.warning(f"Le film {self.title} n'est pas présent dans la liste")
            return False

    
if __name__ == "__main__":
    Movie("harry potter").add_to_movies()
    print(get_movies())