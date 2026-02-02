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
        uid = input("아이디: ")

        conn = Session.get_connection()
        try:
            with conn.cursor() as cursor:
                sql = "SELECT * FROM members WHERE uid = %s"
                cursor.execute(sql, (uid,))
                row = cursor.fetchone()

                if not row:
                    print("아이디가 틀렸습니다.")
                    return

                member = Member.from_db(row)

                if not member.active:
                    print("비활성화된 계정입니다. 관리자에게 문의하세요.")
                    return

                chance = 3
                while chance > 0:
                    pw_input = input(f"비밀번호 입력 (기회 {chance}번): ")

                    if member.pw == pw_input:
                        Session.login(member)
                        print(f"{member.name}님 로그인 성공 ({member.role})")
                        return
                    else:
                        chance -= 1
                        if chance > 0:
                            print("비밀번호가 틀렸습니다.")
                        else:
                            print(f"3번 모두 틀렸습니다. 아이디 \"{uid}\"를 비활성화합니다.")
                            update_sql = "UPDATE members SET active = %s WHERE uid = %s"
                            cursor.execute(update_sql, (False, uid))
                            conn.commit()
                            return
        finally:
            conn.close()
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

    @classmethod
    def list_members(cls):
        print("\n [회원 목록]")
        for m in cls.members:
            print(m)

    @classmethod
    def admin_dif_menu(cls):
        while True:
            print("""
[회원 정보 수정 메뉴]
1. 비활성화 처리
2. 권한 변경

9. 뒤로 가기
        """)
            sel = input("선택: ")

            if sel == "1":
                cls.block_member()
            elif sel == "2":
                cls.change_role()
            elif sel == "9":
                break

    @classmethod
    def block_member(cls):
        uid = input("대상 아이디: ")
        for m in cls.members:
            if m.uid == uid:
                m.active = False
                cls.save()
                print("비활성화 처리 완료")
                return
        print("회원 없음")

    @classmethod
    def change_role(cls):
        uid = input("대상 아이디: ")
        for m in cls.members:
            if m.uid == uid:
                m.role = input("admin / user: ")
                cls.save()
                print("권한 변경 완료")
                return
        print("회원 없음")

