import sqlite3
from collections import defaultdict

entries = {
  "CARS":[
     {
        "MAKE": "VW",
        "MODEL":"Passat",
        "COST":23000
     },
     {
        "MAKE":"Honda",
        "MODEL":"Civic"
     }
    ]
}



keys = ["MAKE", "MODEL", "COST"]
with sqlite3.connect("test.db") as conn:
    c = conn.cursor()
    #c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct} DEFAULT '{df}'" \
    #          .format(tn='cars', cn='COST2', ct='INT', df=None))
    for car in entries['CARS']:
        print(car.get('MAKE'))
        """
        # USE setdefault()
        for key in keys:
            car.setdefault(key, None)
        c.execute('INSERT INTO cars VALUES(?,?,?)', (car['MAKE'], car['MODEL'], car['COST']))

        """
        """
        # USE dict.get()

        c.execute('INSERT INTO cars VALUES(?,?,?)', (car.get('MAKE'), car.get('MODEL'), car.get('COST')))
        """


        # USE collections.defaultdict()

        for car in entries['CARS']:
            car = defaultdict(lambda: None, car)
            c.execute('INSERT INTO cars VALUES(:MAKE, :MODEL, :COST)', car)

    c.execute('SELECT * from cars')
    for row in c.fetchall():
        print(row)


