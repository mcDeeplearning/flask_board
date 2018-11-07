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
    - 

# 배포!!!
### 설정

완성된 CRUD board

heroku에 배포

- `app.py`

```python
import os
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get('DATABASE_URL')
```

- Heroku 에서는 연결되는 DB가 DATABASE_URL이라는 환경변수로 지정되어 있음.
- 만약 이렇게 변경하고 내 로컬 작업환경(혹은 C9)에서 문제가 되지 않으려면 환경변수 지정을 해줘야함.

```bash
echo 'export DATABASE_URL="postgresql:///board"' >> ~/.bashrc
source ~/.bashrc
```



### gunicorn

- gunicorn 설치(heroku에서 서버 실행)

```bash
pip install gunicorn
```

- Procfile(**확장자 없음**, **P는 대문자!!!**)

```bash
# /Procfile
web: gunicorn app:app
```

- 서버 실행 테스트

```bash
gunicorn app:app
```



### heroku 셋팅

- `runtime.txt`

```
python-3.6.1
```

- requirements.txt

```bash
pip freeze > requirements.txt
```

- 필요없는 부분 삭제
  - pygobject
  - python-apt
  - python-editor
  - unattended-upgrades



### heroku 배포

> {프로젝트명} 은 헤로쿠에 이미 있는 프로젝트명은 설정이 불가함. unique하게!

```
$ heroku login
$ heroku create {프로젝트명}
$ heroku git:clone -a {프로젝트명}
$ git push heroku master
```

### heroku postgresql addon 설정

```
$ heroku addons:create heroku-postgresql:hobby-dev
```

### heroku 에서 마이그레이션 파일 반영

```
$ heroku run flask db upgrade -a {프로젝트명}
```

