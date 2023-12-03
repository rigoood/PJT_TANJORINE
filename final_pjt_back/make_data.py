import sqlite3
import random
import json
from collections import OrderedDict

first_name_samples = "김이박최정강조윤장임"
middle_name_samples = "민서예지도하주윤채현지"
last_name_samples = "준윤우원호후서연아은진"
id_sample = 'ABCDEFGHIJKLMNOPQRSTYVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
email_code = ['gmail.com', 'naver.com', 'nate.com', 'daum.net', 'hanmail.net', 'kakao.com']
financial_products = []

con = sqlite3.connect('db.sqlite3')
cur = con.cursor()

def random_name():
    result = ""
    result += random.choice(first_name_samples)
    result += random.choice(middle_name_samples)
    result += random.choice(last_name_samples)
    return result

def random_email():
    result = ""
    result += random.choice(id_sample)
    result += random.choice(id_sample)
    result += random.choice(id_sample)
    result += random.choice(id_sample)
    result += '@'
    result += random.choice(email_code)
    return result

def deposit_list():
    print('Ddone')
    global financial_products
    cur.execute('SELECT id, fin_co_no, fin_prdt_cd from products_depositproduct')
    result = cur.fetchall()

    for row in result:
        cur.execute(f'SELECT id FROM products_depositoption WHERE product_id = {row[0]}')
        opresult = cur.fetchall()
        financial_products.append(f'D/${row[1]}/${row[2]}/${random.choice(opresult)[0]}')

def saving_list():
    print('Sdone')
    global financial_products
    cur.execute('select id, fin_co_no, fin_prdt_cd from products_savingproduct')
    result = cur.fetchall()

    for row in result:
        cur.execute(f'SELECT id FROM products_savingoption WHERE product_id = {row[0]}')
        opresult = cur.fetchall()        
        financial_products.append(f'S/${row[1]}/${row[2]}/${random.choice(opresult)[0]}')

def randon_birth():
    year = str(random.randint(1960, 2000))
    month = str(random.randint(1, 12))
    day = str(random.randint(1, 30)) if month != '2' else str(random.randint(1, 28))
    return year + '-' + month + '-' + day
# json 파일 만들기

file = OrderedDict()

username_list = []
email_list = []
N = 10000
i = 0
deposit_list()
saving_list()


while i < N:
    rn = random_name()
    re = random_email()
    if (re in email_list):
        continue

    username_list.append(rn)
    email_list.append(re)
    i += 1

    
# 저장 위치는 프로젝트 구조에 맞게 수정합니다.
save_dir = '../user_data.json'
with open(save_dir, 'w', encoding="utf-8") as f:
    f.write('[')
    
    for i in range(N):
        print(i)
        # 랜덤한 데이터를 삽입
        file["model"] = "accounts.User"
        file["pk"] = i+1
        file["fields"] = {
            'email': email_list[i],
            'username': username_list[i],  # 유저 이름 랜덤 생성
            'password': "qwerqwer",
            'birth': randon_birth(),  # 나이
            'phone': '',
            'address': '',
            'products': ','.join([random.choice(financial_products) for _ in range(random.randint(0, 5))]), # 금융 상품 리스트
            'money': random.randrange(0, 1500000000, 1000000),    # 현재 가진 금액
            'salary': random.randrange(0, 100000000, 1000000), # 연봉
            'married': random.choice([True, False]),
            'main_bank': "",
            'save_type': random.randint(1, 4),
            'is_active': True,
            'is_staff': False,
            'is_superuser': False
        }

        json.dump(file, f, ensure_ascii=False, indent="\t")
        if i != N-1:
            f.write(',')
    f.write(']')
    f.close()

print(f'데이터 생성 완료 / 저장 위치: {save_dir}')
