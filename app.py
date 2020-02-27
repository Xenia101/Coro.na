from flask import Flask, render_template
from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests
import json

import urllib.request
import urllib.parse

headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:65.0) Gecko/20100101 Firefox/65.0'}

app = Flask(__name__)
app.debug = True
@app.route("/")
def home():
    return render_template('index.html', data=GetTotalCount())

def GetTotalCount():
    URL = "http://ncov.mohw.go.kr/bdBoardList_Real.do?brdId=1&brdGubun=11&ncvContSeq=&contSeq=&board_id=&gubun="
    res = requests.get(URL,headers=headers)
    soup = BeautifulSoup(res.content, 'html.parser')
    data = soup.select('.w_bold')[0:4]
    #data = soup.select('.s_listin_dot > li')[0:4]
    result = list()
    for x in data:
        result.append(x.get_text().replace(',','').replace('명', ''))
    data = [
        {'name' : '확진자'   , 'tag' : 'danger'  , 'count' : result[0]},
        {'name' : '사망자'   , 'tag' : 'dark'    , 'count' : result[2]},
        {'name' : '검사진행' , 'tag' : 'warning' , 'count' : result[3]},
        {'name' : '격리해제' , 'tag' : 'primary' , 'count' : result[1]}]
    return data

def GetLocCount():
    URL = "http://ncov.mohw.go.kr/bdBoardList_Real.do?brdId=1&brdGubun=13&ncvContSeq=&contSeq=&board_id=&gubun="
    res = requests.get(URL,headers=headers)
    soup = BeautifulSoup(res.content, 'html.parser')
    table = soup.find('table', attrs={'class':'num'})
    table_body = table.find('tbody')

    location = list()
    count = list()
    rows = table_body.find_all('tr')
    for row in rows:
        loc = row.find_all('th')
        loc = [ele.text.strip() for ele in loc]
        location.append(loc[0])
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        count.append(int(cols[0].replace(',','')))
    location = location[1:-1]
    count    = count[1:-1]
    data = dict(zip(location, count))
    return data

def geoCoding(getData):
    data = {
        "positions" : []
        }

    print(data)
    print(getData)


if __name__ == "__main__":
    geoCoding(GetLocCount())
    app.run(host="localhost", port=8080, use_reloader=False)
