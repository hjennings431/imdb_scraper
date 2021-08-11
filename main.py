import requests
from bs4 import BeautifulSoup
from requests import get

url = "https://www.imdb.com/search/title?release_date=2017&sort=num_votes,desc&page=1"

# get the HTML data from the url
response = get(url)
html_data = BeautifulSoup(response.text, "html.parser")

# search the HTML data for divs with a specific class ID
movie_divs = html_data.find_all('div', class_ = "lister-item mode-advanced")

# getting info about the first movie on the list
first_movie = movie_divs[0]
first_movie_name = first_movie.h3.a.text
first_year = first_movie.h3.find('span', class_ = 'lister-item-year text-muted unbold')
first_year = first_year.text
first_rating = float(first_movie.strong.text)

# output info
print(first_movie_name, first_year, first_rating)
