from requests_html import HTMLSession
import json


class Scraper:
    def scrapedata(self):
        url = f'https://www.csfd.cz/zebricky/filmy/nejlepsi/'
        s = HTMLSession()
        r = s.get(url)

        data = r.html.find('div.article-content')

        dlist = []

        for d in data:
            item = {
                'title': d.find('a.film-title-name', first=True).text,
                'year': int(d.find('span.film-title-info', first=True).text[1:-1]),
                'link': list(d.find('a.film-title-name', first=True).absolute_links)[0]
            }
            dlist.append(item)

        j = open('data.json', 'w')
        j.write(json.dumps(dlist))
        j.close()
