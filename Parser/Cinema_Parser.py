from bs4 import BeautifulSoup
from requests import request
import re


def get_page(string, filename):
    text = request('get', string).text
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(text)


def get_href(soup):
    print(soup.title)
    div = soup.find_all('div', class_='title')
    filename = 'Cinema/' + soup.title.text.replace('|', '_', 1) + 'list.txt'
    open(filename, 'a').close()
    with open(filename, 'r') as file:
        text = file.read()

    with open(filename, 'a') as file:
        for a in div:
            elem = a.find('a')
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
    source = 'Cinema/result1.html'
    global i
    filename = "Cinema/" + str(i) + '.xml'
    i += 1
    print(i)
    get_page(string, source)
    html = open(source, 'rb')
    soup = BeautifulSoup(html.read(), "html.parser")
    with open(filename, 'w+', encoding='utf-8') as result:
        result.write('<?xml version="1.0"?>\n<Cinema xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" ')
        result.write('xmlns:xsd="http://www.w3.org/2001/XMLSchema">\n')
        # ADDRESS
        address = soup.find('a', class_='address')
        address = '' if address is None else address.text
        print(address)
        result.write('<Address>' + address + '</Address>\n')
        # ID
        result.write('<Id>' + str(i) + '</Id>\n')
        # IMAGE_MAIN
        image_main = soup.find('div', class_='place-info_image')  #
        image_main = '' if image_main is None else image_main.find('img').get('src')  #
        print(image_main)
        result.write('<Image_Main>' + image_main + '</Image_Main>\n')
        # MORE IMAGE
        img_more = soup.find_all('td', class_='gs-slide')
        image = '<Images>\n'
        if img_more.__len__() == 0:
            result.write(image)
            result.write(' ')
        else:
            for a in img_more:
                image += a.find('a').get('href') + ' '
            print(image)
            result.write(image)
        result.write('</Images>\n')
        # INFO
        info = soup.find('div', class_='hidden js-cut_block active')
        if info is None:
            info_res = ''
        else:
            info = soup.find_all('p')
            info_res = ''
            for a in info:
                info_res += a.text + "\n"
        print(info_res)
        result.write('<Info>' + info_res + '</Info>\n')
        # LITTLE INFO
        little_info = soup.find('ul', class_='b-vlist')
        if little_info is None:
            little_info = ''
        else:
            li = little_info.find_all('li')
            little_info = ''
            for a in li:
                little_info += a.text + "\n"
        print(little_info)
        result.write('<Info_Little>' + little_info + '</Info_Little>\n')
        # NAME
        name = soup.find('span', itemprop='name')  #
        name = '' if name is None else name.text  #
        print(name)
        result.write('<Name>' + name + '</Name>\n')
        # SCHEDULE
        schedule = soup.find('li', class_='schedule')
        schedule = '' if schedule is None else schedule.text
        print(schedule)
        result.write('<Schedule>' + schedule + '</Schedule>\n')
        # TELEPHONE
        telephone = soup.find('p', itemprop='telephone')
        telephone = '' if telephone is None else telephone.text
        print(telephone)
        result.write('<Telephone>' + telephone + '</Telephone>\n')
        result.write('</Cinema>')


i = 0


def main():
    filename = 'out1.html'
    get_page('https://afisha.tut.by/places/cinema', filename)
    html = open(filename, 'rb')
    soup = BeautifulSoup(html.read(), "html.parser")
    get_href(soup)
    get_page('https://afisha.tut.by/places/cinema/2', filename)
    html = open(filename, 'rb')
    soup = BeautifulSoup(html.read(), "html.parser")
    get_href(soup)


if __name__ == '__main__':
    main()
