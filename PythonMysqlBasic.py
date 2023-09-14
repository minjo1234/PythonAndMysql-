
import pymysql

print('mysql 연동한 이후에 crud 작업할 예정입니다.')

# database connection
config = {
    'host': '127.0.0.1',
    'user': 'root',
    'password': 'Wlgns3350@',
    'database': 'naver',
    'port': 3306,
    'charset': 'utf8',
    'use_unicode': True
}

conn = pymysql.connect(**config)
cursor = conn.cursor()

# table Create


def CreateTable():
    sql = '''create table User (
        id varchar(255) not null primary key,
        name varchar(255) not null,
        password varchar(255) not null,
        age int not null, 
        gender char(1) not null, 
        birth date
        )'''
    cursor.execute(sql)
    print('User 테이블 생성성공')

# dbInsert


def dbInsert():
    id = input('ID를 입력해주세요. : ')
    name = input('이름을 입력해주세요. : ')
    password = input('Password를 입력해주세요 : ')
    age = int(input('나이를 입력해주세요 : '))
    gender = input('성별을 입력해주세요 ex)남/여 : ')
    birth = input('생일을 입력해주세요 ex)2001-12-08 : ')
    sql = f"insert into naver.user values ('{id}' , '{name}' , '{password}' , {age} , '{gender}' , '{birth}')"
    cursor.execute(sql)
    conn.commit()
    print()
    print(f'{name} 님 저장성공했습니다.')
# dbSelect


def dbSelect():
    sql = "select * from naver.user"
    cursor.execute(sql)
    rows = cursor.fetchall()  # 전체출력

    for r in rows:
        print('%s   %s   %s   %d   %s   %s' % r)
    print('조회된 결과수 :', len(rows))
    print('-'*50)

# dbUpdate


def dbUpdate():
    print()
    id = input('수정할 아이디입력 : ')
    name = input('수정할 이름입력 : ')
    password = input('수정할 비밀번호 입력 : ')
    sql = f"update naver.user set id= '{id}' , name = '{name}', password = '{password}' where id = '{id}'"
    cursor.execute(sql)
    conn.commit()
    print(f'{name} 님 수정성공했습니다.')
# dbDelete


def dbDelete():
    print()
    id = input('삭제할 아이디 입력 : ')
    sql1 = f"select * from naver.user where id = '{id}'"
    cursor.execute(sql1)
    rows = cursor.fetchall()
    print('삭제직전')

    if rows:
        sql2 = f"delete from naver.user where id = '{id}'"
        cursor.execute(sql2)
        conn.commit()
        print(f'{id} 님 삭제완료되었습니다.')
    else:
        print(f'{id} 님에 대한 정보가 없습니다. ')
# dbSearch


def dbSearch():
    id = input('찾고싶은 Id를 입력해주세요.')
    sql = f"select * from naver.user where id = '{id}'"
    cursor.execute(sql)
    rows = cursor.fetchall()

    if rows:
        for r in rows:
            print('%s   %s   %s   %d   %s   %s' % r)
    else:
        print('결과가 존재하지 않습니다.')


# crud 실행할 반복문 작성
flag = True

while flag:
    print()
    sel = int(input('1.신규 2.출력 3.갱신 4.삭제 5.조회 9.종료 >>>'))
    if sel == 1:
        dbInsert()
    elif sel == 2:
        dbSelect()
    elif sel == 3:
        dbUpdate()
    elif sel == 4:
        dbDelete()
    elif sel == 5:
        dbSearch()
    elif sel == 9:
        print('Python Mysql CRUD 프로젝트가 종료됩니다.')
        flag = False
    else:
        print('잘못입력하셨습니다 다시 입력하여주세요.')
