from db import conn, cur

def get_meanings(word):
    query = f"SELECT meaning FROM dictionary WHERE expression='{word.lower()}'"
    print(query)
    cur.execute(query)
    conn.commit()
    meanings =  cur.fetchone()
    if meanings:
        meanings = meanings[0].replace('{','').replace('}','').split(',')
    return meanings

if __name__=="__main__":
    meanings = get_meanings("advantage")
    meanings = meanings[0].replace('{','').replace('}','').split(',')
    print(type(meanings))

