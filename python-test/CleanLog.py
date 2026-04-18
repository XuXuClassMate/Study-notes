# -*- coding: utf-8 -*-
import os
import MySQLdb

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def cleanLogs(startDate):
    conn=MySQLdb.connect(host="zk307",port=3306,user="root",passwd="esg67!#nkK",db="escheduler",charset="utf8")
    cursor=conn.cursor()
    sql = "SELECT log_path FROM t_escheduler_task_instance WHERE start_time<'%s'" % (startDate)
    n = cursor.execute(sql)
    count =0
    for row in cursor.fetchall():
        try:
            if row[0]!=None and os.path.exists(row[0]):
                count +=1
                print 'remove log path:' ,row[0]
                os.remove(row[0])
        except Exception,e:
           print e
    cursor.close()
    print 'clean log end! already clean %d logs' % (count)

if __name__=="__main__":
    if len(sys.argv) != 2:
        print "input the right argments: closing date(xxxx-xx-xx)"
    else:
        print "clean logs before:", sys.argv[1]
        cleanLogs(startDate=sys.argv[1])
