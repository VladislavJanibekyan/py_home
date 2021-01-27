import sqlite3
import os
from sqlite3 import Error
import json
database = os.path.join(os.getcwd(), "film.db")
print(database)
try:
    conn = sqlite3.connect(database)
except Error as e:
    print(e)
curs = conn.cursor()
curs.execute("SELECT {} FROM {} WHERE {} like 'B%'".format("title","film","title"))
conn.commit()
print(curs.fetchall())

curs.execute("SELECT * FROM {} ORDER BY {} desc ".format("film", "length"))
conn.commit()
a = curs.fetchall()[0]
print(f"\nthe longest movie is {a[1]} duration is {a[5]} mins.")
dic_data = {}
end_list = []
list_data = ["film_id", "title", "description", "release_year", "rate", "length", "special_features"]
db_json = '''SELECT *
            FROM film 
           '''
curs.execute(db_json)
conn.commit()
json_a = curs.fetchall()
for i in json_a:
    count = 0
    for j in i:
        dic_data[list_data[count]] = j
        count += 1
    end_list.append(dic_data) 


with open("db_json.json", "w") as file:
    json.dump(end_list, file, indent=2)



#### EXTRA ####
new_tab = """CREATE TABLE IF NOT EXISTS filtered_film(
                                                film_id integer,
                                                title text,
                                                description text,
                                                release_year integer,
                                                rate real,
                                                length integer,
                                                special_features text
                                                );
             """
curs.execute(new_tab)
conn.commit()
new_tab = ''' INSERT INTO filtered_film
                SELECT *
                FROM film
                WHERE release_year > 2010 AND (rate between 3 
                                                        AND 5)
                '''
curs.execute(new_tab)
conn.commit()





















