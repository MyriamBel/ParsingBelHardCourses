#/usr/bin/python3
# -*- coding: utf-8 -*-
"""1. Дан список телефонных номеров в произвольном формате.
Преобразовать номера в формат +375 (17) 222-22-22 с помощью pyparsing
2. Дан список телефонных номеров в произвольном формате.
Преобразовать номера в формат +375 (17) 222-22-22 с помощью регулярных выражений
3. Распарсить страницу https://docs.python.org/3/library/index.html.
Извлечь оглавление в удобочитаемом виде.
4. Распарсить страницу http://www.tc.belhard.com/courses/courses2.php.
Извлечь все ссылки на описания курсов.
Пройти по каждой ссылке и извлечь оглавление каждого курса.
Примечание от разработчика: сайт по указанной ссылке был недоступен, вместо него взят сайт
https://www.belhard.com/ru/education/itacademy
"""

#def formatphonenumber(string):
#    import re
#    pattern0 = r'\d'
#    alld = re.findall(pattern0, string)
#    if len(alld) != 7:
#        return 'Номер телефона должен состоять из 7 цифр'
#    else:
#        summary = ''
#        for i in alld:
#            summary += i
#            if len(summary) == 3 or len(summary) == 6:
#                summary += '-'
#    #pattern1 = r'[0-9]{3}-[0-9]{2}-[0-9]{2}'
#        return '+375(17)' + summary
#while True:
#    print(formatphonenumber(input()))
'''
def phonenumberpyparsing(string):
    import pyparsing
    pattern = pyparsing.Word(pyparsing.nums)
    listd = []
    for data, start, end in pattern.scanString(string):
        listd.append(data[0])
    summary = ''
    for i in listd:
        for j in i:
            summary += j
            if len(summary) == 3 or len(summary) == 6:
                summary += '-'
    if len(summary) != 9:
        return 'Номер телефона должен состоять из 7 цифр'
    else:
        return '+375(17)' + summary
while True:
    print(phonenumberpyparsing(input()))'''
'''
def pageparsing():
    from urllib.request import urlopen
    from bs4 import BeautifulSoup

    url = 'https://docs.python.org/3/library/index.html'
    page = urlopen(url)

    bsObj = BeautifulSoup(page.read(), "html.parser")

    listOfli = bsObj.find('div', {'class': 'toctree-wrapper compound'}).find_all('a')

    for i in listOfli:
        print(i.text)
pageparsing()
'''

def getlinks():
    from urllib.request import urlopen
    from bs4 import BeautifulSoup
    import re
    url = 'https://www.belhard.com/ru/education/itacademy'
    page = urlopen(url)

    bsObj = BeautifulSoup(page.read(), "html.parser")

    listOfCoursesContainer = bsObj.find('div', {'id': "page"}) #получили контейнер с ссылками на курсы

    alllists = listOfCoursesContainer.findAll('a', href=re.compile("^(/ru/component/)(.*)\w+$")) #Получаем все элементы списка li
    listofafref = []
    for i in alllists:
        listofafref.append(i.get('href'))
    return listofafref

def geth1(url):
    from urllib.request import urlopen
    from bs4 import BeautifulSoup
    url = 'https://www.belhard.com' + url
    page = urlopen(url)
    bsObj = BeautifulSoup(page.read(), 'html.parser')
    textofprogram =bsObj.find('div', {'id': 'page'}).find_all('p')
    with open('parsing.txt', 'a') as f:
        f.write('Parsed URL:'+'\n')
        f.write(url+'\n')
        for i in textofprogram:
            f.write(i.text + '\n')
        f.write('-----------------------------------------' + '\n')

geturls = getlinks()
for i in geturls:
    geth1(i)