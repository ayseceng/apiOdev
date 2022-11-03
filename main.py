import requests


class Movie:
    def __init__(self) -> None:
        self.api_url = "https://api.themoviedb.org/3"
        self.api_key = "4bcdc65bb9a1454fd36a706a71b561ef"

    def getPopulars(self):
        response = requests.get(f"{self.api_url}/movie/popular?api_key={self.api_key}&language=en-US&page=1")
        return response.json()

    def getSearchResults(self, keyword):
        response = requests.get(f"{self.api_url}/search/keywoard?api_key={self.api_key}&query={keyword}&page=1")
        return response.json()


movieApi = Movie()

while True:
    secim = input("1-Popular Movies\n2-Search Movies\n3-Exit\nSecim: ")

    if secim == "3":
        break
    else:
        if secim == "1":
            movies = movieApi.getPopulars()
            for movie in movies['results']:
                print(movie['title'])

        if secim == "2":
            keyword = input("keyword: ")
            movies = movieApi.getSearchResults(keyword)
            for movie in movies['results']:
                print(movie['name'])
