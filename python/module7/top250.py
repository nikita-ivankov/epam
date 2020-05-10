import requests, json
from bs4 import BeautifulSoup, Tag

def parse_top_250(file):
    result = []
    url = 'https://imdb.com/chart/top'

    request = requests.get(url, headers={'Accept-Language': 'En-us'})
    soup = BeautifulSoup(request.text, 'lxml')

    film_list = soup.find(class_='lister-list')

    for film in film_list.find_all('tr'):
        if isinstance(film, Tag):
            about_movie = film.find(class_='titleColumn').a['title'].replace(' (dir.), ', ',').split(',')
            Raiting = film.find(class_='ratingColumn imdbRating').text.replace('\n','')
            Movie = film.find(class_='titleColumn').a.text
            Position = film.find(class_="posterColumn").find('span')['data-value']
            Year = film.find(class_='titleColumn').find(class_="secondaryInfo").text.replace('(','').replace(')','')
            Director = about_movie[0]
            Crew = ','.join(about_movie[1:])

            result.append({Movie:{"Position": Position, "Year": Year, "Director": Director,
                                  "Crew": Crew, "Rating": Raiting}})

    with open(file, 'w') as output_file:
        json.dump(result, output_file)

if __name__ == '__main__':
    parse_top_250('result.txt')
