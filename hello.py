import random
import requests
import json
from flask import Flask, escape, request, render_template

app = Flask(__name__)

@app.route('/')
def hello():
    name = request.args.get("name", "World")
    return f'Hello, {escape(name)}!'

@app.route('/myname')
def myname():
    return '김재관입니다'

# 랜덤으로 점심메뉴 추천해주는 서버
@app.route('/lunch')
# def 함수를 선언하는 키워드
# 함수를 설정하는 이유 : 반복해야 하는 긴 동작이나 행동을 짧게 정의해 반복하기 용이하도록 
def lunch():
    menus = ['양자강','김밥까페','20층','순남시래기','서브웨이']
    lunch = random.choice(menus)
    return lunch

# 아이돌 백과사전
@app.route('/idols')
def idol():
    idols = {
        '트와이스': {
            '모모': 24,
            '사나': 24,
            '나연': 25
        },
        '레드벨벳':{
            '조이': 24,
            '웬디': 26,
            '아이린': 29,
            '슬기': 26
        },
        '써니힐': '이젠 없어....복귀좀',
        '소녀시대': '소녀시대'
    }
    return idols

@app.route('/post/<int:num>')
def post(num):
    posts = ['0번 포스트', '1번 포스트', '2번 포스트']
    return posts[num]

# 실습 : 큐브 뒤에 전달된 수의 세제곱수를 화면에 표현해 주세요
# 1 > 1, 2 > 8, 3 > 27
# str() : 숫자를 문자로 바꿔주는 함수
@app.route('/cube/<int:num>')
def cube(num):
    cubed = num*num*num
    return str(cubed)

# 클라이언트에게 html 파일을 주고싶음.
@app.route('/html')
def html():
    return render_template('hello.html')


@app.route('/ping')
def ping():
    return render_template('ping.html')

@app.route('/pong')
def pong():
    age = request.args.get('age')
# age = request.args['age']
    return render_template('pong.html', age_in_html=age)

# 로또번호를 가져와서 보여주는 서버 만들기
@app.route('/lotto_result/<int:round>')
def lotto_result(round):
    url = f'https://www.nlotto.co.kr/common.do?method=getLottoNumber&drwNo={round}'
    result = requests.get(url).json()

    winner = []
    for i in range(1,7):
        # key에 대한 함수를 가져올 때는 .get을 필히 사용할 것.
        winner.append(result.get(f'drwtNo{i}'))
    
    winner.append(result.get('bnusNo'))

    return json.dumps(winner)

app.run(debug=True)
"""
# 함수 예
# lunch() =  menus = ['양자강','김밥까페','20층','순남시래기','서브웨이']
    lunch = random.choice(menus)
    return lunch
    """