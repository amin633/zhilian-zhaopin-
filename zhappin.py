#coding:utf-8
import urllib2

def urlget(i):
    url = 'http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E5%8C%97%E4%BA%AC&kw=python&sm=0&p='
    pageurl = url + str(i)
    #print pageurl
    return pageurl

        
def zwxx(url):
    up = urllib2.urlopen(url)
    cont = up.read()
    head = '"font-weight: bold" href="'
    tail = '</a>'
    ph = -len(head)
    pt = -len(tail)
    zwxxlist = []
    zwmclist = []
    i = 0
    while i < cont.count(head):
        ph = cont.find(head,pt + len(tail))
        pt = cont.find(tail,ph)
        x = cont[ph:pt + len(tail)]
        phref = x.find("http")
        plager = x.find(">")
        zwxx = x[phref : plager - len('" target="_blank"')]
        zwmc = x[plager + 1 : len(x) - 4]
        zwxxlist.append(zwxx)
        zwmclist.append(zwmc)
        i += 1
    return zwxxlist,zwmclist



def gsmc(url):
    up = urllib2.urlopen(url)
    cont = up.read()
    head = '<td class="gsmc">'
    tail = '</td>'
    ph = -len(head)
    pt = -len(tail)
    gsmclist = []
    i = 0
    while i < cont.count(head):
        ph = cont.find(head,pt + len(tail))
        pt = cont.find(tail,ph)
        x = cont[ph:pt + len(tail)]
        phref = x.find('target="_blank">')
        plager = x.find('</a>')
        gsmc = x[phref + len('target="_blank">') : plager]
        gsmclist.append(gsmc)
        i += 1
    return gsmclist



def zwyx(url):
    up = urllib2.urlopen(url)
    cont = up.read()
    head = '<td class="zwyx">'
    tail = '</td>'
    ph = -len(head)
    pt = -len(tail)
    zwyxlist = []
    i = 0
    while i < cont.count(head):
        ph = cont.find(head,pt + len(tail))
        pt = cont.find(tail,ph)
        x = cont[ph:pt + len(tail)]
        phref = x.find('target="_blank">')
        plager = x.find('</a>')
        zwyx = x[phref + len('target="_blank">') : plager]
        zwyxlist.append(zwyx)
        i += 1
    return zwyxlist


def gzdd(url):
    up = urllib2.urlopen(url)
    cont = up.read()
    head = '<td class="gzdd">'
    tail = '</td>'
    ph = -len(head)
    pt = -len(tail)
    gzddlist = []
    i = 0
    while i < cont.count(head):
        ph = cont.find(head,pt + len(tail))
        pt = cont.find(tail,ph)
        x = cont[ph:pt + len(tail)]
        phref = x.find('target="_blank">')
        plager = x.find('</a>')
        gzdd = x[phref + len('target="_blank">') : plager]
        gzddlist.append(gzdd)
        i += 1
    return gzddlist

url = urlget(3)


a = zwxx(url)
b = gsmc(url)
c = zwyx(url)
d = gzdd(url)



fw = open('a.html','w')
htmlhead = '<html><head><meta charset="utf-8"></head><body><table>'
fw.write(htmlhead)
i = 0
while i < len(b):
    fw.write('<tr><td><a href = "%s">' % (a[0][i]))
    fw.write(a[1][i] + "</a></td><td>" + b[i] + "</td><td>" + c[i] + "</td><td>" + d[i] + "</td></tr>")
    i += 1
htmltail = '</table></body></html>'
fw.write(htmltail)
fw.close()
  
