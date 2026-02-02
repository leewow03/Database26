from LMS.common import Session
from LMS.domain import Member


class MemberService:
    @classmethod
    def load(cls):
        conn = Session.get_connection()
        #conn은 연결 확인하는 변수
        try:
            with conn.cursor() as cursor:
                cursor.execute("SELECT COUNT(*) as cnt FROM members")
                count = cursor.fetchone()['cnt']
                print(f"시스템: 현재 등록된 회원 수는 {count}명입니다.")
        finally:
            conn.close()

    @classmethod
    def login(cls):
        print("\n[로그인]")
        #1. input에서 uid pw 받기
        uid = input("아이디: ")
        pw = input("비밀번호: ")

        #2. DB랑 연결 하는 통로를 conn에 ㄱ(출입증)
        conn = Session.get_connection()
        try: # cursor 이라는 통역사를 불러온다
            with conn.cursor() as cursor:
                # 3. sql이라는 설명서(변수)를 먼저 만든다
                sql = "SELECT * FROM members WHERE uid = %s AND password = %s"
                cursor.execute(sql, (uid, pw)) # 4. 설명서 안에 input 받은걸 넣은다 / (sql, (uid, pw)) = (설명서,(재료))
                row = cursor.fetchone() #5. 변수 row = cursor이라는 통역사가 하나를 가져오기 시도

                if row:
                    member = Member.from_db(row)

                    if not member.active:
                        print("비활성화된 계정입니다. 관리자에게 문의하세요.")
                        return

                    Session.login(member)
                    print(f"{member.name}님 로그인 성공 ({member.role})")
                else:
                    print("아이디 또는 비밀번호가 틀렸습니다.")
        finally:
            conn.close()

    # MemberService 클래스 내부에 추가하세요
    @classmethod
    def logout(cls):
        # 1. 먼저 세션에 로그인 정보가 있는지 확인
        if not Session.is_login():
            print("\n[알림] 현재 로그인 상태가 아닙니다.")
            return

        # 2. 세션의 로그인 정보 삭제
        Session.logout()
        print("\n[성공] 로그아웃 되었습니다. 안녕히 가세요!")

    @classmethod
    def logout(cls):
        print("\n[회원가입]")
        uid = input("아이디: ")

        conn = Session.get_connection()
        try:
            with conn.cursor() as cursor:
                # 1. 중복 체크
                check_sql = "SELECT id FROM members WHERE uid = %s"
                cursor.execute(check_sql, (uid,))
                if cursor.fetchone():
                    print("이미 존재하는 아이디입니다.")
                    return

                pw = input("비밀번호: ")
                name = input("이름: ")

                # 2. 데이터 삽입
                insert_sql = "INSERT INTO members (uid, password, name) VALUES (%s, %s, %s)"
                cursor.execute(insert_sql, (uid, pw, name))
                conn.commit()
                print("회원가입 완료! 로그인해 주세요.")
        except Exception as e:
            conn.rollback()
            print(f"회원가입 오류: {e}")
        finally:
            conn.close()

    @classmethod
    def modify(cls):  # 회원 수정 메서드
        if not Session.is_login():
            print("로그인 후 이용 가능합니다.")
            return

        member = Session.login_member
        print(f"내정보확인 : {member}")  # Member.__str__()
        print("\n[내 정보 수정]\n1. 이름 변경  2. 비밀번호 변경 3. 계정비활성 및 탈퇴 0. 취소")
        sel = input("선택: ")

        new_name = member.name
        new_pw = member.pw

        if sel == "1":
            new_name = input("새 이름: ")
        elif sel == "2":
            new_pw = input("새 비밀번호: ")
        elif sel == "3":
            print("회원 중지 및 탈퇴를 진행합니다.")
            cls.delete()
        else:
            return

        conn = Session.get_connection()
        try:
            with conn.cursor() as cursor:
                sql = "UPDATE members SET name = %s, password = %s WHERE id = %s"
                cursor.execute(sql, (new_name, new_pw, member.id))
                conn.commit()

                # 메모리(세션) 정보도 동기화
                member.name = new_name
                member.pw = new_pw
                print("정보 수정 완료")
        finally:
            conn.close()

    @classmethod
    def delete(cls):
        if not Session.is_login(): return
        member = Session.login_member

        print("\n[회원 탈퇴]\n1. 완전 탈퇴  2. 계정 비활성화")
        sel = input("선택: ")

        conn = Session.get_connection()
        try:
            with conn.cursor() as cursor:
                if sel == "1":
                    sql = "DELETE FROM members WHERE id = %s"
                    cursor.execute(sql, (member.id,))
                    print("회원 탈퇴 완료")
                elif sel == "2":
                    sql = "UPDATE members SET active = FALSE WHERE id = %s"
                    cursor.execute(sql, (member.id,))
                    print("계정 비활성화 완료")

                conn.commit()
                Session.logout()
        finally:
            conn.close()
