import requests
import pymysql
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:67.0) Gecko/20100101 Firefox/67.0', }
extendURLs = []
vocabulary = {}

def translate(url):
#    print(url)
    source_code = requests.get(url , headers=headers).text
    soup = BeautifulSoup(source_code, 'html.parser')
#    print(soup)

    try: 
        word_crab = soup.find('span', attrs={'class': 'headword'}).getText()
    except:
        word_crab = soup.find('h2', attrs={'class': 'headword'}).getText()
#    finally:
#        source_code = requests.get(url , headers=headers).text
#        soup = BeautifulSoup(source_code, 'html.parser')
#        try:
#            word_crab = soup.find('span', attrs={'class': 'headword'}).getText()
#        except:
#            word_crab = soup.find('h2', attrs={'class': 'headword'}).getText()

    fd.write(f'{word_crab} : ')
    print(word_crab)

    if word_crab == 'yah':
        print(soup)

    translation_all = soup.find_all('div', attrs={'class':'ddef_h'})
#    print(translation_all)
#   translation_all_temp = soup.find_all('span', attrs={'class':'trans dttrans dtrans-se'})
#   print(translation_all_temp)
#    if word_crab == 'zany':
#        print(translation_all)

    detail_list = list()
    for translation in translation_all:
        detail = translation.getText()
#        try:
        fd.write(f'{detail}, ')
#        except:
#            print('error')
#            fd.write(f"error, ")
        detail_list.append(detail)
#        detail_list_to_str = ';'.join(detail_list)
#    vocabulary[word_crab] = detail_list
    fd.write('\n')

 #   sql = """
 #   insert into words(id,word,meaning) values (null,%s,%s)
    """

    word = word_crab
    meaning = detail_list_to_str
#    try:
    cursor.execute(sql,(word,meaning))
#    except:
#        meaning1_en = 'error'
#        cursor.execute(sql,(word,meaning1_en))

    conn.commit()
"""
if __name__ == '__main__':
    conn = pymysql.connect(
            host='localhost',
            user='root',
            password='root',
            database='vocabulary',
            port=3306
            )
    cursor = conn.cursor()
   

#    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    alphabet = ['y','z']
    for letter in alphabet:
#        print(f"start at: {letter}")
        fd = open('extendURL_' + letter + '.txt', 'r')
        contents = fd.readlines()
        fd.close()
        extendURLs.clear()
        for name in contents:
            name = name.strip('\n')
            extendURLs.append(name)

        fd = open('vocabulary_' + letter + '.csv', 'w', encoding='utf-8')


        for wordURL in extendURLs:
            fd.write(f'{wordURL} : ')
            translate(wordURL) 
        
        fd.close()

#        print(f"end at: {letter}")

#    conn.close()