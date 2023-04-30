''' RUN THIS FILE TO CREATE DUMMY USERS'''



import sqlite3


user=''
password=''
cursor=''

create = '''
            create table if not exists User(
            name TEXT,
            password TEXT,
            access TEXT);
        '''

insert =  f"insert into User values('ankit','pass','admin')"

read = f"select access from User where name='{user}', 'password={password}'"

delete = f"delete from User where name='{user}', 'password={password}'"


try:
    file = "user.sqlite"

    sqliteConnection = sqlite3.connect(file)
    if sqliteConnection:
        cursor = sqliteConnection.cursor()
        cursor.execute(create)

        cursor.execute(insert)
        

except sqlite3.Error as error:
    print(error)
