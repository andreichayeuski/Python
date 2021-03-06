from bs4 import BeautifulSoup
from requests import request
import re
import datetime
from datetime import *


def genre_parse(string):
    result = re.findall(r'[А-Я][а-я]+', string)
    return result


def get_substr_date(string):
    result = string.replace('В прокате ', '')
    return result


def get_page(string, filename):
    text = request('get', string).text
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(text)


def replace_all_slash(string):
    res = string.replace('/', '\/')
    return res


def replace_all_kav(string):
    res = string.replace('\"', '\\"')
    return res


def get_href(soup):
    print(soup.title)
    div = soup.find('div', class_='events-block js-cut_wrapper')
    li = div.find_all('li', class_='lists__li')
    filename = 'Film/' + soup.title.text + 'list.txt'
    open(filename, 'a').close()
    with open(filename, 'r') as file:
        text = file.read()

    with open(filename, 'a') as file:
        for a in li:
            elem = a.find('a', class_='name')
            span = elem.get('href')
            if span in text:
                print('this link is here')
            else:
                file.writelines(span + '\n')
                get_info(span)

    with open(filename, 'r') as file:
        for line in file:
            print(line)


def get_info(string):
    source = 'Film/result.html'
    global i
    filename = 'Film/' + str(i) + '.xml'
    i += 1
    print(i)
    get_page(string, source)
    html = open(source, 'rb')
    soup = BeautifulSoup(html.read(), "html.parser")
    with open(filename, 'w+', encoding='utf-8') as result:
        result.write('<?xml version="1.0"?>\n<Film xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" ')
        result.write('xmlns:xsd="http://www.w3.org/2001/XMLSchema">\n')
        # AGE RESTRICTIONS
        age = soup.find_all('span', class_='label')
        for elem in age:
            if elem.text[0] == 'П' or elem.text == '3D':
                print('no restrictions')
                age = ''
            else:
                age = elem.text
                break
        print(age)
        result.write('<Age>' + ('' if age == [] else age) + '</Age>\n')
        # COUNTRY
        country = soup.find('td', class_='author')
        country = '' if country is None else country.text
        print(country)
        result.write('<Country>' + country + '</Country>\n')
        # DATE
        film_date = soup.find('td', class_='date')
        film_date = '' if film_date is None else film_date.text
        film_date = get_substr_date(film_date)
        print(film_date)
        result.write('<Date>' + film_date + '</Date>\n')
        # DURATION
        duration = soup.find('td', class_='duration')
        duration = '' if duration is None else duration.text
        print(duration)
        result.write('<Duration>' + duration + '</Duration>\n')
        # GENRE
        genre = soup.find('td', class_='genre')
        result.write('<Genre>\n')
        if genre is None:
            result.write(' ')
        else:
            genre = genre.text
            result.write(genre)
        result.write('</Genre>\n')
        # ID
        result.write('<Id>' + str(i) + '</Id>\n')
        # LINK
        link = string
        print(link)
        result.write('<Link>' + link + '</Link>\n')
        # IMAGE_MAIN
        image_main = soup.find('img', class_='main_image')
        image_main = '' if image_main is None else image_main.get('src')
        print(image_main)
        result.write('<Image_Main>' + image_main + '</Image_Main>\n')
        # MORE IMAGE
        img_more = soup.find_all('td', itemprop='image')
        image = '<Images>\n'
        if img_more.__len__() == 0:
            img_more = soup.find_all('img', class_='fotorama__img')
            if img_more.__len__() == 0:
                result.write(image)
                result.write(' ')
            else:
                for a in img_more:
                    image += a.get('src') + ' '
                print(image)
                result.write(image)
        else:
            for a in img_more:
                image += a.find('a').get('href') + ' '
            print(image)
            result.write(image)
        result.write('</Images>\n')
        # INFO
        info = soup.find('span', class_='_reachbanner_')
        if info is None:
            info = soup.find('div', itemprop='description')
            info = '' if info is None else info.contents[0].strip()
        else:
            info = info.text
        print(info)
        result.write('<Info>' + info + '</Info>\n')
        # NAME
        name = soup.find('h1', id='event-name')
        name = '' if name is None else name.text
        print(name)
        result.write('<Name>' + name + '</Name>\n')
        # RATING
        rating = soup.find('span', class_='rating-big__value')
        rating = '' if rating is None else rating.text
        print(rating)
        result.write('<Rating>' + rating + '</Rating>\n')
        # VIDEO
        text = open(source, 'r', encoding='charmap')
        temp = text.read()
        buf = temp.find('"video", file: ')
        video = ''
        if buf != -1:
            buf += 16
            print(temp[buf])
            while temp[buf] != '"':
                video += temp[buf]
                buf += 1
            print(video)
        result.write('<Video>' + video + '</Video>\n')
        # YEAR
        year = soup.find('td', class_='year')
        year = '' if year is None else year.text
        print(year)
        result.write('<Year>' + year + '</Year>\n')
        result.write('</Film>')


i = 0


def main():
    filename = 'Film/out.html'
    day = datetime.today().day
    print(day)
    for x in range(day, day + 4):
        get_page('https://afisha.tut.by/day/film/2018/05/' + str(x), filename)
        html = open(filename, 'rb')
        soup = BeautifulSoup(html.read(), "html.parser")
        get_href(soup)


if __name__ == '__main__':
    main()
