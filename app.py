from flask import Flask, render_template
from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)

@app.route("/")
def home():
    data = api()
    return render_template('index.html', data=data)

def api():
    URL = "http://ncov.mohw.go.kr/bdBoardList_Real.do?brdId=1&brdGubun=11&ncvContSeq=&contSeq=&board_id=&gubun="
    html = urlopen(URL)
    res = requests.get(URL)
    soup = BeautifulSoup(res.content, 'html.parser')
    data = soup.select('.s_listin_dot > li')[0:4]
    result = list()
    for x in data:
        result.append(x.get_text().replace(',','').split(' ')[-1].replace('명', ''))
    data = [
        {'name' : '확진자'   , 'tag' : 'danger'  , 'count' : result[0]},
        {'name' : '사망자'   , 'tag' : 'dark'    , 'count' : result[2]},
        {'name' : '검사진행' , 'tag' : 'warning' , 'count' : result[3]},
        {'name' : '격리해제' , 'tag' : 'primary' , 'count' : result[1]}]

    return data

if __name__ == "__main__":
    app.run(host="localhost", port=8080)
