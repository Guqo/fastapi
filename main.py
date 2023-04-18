from fastapi import FastAPI
from pydantic import BaseModel
import json

from scraper import Scraper

app = FastAPI()
s = Scraper()
s.scrapedata()


class Item(BaseModel):
    title: str
    year: int
    link: str


@app.get('/')
async def root():
    return {'message': 'Film Database'}


@app.get('/films')
async def read_items():
    j = open('data.json', 'r')
    data = json.load(j)
    j.close()
    return data


@app.get('/films/{item_id}')
async def read_item(item_id: int):
    j = open('data.json', 'r')
    data = json.load(j)
    j.close()
    return data[int(item_id)]


@app.post('/films/')
async def add_item(item: Item):
    j = open('data.json', 'r')
    data = json.load(j)
    data.append(dict(item))
    j.close()

    j = open('data.json', 'w')
    j.write(json.dumps(data))
    j.close()
    return item


@app.patch('/films/{item_id}')
async def update_item(item_id: int, item: Item):
    j = open('data.json', 'r')
    data = json.load(j)
    data[item_id]['title'] = item.title
    data[item_id]['year'] = item.year
    data[item_id]['link'] = item.link
    j.close()

    j = open('data.json', 'w')
    j.write(json.dumps(data))
    j.close()
    return item


@app.delete('/films/{item_id}')
async def delete_item(item_id: int):
    j = open('data.json', 'r')
    data = json.load(j)
    data.pop(item_id)
    j.close()

    j = open('data.json', 'w')
    j.write(json.dumps(data))
    j.close()
    return {'message': f'Deleted film with id {item_id}'}
