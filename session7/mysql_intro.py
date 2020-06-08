import pymysql

client = pymysql.connect(
  host='localhost',
  user='root',
  password='@gmail.com'
)

cursor = client.cursor()

# cursor.execute('CREATE DATABASE d4e12')

cursor.execute(
  '''
    CREATE TABLE IF NOT EXISTS d4e12.cake (
    name VARCHAR(255) PRIMARY KEY,
    calor_rate INT(11)
  )
  '''
)

cursor.execute( 
  '''
     CREATE TABLE IF NOT EXISTS d4e12.ingredient ( 
      name VARCHAR(255) PRIMARY KEY,
      cake_name VARCHAR(255) UNIQUE REFERENCES d4e12.cake(name)
    )
  '''
)

cake_name = 'otga'

cursor.execute( # string formating
  f'''
    INSERT INTO d4e12.cake(name, calor_rate)
    VALUES ('{cake_name}', 3000), ('agto', 6000)
  '''
)


client.commit()