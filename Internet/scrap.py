import requests
from bs4 import BeautifulSoup
from time import sleep
import random

class Book:

    def __init__(self, title, author, rating):
        self.title = title
        self.author = author
        self.rating = rating[:rating.index(' avg')].strip()

    def __str__(self):
        return f"{self.title}|{self.author}|{self.rating}"

books = []
errors = []
user_agents_list = [
    'Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.83 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'
]

base_url = "https://www.goodreads.com"
end_point = "/list/show/7.Best_Books_of_the_21st_Century"

n_pages = [i for i in range(1,4)]

for n_page in n_pages:
    print(f"Current Progress = page {n_page}")
    sleep(random.randint(1,3))

    params = f"?page={n_page}"

    header = {'User-Agent' : random.choice(user_agents_list)}

    response = requests.get(base_url + end_point + params, headers = header)

    if not response:
        error = f"Request failed {base_url + end_point + params}, code = {response.status_code}"
        errors.append(error)
        print(error)
        continue

    page = response.text
    soup = BeautifulSoup(page, 'html.parser')
    main_content = soup.find('div', class_='mainContent')
    left_container = main_content.find('div', class_='leftContainer')
    all_votes = left_container.find('div', id = 'all_votes')

    book_list = all_votes.find_all('tr', {"itemtype" : "http://schema.org/Book"})

    for book in book_list:
        title = book.find('a', class_ = "bookTitle")
        book_title = title.find('span').text.strip()

        author = book.find('a', class_="authorName")
        book_author = author.find('span').text.strip()

        book_rating = book.find('span', class_ = 'minirating').text.strip()

        books.append(Book(book_title, book_author, book_rating))

with open('books.csv', 'wt', encoding='utf-8') as f:
    f.write("Title|Author|Rating\n")
    for book in books:
        f.write(f"{str(book)}\n")

print(errors)