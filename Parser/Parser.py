from bs4 import BeautifulSoup
from requests import request
import re


def genre_parse(string):
    result = re.findall(r'[А-Я][а-я]+', string)
    return result


def get_page(string, filename):
    text = request('get', string).text
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(text)


def get_href(soup):
    print(soup.title)
    div = soup.find('div', class_='events-block js-cut_wrapper')
    li = div.find_all('li', class_='lists__li')
    filename = soup.title.text + 'list.txt'
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
    source = 'result.html'
    global i
    filename = "" + str(i) + '.json'
    i += 1
    print(i)
    get_page(string, source)
    html = open(source, 'rb')
    soup = BeautifulSoup(html.read(), "html.parser")
    with open(filename, 'w+', encoding='utf-8') as result:
        # MAIN IMAGE
        image_main = soup.find('img', class_='main_image')
        image_main = '' if image_main is None else image_main.get('src')
        print(image_main)
        result.write('{"image_main":"' + image_main + '",')
        # NAME
        name = soup.find('h1', id='event-name')
        name = '' if name is None else name.text
        print(name)
        result.write('"name":"' + name + '",')
        # AGE RESTRICTIONS
        age = soup.find('span', class_='label')
        age = '' if age is None else age.text
        print(age)
        result.write('"age":"' + age + '",')
        # GENRE
        genre = soup.find('td', class_='genre')
        if genre is None:
            genre = ''
            result.write('"genre":{' + genre + '},')
        else:
            genre = genre.text
            genre = genre_parse(genre)
            print(genre)
            result.write('"genre":{')
            for a in genre:
                result.write('"' + a + '",')
            result.seek(result.tell() - 1)
            result.write('},')
        # YEAR
        year = soup.find('td', class_='year')
        year = '' if year is None else year.text
        print(year)
        result.write('"year":"' + year + '",')
        # COUNTRY
        country = soup.find('td', class_='author')
        country = '' if country is None else country.text
        print(country)
        result.write('"county":"' + country + '",')
        # DURATION
        duration = soup.find('td', class_='duration')
        duration = '' if duration is None else duration.text
        print(duration)
        result.write('"duration":"' + duration + '",')
        # RATING
        rating = soup.find('span', class_='rating-big__value')
        rating = '' if rating is None else rating.text
        print(rating)
        result.write('"rating":"' + rating + '",')
        # INFO
        info = soup.find('div', itemprop='description')
        info = '' if info is None else info.next
        print(info)
        result.write('"info":"' + info + '",')
        # VIDEO
        text = open(source, 'r', encoding='charmap')
        temp = text.read()
        buf = temp.find('"video", file: ')
        video = '"'
        if buf != -1:
            buf += 15
            print(temp[buf])
            while temp[buf] != '"':
                video += temp[buf]
                buf += 1
            print(video)
        video += '"'
        result.write('"video":' + video + ',')
        # MORE IMAGE (we need they?)
        img_more = soup.find_all('td', itemprop='image')
        image = '"image":{'
        if img_more.count(str) == 0:
            image = '"image":{}'
            result.write(image)
        else:
            for a in img_more:
                image += '"' + a.find('a').get('href') + '",'
            print(image)
            result.write(image)
            result.seek(result.tell() - 1)
            result.write('}')
        result.write('}')


i = 0


def main():
    filename = 'out.html'
    get_page('https://afisha.tut.by/film', filename)
    html = open(filename, 'rb')
    soup = BeautifulSoup(html.read(), "html.parser")
    get_href(soup)


if __name__ == '__main__':
    main()
