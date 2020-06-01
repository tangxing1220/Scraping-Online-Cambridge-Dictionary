import requests 
from bs4 import BeautifulSoup

guidURL = 'https://dictionary.cambridge.org/browse/english-chinese-simplified/'
guideURLs = []
extendURLs = []

def start(url, flag):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.0; WOW64; rv:24.0) Gecko/20100101 Firefox/24.0' }

    source_code = requests.get(url , headers=headers).text
    soup = BeautifulSoup(source_code, 'html.parser')
    #print(soup)

    #guide url
    if flag == 1 :
        for each_text in soup.findAll('a', {'class':'dil tcbd'}):
            #print(each_text)
            guideURLs.append(each_text.get('href'))  
    #extend url
    else:
       for each_text in soup.findAll('a', {'class': 'tc-bd'}):
            #print(each_text)  
            extendURLs.append(each_text.get('href'))
   
if __name__ == '__main__':
    #guide url
    for i in 'abcdefghijklmnopqrstuvwxyz':
        start(guidURL+i,1)
        print(i)
    print(guideURLs)
    print(len(guideURLs))

    #extend url
    for g in guideURLs:
        start(g, 2)
        print(g)
    print(extendURLs)
    print(len(extendURLs))

    #save all alphabets url
    fd = open('guideURLs.txt', 'w')
    for name in guideURLs:
        fd.write(name)
        fd.write('\n')
    fd.close()
    
    #save all words url
    fd = open('extendURLs.txt', 'w')
    for name in extendURLs:
        fd.write(name)
        fd.write('\n')
    fd.close()