import pymysql.cursors
import izyrtm_prop

def getConn():
    connection = pymysql.connect(host=izyrtm_prop.db_host,
        user=izyrtm_prop.db_user,
        password=izyrtm_prop.db_pw,
        db=izyrtm_prop.db_datadbase,
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor)
    return connection

def getBotList():
    conn = getConn()

    try:
        with conn.cursor() as cursor:
            #sql = 'SELECT * FROM tb_bot WHERE email = %s'
            sql = 'SELECT * FROM tb_bot'
            #cursor.execute(sql, ('test@test.com',))
            cursor.execute(sql)
            result = cursor.fetchall()
            #print(result)
            # (1, 'test@test.com', 'my-passwd')
            #print('select list start')
            for i in result:
                #   print(i)
                #seq_no,bot_key,bot_token,bot_type,bot_title,topic_name,user_list,use_yn,reg_dt,mod_dt
                #print(str(i['seq_no'])+' / '+str(i['bot_key'])+' / '+str(i['bot_token'])+' / '+str(i['bot_type'])+' / '+str(i['bot_title'])+' / '+str(i['topic_name'])+' / '+str(i['user_list'])+' / '+str(i['use_yn']))
                #print("\n")
            #print('select list end')
        return result
    finally:
        conn.close()


if __name__ == '__main__':
    getBotList()