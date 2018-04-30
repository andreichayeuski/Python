from bs4 import BeautifulSoup
from requests import request
from pyparsing import Word, alphas, ZeroOrMore, Suppress, Optional
import re


def genre_parse(str):
    result = re.findall(r'[А-Я][а-я]+', str)
    return result


def get_page(str, filename):
    text = request('get', str).text
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(text)
    f.close()


def get_hrefs(soup):
    print(soup.title)
    div = soup.find('div', class_='events-block js-cut_wrapper')
    li = div.find_all('li', class_='lists__li')
    filename = soup.title.text + 'list.txt'
    file = open(filename, 'a')
    file.close()
    file = open(filename, 'r')
    text = file.read()
    file.close()
    file = open(filename, 'a')
    for a in li:
        elem = a.find('a', class_='name')
        span = elem.get('href')
        if span in text:
            print('this link is here')
        else:
            file.writelines(span + '\n')
            get_info(span)
    file.close()
    file = open(filename)
    for line in file:
        print(line)
    file.close()


def get_info(str):
    filename = 'result.html'
    # get_page(str, filename)
    html = open(filename, 'rb')
    soup = BeautifulSoup(html.read(), "html.parser")
    result = open('result.json', 'w+')
    # MAIN IMAGE
    img = soup.find('img', class_='main_image').get('src')
    print(img)
    result.write('{"img":"' + img + '",')
    # NAME
    name = soup.find('h1', id='event-name').text
    print(name)
    result.write('"name":"' + name + '",')
    # AGE RESTRICTIONS
    age = soup.find('span', class_='label').text
    print(age)
    result.write('"age":"' + age + '",')
    # GENRE
    genre = soup.find('td', class_='genre').text
    genre = genre_parse(genre)
    print(genre)
    result.write('"genre":{')
    for a in genre:
        result.write('"' + a + '",')
    result.seek(result.tell() - 1)
    result.write('},')
    # YEAR
    year = soup.find('td', class_='year').text
    print(year)
    result.write('"year":"' + year + '",')
    # COUNTRY
    country = soup.find('td', class_='author').text
    print(country)
    result.write('"county":"' + country + '",')
    # DURATION
    duration = soup.find('td', class_='duration').text
    print(duration)
    result.write('"duration":"' + duration + '",')
    # RATING
    rating = soup.find('span', class_='rating-big__value').text
    print(rating)
    result.write('"rating":"' + rating + '",')
    # INFO
    info = soup.find('div', itemprop='description').next
    print(info)
    result.write('"info":"' + info + '",')
    # VIDEO Не знаю, что делать, потому что не хочет грузить
    # video = soup.find('video').get('src')
    # print(video)
    # MORE IMAGE (we need they?)
    img_more = soup.find_all('td', itemprop='image')
    image = '"image":{'
    for a in img_more:
        image += '"' + a.find('a').get('href') + '",'
    print(image)
    result.write(image)
    result.seek(result.tell() - 1)
    result.write('}}')


def main():
    # filename = 'out.html'
    # get_page('https://afisha.tut.by/film', filename)
    # html = open(filename, 'rb')
    # soup = BeautifulSoup(html.read(), "html.parser")

    # get_hrefs(soup)
    get_info('result.html')
    # print(elem)


if __name__ == '__main__':
    main()
