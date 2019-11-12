import json
from difflib import get_close_matches
from psycopg2 import connect

with open("data.json") as file, open("db_config.json") as config_file:
    data = json.load(file)
    credential = json.load(config_file)
    conn = connect(**credential)
    cur = conn.cursor()



if __name__=="__main__":
    print(data['advantage'])

    # Select query
    cur.execute("select * from dictionary where expression='advantage'")
    conn.commit()

    result = cur.fetchall()
    meanings = result[0][1].replace('{','').replace('}','').split(',')

    for meaning in meanings:
        print(meaning)
