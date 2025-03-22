def new_func1():
    # pip install requests
# pip install bs4
# pip install html5lib
# pip install lxml
        import requests # type: ignore
        from bs4 import BeautifulSoup # type: ignore

# How to get the HTML from a website
        website = 'https://subslikescript.com/movie/Titanic-120338'
        result = requests.get(website)
        content = result.text

        soup = BeautifulSoup(content, 'lxml')
        print(soup.prettify())

# How to scrape a single page
        box = soup.find('article', class_='main-article')

        title = soup.find('h1').get_text()
        print(title)

        transcript = box.find('div', class_='full-script').get_text(strip=True, separator='')
        print(transcript)

# Exporting data to a txt file
        with open(f'{title}.txt', 'w') as file:
            file.write(transcript)

    new_func() # type: ignore