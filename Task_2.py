class Movies:
    def __init__(self):
        self.movies = []

    def add_movie(self, movie):
        self.movies.append(movie)

class Comedy(Movies):
    def add_movie(self, movie):
        super().add_movie(movie)
        return f"Комедии: {self.movies}"

class Drama(Movies):
    def add_movie(self, movie):
        super().add_movie(movie)
        return f"Драмы: {self.movies}"

comedy = Comedy()
print(comedy.add_movie('Большой куш')) 

drama = Drama()
<<<<<<< HEAD
print(drama.add_movie('Оружейный барон'))  
=======
print(drama.add_movie('Оружейный барон'))  
>>>>>>> 8a4aa9e9ee244109adc17b424d0ab512805a4890
