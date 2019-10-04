import pymysql.cursors

conn = pymysql.connect(host='monbot.hopto.org',
        user='izyrtm',
        password='new1234!',
        db='monbot',
        charset='utf8mb4')

try:
    with conn.cursor() as cursor:
        sql = 'SELECT * FROM tb_bot'
        cursor.execute(sql)
        result = cursor.fetchone()
        print(result)
        
finally:
    conn.close()
