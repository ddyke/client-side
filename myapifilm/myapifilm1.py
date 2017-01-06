import requests, json, sqlite3
from collections import defaultdict


TOKEN = 'your token'
url = requests.get('http://api.myapifilms.com/imdb/inTheaters?token={}&format=json&language=en-us'.format(TOKEN))

binary = url.content

output = json.loads(str(binary, 'utf-8'))


movies = output['data']['inTheaters']

names = ["title", "year", "votes", "releasedate", "metascore", "rating"]
with sqlite3.connect('movies.db') as conn:
    c = conn.cursor()

    for movie in movies:
        all_movies = movie['movies']
        for meta in all_movies:
            meta = defaultdict(lambda: None, meta)
            if (meta['title']):
                c.execute("INSERT INTO new_movies VALUES(?, ?, ?, ?, ?, ?)",
                          (meta["title"], meta["year"], meta["votes"],
                           meta["releaseDate"], meta["metascore"],
                           meta["rating"]))
        c.execute('SELECT * FROM new_movies ORDER BY title ASC')

    rows = c.fetchall()

    for r in rows:
        print(r[0], r[1], r[2], r[3], r[4], r[5])


