# jumpToDjangoExercise
점프 투 장고를 빠르게 연습하자

- Pybo Django project

- 전반적인 설정을 설명하려고 한다.
- 다음 책을 이용하여 만든 프로젝트이다.
- [책 링크](https://wikidocs.net/book/4223)
- [배포 URL](https://pybods.shop/)
- 프로젝트 소개
    - 간단히 게시글 서비스이다.
    - 세션 쿠키방식의 회원가입 서비스를 사용한다!
    - ORM 기술을 사용!
    - Django 프레임 워크, gunicon, nginx, aws lightsail, postgreSQL, sqlite을 사용하였다.!

- <details>
    <summary>프로젝트 외부</summary>
    <div markdown="1">

    - 로컬(window 개발)
        - mysite.cmd
        - 로컬은
            - 프로젝트 위치로 이동한다음, 장고 관련 환경 변수를 local로 설정하고
            - mysite라는 가상환경으로 activate한다! (로컬에서)
    - 운영(Ubuntu)
        - 운영 환경은
        - .bashrc 뒷부분에 alias 명령어 설정
            - 프로젝트 위치로 이동한다음, 장고 관련 환경 변수를 prod로 설정하고
            - mysite라는 가상환경으로 activate한다!
        - 서비스 프로그램
            - gunicorn
                - WSGI server. 위스키 서버 라고도 함.
                - wev server와 WSGI application을 연결함. python 코드를 대신 호출.
                - 서버를 호출하는 방법은 TCP IP 방식과 소켓방식이 있는데, 소켓 방식이 빠르다 단, 소켓방식 사용시, NGINX 와 같은 웹서버가 필요.
                - /etc/systemd/system/mysite.service
                    - gunicorn 서비스 프로그램 실행 관련 내용 확인 가능.
                - 관련 중요 명령어.
                    
                    ```python
                    sudo systemctl restart mysite.service
                    ```
                    
            - nginx
                - 웹서버 역할
                - 파이보 서비스에 대한 Nginx의 설정파일을 다음과 같이 관리자 권한으로 작성한다.
                    - 파일 명
                        - /etc/nginx/sites-available/mysite
                    - nginx 실행 관련 중요한 설정들이 있다.
                        - ex)
                            - ssl 설정
                            - favicon 위치?
                            - 듣고 있는 포트.
                            - static 이 들어간 경로는 특정 경로에서 가져와라!
                            - 그게 아니면 gunicorn을 이용해라_!
                - nginx 서비스 실행 관련 중요 명령어
                    
                    ```python
                    sudo systemctl restart nginx
                    ```
                    
    - Cloud(AWS lightsail)
        - instance
            - Ubuntu
                - network
                    - IP firewall 설정
                        - 접속허용 포트 설정 (80, 443 등등.)
                - storage
                    - 40GB 설정
        - database
            - PostgreSQL
                - networking
                    - PUBLIC 모드 설정하여, 외부에서 DB 접근 가능 설정.!
        - networking
            - DNS 설정
            - static IP 설정
    </div>
    </details>



- <details>
    <summary>프로젝트 내부</summary>
    <div markdown="1">

    - 제일 중요한 설정(config)
        - 기본!(base.py)
            - BASE_DIR 설정
            - DEBUG 기본 설정
            - LOGGING 설정
            - INSTALLED_APPS :
            - TEMPLATE
            - DATABASE 설정
            - TIME ZONE 설정
            - STATICFILES_DIRS 설정
            - LOGIN_REDIRECT_URL
            - LOGOUT_REDIRECT_URL
        - 그외
            - 개발
                - local .py
                - 127.0.0.1 과 localhost를 허용한다.
            - 운영
                - prod.py
                    - ALLOWE_HOST
                    - STATIC_ROOT 변경
                    - DEBUG false
                    - .env 파일 읽기
                    - DATABASE 정보를 .env 정보 토대로 설정.
        - urls.py
            - pybo 패스는 pybo.url로 연결
            - common 패스는 common으로
            - ‘’ 는 index로!
            - DEBUG true일 경우 debug_toolbar 확인.
            - handler404 설정.
    - pybo
        - forms.py : api 에서 post 로 전달받은 데이터를 특정 형태로 가공하거나, 템플릿에서 form을 구성할때 사용하기도 함.
        - models.py : Django ORM 관련된 설정. 이 설정으로 테이블이 생성됨. M:N이면 관계 테이블이 생성되기도 함.
        - admin.py : 어드민 페이지를 구성할 떄 사용되는 파일.
        - tests.py : app을 테스트하기 위해 사용되는 코드. 파일이나 폴더 형태 가능.
        - urls.py : 특정 URL 패턴을 어떤 뷰파일의 어떤 함수와 연결할지 매핑함.
        - migrations : makeMigration 명령어 수행시, 만들어지는 파일들을 저장해두는 폴더
        - templatetags : 파이보 서비스에서 사용할 커스텀 필터들을 명시해둔 파일들을 저장한 폴더.
    - common
        - pybo와 유사 하여 생략
    - static
        - 정적 파일 경로
    - logs
        - 기본설정(base.py)에서 명시한 로그파일 설정 경로
    - templates
        - templates 파일들 이 모여있는 폴더.
        - template은 각 앱 밑에 하거나, 이렇게 한곳에 모아서 할수 있지만, 주로 후자를 선택.
    - 기타 파일들
        - .gitigrore
            - log 폴더 무시.
        - db.sqlite3
            - sqlite 관련된 파일.
        - manage.py
            - Django 프로젝트 생성시 만들어지는 기본 파일.
            - 이것을 이용하여 서버를 실행함. ex)python runserver manage.py
    - DB 관련하여…
        - DB는 DjangoORM을 사용
        - 모델은 DB의 테이블 과 연결되는 파이썬 코드.
        - 모델을 변경후, 다음 2step으로 적용함.
        - python [manage.py](http://manage.py/) makemigrations
            - 모델을 참고하여 migration 관련 python 코드 생성.
        - python [manage.py](http://manage.py/) migrate
            - 위에서 만든 코드를 이용하여 관련 테이블 생성 또는 수정.
    </div>
    </details>
    

