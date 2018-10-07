
class Movie():
	def __init__(self, title, year, rating, runtime, genre, stars):
		self.title = title
		self.year = year
		self.rating = rating
		self.runtime = runtime
		self.genre = genre
		self.stars = stars

	def printMovie(self):
		print(self.title + ": " + self.year + ", " + self.rating + ", " + self.runtime + ", " + self.genre + ", " + self.stars)


class Movies():
	def __init__(self):
		self.movies = []
		self.createMoviesList()

	def createMoviesList(self):
		file = open("testfile.txt", "r")

		for line in file:

			line = line.strip().split(',')

			title = line[0].replace("'", "")
			year = line[1].replace(" ", "")
			rating = line[2].replace(" ", "")
			runtime = line[3].replace(" ", "").replace("min", "")
			stars = line[len(line) - 1].replace(" ", "")
			genre = ""


			for num in range(4, len(line) - 1):
				if num + 1 == len(line) - 1:
					genre += line[num].replace(" ", "")
				else:
					genre += (line[num].replace(" ", "") + ",")

			self.movies.append(Movie(title, year, rating, runtime, genre, stars))

		file.close

	def printMovies(self):
		for i in range(0, len(self.movies)):
			self.movies[i].printMovie()

	

def main():
	movies = Movies()
	movies.printMovies()

if __name__ == "__main__":
	main()




