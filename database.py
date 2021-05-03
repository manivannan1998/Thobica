import sqlite3


# connect to the sqlite3
db = sqlite3.connect('Registration')
# created cursor from database Registration
 rs = db.cursor()

# create table name and password in varchar
# rs.execute('''create table Register(name varchar(50), email varchar(10), passwd(10))''')
# db.commit()

# add data intavle
rs.execute('''insert into Register values('moni', '@gmail.com', 'moni1234#')''')
db.commit()

rs.execute('select * from Register')
for i in rs:
    print(i)
