import sqlite3

connection = sqlite3.connect('not_telegram.db')
cursor = connection.cursor()
cursor.execute(''
               'CREATE TABLE IF NOT EXISTS Users ('
               'id INTEGER PRiMARY KEY,'
               'username TEXT NOT NULL,'
               'email TEXT NOT NULL,'
               'age INTEGER,'
               'balance INTEGER TEXT NOT NULL)''')

cursor.execute('CREATE INDEX IF NOT EXISTS idx_email ON Users (email)')

cursor.execute('DELETE FROM Users WHERE id = 6')
cursor.execute('SELECT COUNT(*) FROM Users')
result_1 = cursor.fetchone()[0]
print(result_1)
cursor.execute('SELECT SUM(balance) FROM Users')
result_2 = cursor.fetchone()[0]
print(result_2)
cursor.execute('SELECT AVG(balance) FROM Users')
result_3 = cursor.fetchone()[0]
print(result_3)
print(result_2 / result_1)


connection.commit()
connection.close()
