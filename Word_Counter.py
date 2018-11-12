import requests
from bs4 import BeautifulSoup
import operator


def search(url):
    list = []
    data = requests.get(url).text
    soup = BeautifulSoup(data,'lxml')
    for postedtext in soup.findAll('a', {'class': 'news-info'}):
        plaintext = postedtext.string
        words = plaintext.lower().split()
        for eachtext in words:
            print(eachtext)
            list.append(eachtext)
    clean_up_words(list)
    

def clean_up_words(list):
    cleaned_up_list = []
    for word in list:
        symbols = "!@#$^&*())_+=][\';/.,><?'"
        for w in range(0, len(symbols)):
            word = word.replace(symbols[w], "")
        if len(word) > 0:
            print(word)
            cleaned_up_list.append(word)
    dictionary(cleaned_up_list)


def dictionary(cleaned_up_list):
    words_list = {}
    for word in cleaned_up_list:
        if word in words_list:
            word_list[word] += 1
        else:
            word_list[word] = 1
    for key, value in sorted(words_list.items(), key=operator.itemgetter(1)):
        print(key,value)

#To test this out
search('https://www.thenetnaija.com/news')
