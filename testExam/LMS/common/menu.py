class Menu:
    members = None
    menu = None

    @classmethod
    def main_menu(cls):
        print("""
====textExam LMS====
    [메인 메뉴]
1. 회원가입
2. 로그인

9. 프로그램 종료
""")

    @classmethod
    def login_menu(cls):
        print("""
====textExam LMS====
    [회원 메뉴]
1. 본인 점수 보기
2. 게시판 
3. 자판기
4. 본인 정보 보기
5. 본인 정보 수정
6. 계정 탈퇴
7. 로그 아웃

9. 프로그램 종료
""")

    @classmethod
    def admin_menu(cls):
        print("""
====textExam LMS====
    [관리자 메뉴]
1. 회원 점수 보기
2. 게시판 
3. 자판기
4. 회원 보기
5. 회원 정보 수정
6. 로그아웃

9. 프로그램 종료
""")

