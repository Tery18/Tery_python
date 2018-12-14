# encoding: utf-8
import cx_Oracle
def get_rows(begindt,enddt) :
   # conn =  cx_Oracle.connect('HEX_SPCC/HEX_SPCC88@172.170.2.88:1521/HEXDB')
    conn = cx_Oracle.connect('scott/tiger@192.168.1.148:1521/HEXDB')
   # print (conn.version)
    cursorobj =  conn.cursor()
    sql = "select  count(*)  from  stk_chkstk  where   TO_CHAR(UPDDT,'yyyymmdd') between  :begindt   and   :enddt"
    cursorobj.parse(sql)
    cursorobj.execute(sql,[begindt,enddt])
    s = (cursorobj.fetchone()[0])
    cursorobj.close()
    conn.close()
    return  s

