# 파이썬과 mysql 병합 작업을 위한 sql 페이지
USE lms;
# 절차: 일반적으로 system(root) 계정은 개발용으로 사용 안함
# mysql에  사용할 id / pw / 권한 등을 부여하고 db 생성한다.

#DROP USER IF EXISTS 'mbc'@'localhost';
CREATE USER 'mbc'@'localhost' IDENTIFIED BY '1234'; 
# 사용자계정생성 ID     접속PC     				비번
# '1hj'@'192.168.0.154' '5678' -> 임효정씨가 154주소로 들어옴
#'1hj'@'192.168.0.%' -> 192.168.0.1~192.168.0.255
# '1hj'@'%" -> 전체ip(외부에서도 접속됨->보안에 좋지 않음)
# 사용자 계정 생성은 ID가 중복되어도 됨 -> 대신 접속PC를 다중처리를 할수 있음
# CREATE USER 'mbc'@'%'IDENTIFIED BY 'Mbc320!!';

# 사용자를 삭제
DROP USER 'mbc'@'localhost';

# mbc사용자에게 lms 권한 부여
# 1. 데이터베이스 생성-> 2. 계정에 권한을 준다.
CREATE DATABASE lms DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
# lms 데이터베이스를 생성 				 한국어 지원 utf-8
# COLATE : 문자 집합에 포함된 문자들을 어떻게 비교하고 정렬할지 정의하는 키워드
# 데이터비교시 대소문자 구분, 문자 간의 정렬 순서, 언어별 특수문자 처리 방식 지원
# utf8mb4: 문자집합
# general : 비교규칙(간단한 일반비교)
# ci : Case Insensitive(대소문자 구분하지 않겠다)
# COLLATE utf8mb4_bin(대소문자 구분함)

# mbc라는 계정에 lms를 사용할수있게 권한 부여
GRANT ALL PRIVILEGES  ON LMS.* TO 'mbc'@'localhost';
#					DB명.테이블  ID   		접속PC
# ALL PRIVILEGES -> 모든 권한 부여
# GRANT select ,insert ON LMS.* TO '알바'@'%';
# 		READ	CREATE

# 권한 즉시 반영
FLUSH PRIVILEGES;

USE MYSQL;  #MYSQL 최고 DB에 접속
select * from user; #MYSQL에 사용자의 목록을 볼수가 있다.












