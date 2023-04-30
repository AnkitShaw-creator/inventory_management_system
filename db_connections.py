import sqlite3

file = "user.sqlite"

user=''
password=''
cursor=''

create = '''
            create table if not exists User(
            name TEXT,
            password TEXT,
            access TEXT);
        '''

insert =  f"insert into User values('{user}','{password}',admin)"



try:
    sqliteConnection = sqlite3.connect(file)
    if sqliteConnection:
        cursor = sqliteConnection.cursor()
        cursor.execute(create)
        

except sqlite3.Error as error:
    print(error)



def check_user(u, p):
    user = u
    password = p

    read = f"select access from User where name='{user}', 'password={password}'"

    cursor.execute(read)
    result = cursor.fetchall()
    if "admin" in result:
        return True
    
    return False

def delete_user(u,p):
    user = u
    password = p

    delete = f"delete from User where name='{user}', 'password={password}'"

    cursor.execute(delete)

    read = f"select access from User where name='{user}', 'password={password}'"

    cursor.execute(read)
    result = cursor.fetchall()
    if "admin" in result:
        return True
    
    return False