# 플라스크 게시판 만들기

### [파이썬 환경 설정](https://github.com/mcDeeplearning/TIL/blob/master/%ED%8C%8C%EC%9D%B4%EC%8D%AC%20%ED%99%98%EA%B2%BD%EC%84%A4%EC%A0%95.md)

### 데이터베이스

- 설정
```bash
$ sudo apt-get update
# ubuntu에 postgresql을 설치
$ sudo apt-get install postgresql postgresql-contrib libpq-dev
# python(flask)에서 postgresql를 사용하기 편하게 도와주는 친구들
$ pip install psycopg2 psycopg2-binary
# import 해서 쓸 친구들
$ pip install Flask-SQLAlchemy Flask-Migrate
```

- DB 설정
```bash
# postresql 실행
$ psql
ubuntu# CREATE DATABASE <이름> WITH template=template0 encoding='UTF8';
ubuntu# \q 
```

### `models.py`설정
### `app.py` 설정

### 마이그레이션

- flask db initialize : `flask db init`
    - `migrations`폴더 생성
- models.py 파일의 현재 상태를 반영 : `flask db migrate`
    - `migrations`폴더에 파일 생성
- DB에 반영 : `flask db upgrade`
- 실제로 DB에서 확인하기
    - `psql <이름>` 
    - `ubuntu# \d <테이블이름>`