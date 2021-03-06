import urllib.request
import threading
from time import ctime
from bs4 import BeautifulSoup
def getPM25(cityname):
    site ='http://www.pm25.com/'+cityname+'.html'
    html=urllib.request.urlopen(site)
    soup=BeautifulSoup(html.read(),'lxml')

    city=soup.find(class_='bi_loaction_city')
    aqi=soup.find("a",{"class","bi_aqiarea_num"})
    quality=soup.select(".bi_aqiarea_right span")
    result=soup.find("div",class_='bi_aqiarea_bottom')
    
    print (city.text + u'AQI:'+aqi.text + u'\n质量:' + quality[0].text+result.text)
    print ('*'*20+ctime()+"*"*20)
def one_thread():#单线程
    print ('One_thread Start:'+ctime()+'\n')
    getPM25('wuhan')
    getPM25('hengyang')
def two_thread():#多线程
    print ('Two_thread Start:'+ctime()+'\n')
    threads=[]
    t1=threading.Thread(target=getPM25,args=('wuhan',))
    threads.append(t1)
    t2=threading.Thread(target=getPM25,args=('hengyang',))
    threads.append(t2)

    for t in threads:
        t.start()
if __name__=='__main__':
    one_thread()
    print('\n'*2)
    two_thread()
    
