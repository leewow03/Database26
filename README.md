# Database26
데이터베이스학습용mysql

MYSQL 설치 진행

mysql




```
행(ROW) 가로
열 (Column) 세로줄
SQL
 structured query language
(구조화된 쿼리 언어)의 약자
데베 쓸때 표준화된 문법
쿼리문은 뒤에서 부터 읽는게 편함

암기 방법
정의어 : DDL Data Definition Language
	데베, 데이블, 사용자, 뷰, 인덱스, 스키마 생성/ 수정/ 삭제
	생성 :  CREATE DATA BASE / CREAT TABLE / CREATE USER
	수정 : ALTER DATABASE / ALTER TABLE / ALTER USER
	삭제 : DROP DATABASE/ DROP TABLE / DROP USER
	이름 변경 : RENAME TBALE / RENAME USER
	테이블 초기화 : TRUNCATE

조작어 : DML Data manipulation Language
	데이터 테이블에 자료 관리용
	C (자료생성) : INSERT INTO 테이블명(필드명들) VALUES(값들)
	R (찾아옴): SELECT 필드명 FROM 테이블 WHERE 조건
	U(자료수정): UPDATE 테이블명 SET(필드명=값) WHERE 조건
	D(자료 삭제): DELETE FROM 테이블 WHERE 조건
제어어 : DCL 데이터의 보안, 무결성, 데이터 회복, 병행수행 등(데이터관리목적)
Data Control Language
	ROLLBACK : 트렌직션 복귀
	COMMIT : 트렌직션 저장
		(트렌직션 : 일괄작업)
	GRANT : 권한 부여
	(사용자에게 관리자가 테이블 및 기능에 권한 부여)
	REVOKE: 권한 삭제
```
