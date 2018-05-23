from bs4 import BeautifulSoup
from requests import request
import datetime
from datetime import *


def get_page(string, filename):
    text = request('get', string).text
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(text)


def get_sessions(soup, film_date):
    global i
    print(film_date)
    all_div = soup.find_all('div', class_='b-film-info js-ttinfo')
    for film_div in all_div:
        cinema_link = film_div.find('div', class_='name ')
        all_film_li = film_div.find_all('li', class_='b-film-list__li')
        cinema_link = '' if cinema_link is None else cinema_link.find('a').get('href')
        print('\t' + cinema_link)
        for film_li in all_film_li:
            film_link = film_li.find('div', class_='film-name')
            film_link = film_link.find('a').get('href')
            print('\t\t' + film_link)
            all_ul = film_li.find_all('ul', class_='b-list b-shedule-list')
            for ul in all_ul:
                all_li = ul.find_all('li', class_='lists__li')
                for li in all_li:
                    film_time = li.find('a')
                    film_time = film_time.contents[0].strip()
                    print('\t\t\t' + film_time)
                    filename = "Session/" + str(i) + '.xml'
                    print(i)
                    i += 1
                    with open(filename, 'w+', encoding='utf-8') as result:
                        result.write('<?xml version="1.0"?>\n<SessionFromFile xmlns:xsi="http://www.w3.org/2001/')
                        result.write('XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema">\n')
                        result.write('<Time>' + film_time + '</Time>\n')
                        result.write('<Date>' + film_date + '</Date>\n')
                        result.write('<FilmLink>' + film_link + '</FilmLink>\n')
                        result.write('<CinemaLink>' + cinema_link + '</CinemaLink>\n')
                        result.write('</SessionFromFile>')


i = 0


def main():
    filename = 'out2.html'
    day = datetime.today().day
    print(day)
    for x in range(day, day + 4):
        get_page('https://afisha.tut.by/day/film/2018/05/' + str(x), filename)
        html = open(filename, 'rb')
        soup = BeautifulSoup(html.read(), "html.parser")
        film_date = str(x) + '.05.2018'
        get_sessions(soup, film_date)


if __name__ == '__main__':
    main()
