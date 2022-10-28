import pymysql
db= pymysql.Connect(host='localhost' , user='root' , password='', db='db_sma2')
cursor =db.cursor()
print("mengurutkan data akun dari followers terbanyak ")
cursor.execute("select*from tbl_scraping ORDER BY follower_count desc  " )
dt= cursor.fetchall()
for d in dt:
  print(d)

print("mengurutkan data akun dari followers paling sedikit ")
cursor.execute("select*from tbl_scraping ORDER BY follower_count asc   " )
dat= cursor.fetchall()
for dta in dat :
  print(dta)
  