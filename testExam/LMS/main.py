from testExam.LMS.service import *
from testExam.LMS.common import *
import pymysql

def main():
    MemberService.load()
    run = True
    while run:
        member = Session.login_member

        # 로그인 안했을때 메인 메뉴
        if member is None :
            Menu.main_menu()
            print("시작할려면 로그인 하세요.")
            sel = input(">>> ")
            if sel == "1": MemberService.signup()
            elif sel == "2": MemberService.login()
            elif sel == "9":
                print("프로그램 종료")
                run = False


        # 관리자가 했을때 메인 메뉴
        elif Session.is_admin():
            print("sad")
            subrun = True
            while subrun:
                Menu.admin_menu()
                sel = input(">>> ")
                if sel == "1": pass   # 회원 점수보기
                elif sel == "2": pass # 게시판 메뉴
                elif sel == "3": pass # 자판기 메뉴
                elif sel == "4": MemberService.list_members() # 회원 보기
                elif sel == "5": MemberService.admin_dif_menu()# 회원 정보 수정
                elif sel == "6":
                    print("로그아웃 되었습니다.")
                    Session.login_member = None
                    subrun = False
                elif sel == "9":
                    print("프로그램 종료")
                    subrun = False
                    run = False
                else:
                    print("다시 선택해주시오.")

        # 유저가 로그인시 유저 메뉴 띄우기
        else:
            subrun = True
            while subrun:
                Menu.login_menu()
                sel = input(">>> ")
                if sel == "1": pass  #본인 점수보기
                elif sel == "2": pass  # 게시판 메뉴
                elif sel == "3": pass  # 자판기 메뉴
                elif sel == "4": MemberService.PI_members() #본인 정보 보기
                elif sel == "5": MemberService.modify() # 본인 정보 수정
                elif sel == "6":
                    if MemberService.delete():
                        subrun = False  # 계정 탈퇴
                elif sel == "7":
                    print("로그아웃 되었습니다.")
                    Session.login_member = None
                    subrun = False
                elif sel == "9":
                    print("프로그램 종료")
                    subrun = False
                    run = False
                else:
                    print("다시 선택해주시오.")

if __name__ == "__main__":
    main()