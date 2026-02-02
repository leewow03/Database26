# session에서 DB접속도 관리하자!
# 현재 session으로 상태관리를 하는데 차후에
# 프론트를 배우면 웹브라우져에서 세션을 처리한다.
# html + css + js: w3c라고 부른다. 웹표준!
# 차후에는 이곳이 DB관리하는 connection 영역이 될것이다.

# 파이참에서도 DB를 관리하는 메뉴가 있다.
# 오른쪽 버튼에 DB 선택함 -> mysql 워크밴치 대타용

import pymysql #  pip install pymysql 터미널 설치필수

class Session:
    login_member = None

    @staticmethod
    def get_connection(): # 데이터베이스에 연결용 코드
        print("get_connection()메서드 호출 - mysql에 접속됩니다.")

        return pymysql.connect(
            host='localhost',
            user='mbc',
            password='1234',
            db='lms',
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor
            #dict 타입으로 처리함(딕셔너리타입 k : v)
        )
    @classmethod
    def login(cls,member):# MemberService에서 로그인시 객체를 담아놈
        cls.login_member = member

    @classmethod
    def logout(cls):
        cls.login_member = None

    @classmethod
    def is_login(cls):
        return cls.login_member is not None
        # 로그인 했으면 True / 안했으면 False

    # 추가: 권한 체크 메서드 (서비스 계층에서 사용됨)
    @classmethod
    def is_admin(cls): # 로그인한 객체가 admin이냐?
        return cls.is_login() and cls.login_member.role == "admin"
        # 로그인했고 role이 admin이면 True / None False

    @classmethod
    def is_manager(cls):
        # 매니저이거나 어드민이면 참 (보통 어드민이 매니저 권한을 포함함)
        return cls.is_login() and cls.login_member.role in ("manager", "admin")