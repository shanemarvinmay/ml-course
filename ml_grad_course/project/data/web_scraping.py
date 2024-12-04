books = ['Genesis', 'Exodus', 'Leviticus', 'Numbers', 'Deuteronomy', 'Joshua', 'Judges', 'Ruth', '1 Samuel', '2 Samuel', '1 Kings', '2 Kings', '1 Chronicles', '2 Chronicles', 'Ezra', 'Nehemiah', 'Esther', 'Job', 'Psalms', 'Proverbs', 'Ecclesiastes', 'Song', 'of', 'Solomon', 'Isaiah', 'Jeremiah', 'Lamentations', 'Ezekiel', 'Daniel', 'Hosea', 'Joel', 'Amos', 'Obadiah', 'Jonah', 'Micah', 'Nahum', 'Habakkuk', 'Zephaniah', 'Haggai', 'Zechariah', 'Malachi', 'Matthew', 'Mark', 'Luke', 'John', 'Acts', 'Romans', '1 Corinthians', '2 Corinthians', 'Galatians', 'Ephesians', 'Philippians', 'Colossians', '1 Thessalonians', '2 Thessalonians', '1 Timothy', '2 Timothy', 'Titus', 'Philemon', 'Hebrews', 'James', '1 Peter', '2 Peter', '1 John', '2 John', '3 John', 'Jude', 'Revelation']
# books_set = set()
# for book in books:
#     books_set.add(book)
# https://www.sacred-texts.com/bib/wb/esp/gen.htm
# https://www.sacred-texts.com/bib/wb/esp/
book_links = []
import requests
from bs4 import BeautifulSoup

URL = "https://www.sacred-texts.com/bib/wb/esp/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

links = soup.find_all("a")
for link in links:
    for book in books:
        if book in link:
            book_url = URL + link['href']
            book_links.append(book_url)
            # print(book_url)

Bible = ''
for book_link in book_links:
    print(book_link)
    page = requests.get(book_link)
    soup = BeautifulSoup(page.content, "html.parser")
    ps = soup.find_all('p')
    for p in ps:
        # print(p)
        a = p.find('a')
        verse_num = a.text
        # print(a)
        # print(p.text)
        verse = p.text
        # print(len(verse))
        verse = verse.replace("&nbsp;", "")
        verse = verse.replace(chr(160), "")
        for i in range(len(verse) - 1):
            if ord(verse[i]) == 160:
                # print('point reached', chr(160), '!')
                verse = verse[:i] + verse[i+1:]
        # print(len(verse))
        Bible += p.text + '\n'

with open("project/data/esperanto/Biblio.txt", "w", encoding="utf-8") as f:
    f.write(Bible)