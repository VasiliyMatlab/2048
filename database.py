import sqlite3

bd = sqlite3.connect("2048.sqlite")

cursor = bd.cursor()
cursor.execute('''
create table if not exists RECORDS (
    name text,
    score integer
)
''')

# Записать результат в базу данных
def insert_result(name: str, score: int):
    cursor.execute('''
        insert into RECORDS values (?, ?)
    ''', (name, score))
    bd.commit()

# Выдать 3 лучших результата неповторяющихся игроков из базы данных
def get_best():
    cursor.execute('''
    SELECT name, max(score) score from RECORDS
    GROUP by name
    ORDER by score DESC
    limit 3
    ''')
    return cursor.fetchall()