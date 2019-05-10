import pymysql.cursors

conn = pymysql.connect(host='localhost',
                       user='root',
                       password="5874",
                       db='test',
                       charset='utf8mb4')

try:
    with conn.cursor() as cursor:
        sql = 'SELECT * FROM users WHERE email = %s'
        cursor.execute(sql, ('test@test.com',))
        result = cursor.fetchone()
        print(result)
        # (1, 'test@test.com', 'my-passwd')
finally:
    conn.close()


con = pymysql.connect(host="localhost",user = "root",password = "5874", db="test",charset="utf8mb4")

try:
    with con.cursor() as cursor:
        sqll = 'SELECT * FROM users WHERE email=%s'
        cursor.execute(sqll)
        result = cursor.fetchone()
        print(re)