import requests
import pymysql
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:67.0) Gecko/20100101 Firefox/67.0', }
extendURLs = []
vocabulary = {}

def translate(url):
    source_code = requests.get(url , headers=headers).text
    soup = BeautifulSoup(source_code, 'html.parser')
#    print(soup)

    try:
        word_crab = soup.find('span', attrs={'class': 'headword'}).getText()
    except:
        word_crab = soup.find('h2', attrs={'class': 'headword'}).getText()

    print(word_crab)


    translation_all = soup.find_all('div', attrs={'class':'ddef_h'})

    translation_all_temp = soup.find_all('div', attrs={'class':'def-body ddef_b'} )
#    translation_all_temp = soup.find_all('div', attrs={'span':'def-body ddef_b'})
#    translation_all_temp_1 = translation_all_temp.find('span',attrs={'class':'trans dtrans dtrans-se'})
#    print(translation_all)
#    print('\n')
    print(translation_all_temp)
    detail_list_temp = list()
    for translation_temp in translation_all_temp:
        detail_temp = translation_temp.find('span',attrs={'class':'trans dtrans dtrans-se'}).getText()
        detail_list_temp.append(detail_temp)
        detail_list_to_str_temp = ';'.join(detail_list_temp)
    print(detail_list_to_str_temp)
    #vocabulary[word_crab] = detail_list


    detail_list = list()
    for translation in translation_all:
        detail = translation.getText()
        detail_list.append(detail)
        detail_list_to_str = ';'.join(detail_list)
    print(detail_list_to_str)
    #vocabulary[word_crab] = detail_list
    detail_combine = []

    for index in range(len(detail_list)):
        detail_combine.append(detail_list[index])
        detail_combine.append(detail_list_temp[index])
        detail_combine.append(';')
    print(detail_combine)

    detail_combine_to_str = ' '.join(detail_combine)


    sql = """
    insert into words(id,word,meaning) values (null,%s,%s)
    """

    word = word_crab
    meaning = detail_combine_to_str
#    try:
    cursor.execute(sql,(word,meaning))
#    except:
#        meaning1_en = 'error'
#        cursor.execute(sql,(word,meaning1_en))

    conn.commit()

if __name__ == '__main__':
    conn = pymysql.connect(
            host='localhost',
            user='root',
            password='root',
            database='vocabulary',
            port=3306
            )
    cursor = conn.cursor()
    """
#    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    alphabet = ['t','u','v','w','x','y','z']
    for letter in alphabet:
#        print(f"start at: {letter}")
        fd = open('extendURL_' + letter + '.txt', 'r')
        contents = fd.readlines()
        fd.close()
        extendURLs.clear()
        for name in contents:
            name = name.strip('\n')
            extendURLs.append(name)

        for wordURL in extendURLs:

            translate(wordURL) 
        
#        fd.close()

#        print(f"end at: {letter}")

    conn.close()
    """
    wordURL='https://dictionary.cambridge.org/dictionary/english-chinese-traditional/taxi'
    translate(wordURL) 
    conn.close()