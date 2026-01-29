use note;
#멤버 테이블 생성
create table 학생

(학번 CHAR(4) NOT NULL,
이름 VARCHAR(20) NOT NULL,
주소 VARCHAR(50) NULL DEFAULT '미정',
학년 INT NOT NULL,
나이 INT NULL,
성별 CHAR(1) NOT NULL,
휴대폰번호 CHAR(14) NULL,
소속학과 VARCHAR(20) NULL,
PRIMARY KEY (학번) ) ;

INSERT INTO 학생 VALUES ('s001', '김연아', '서울 서초', 4, 23, '여', '010-1111-2222', '컴퓨터') ;
INSERT INTO 학생 VALUES ('s002', '홍길동', DEFAULT, 1, 26, '남', NULL, '통계') ;
INSERT INTO 학생 VALUES ('s003', '이승엽', NULL, 3, 30, '남', NULL, '정보통신') ;
INSERT INTO 학생 VALUES ('s004', '이영애', '경기 분당', 2, NULL, '여', '010-4444-5555', '정보통신') ;
INSERT INTO 학생 VALUES ('s005', '송윤아', '경기 분당', 4, 23, '여', '010-6666-7777', '컴퓨터') ;
INSERT INTO 학생 VALUES ('s006', '홍길동', '서울 종로', 2, 26, '남', '010-8888-9999', '컴퓨터') ;
INSERT INTO 학생 VALUES ('s007', '이은진', '경기 과천', 1, 23, '여', '010-2222-3333', '경영') ;
INSERT INTO 학생 VALUES ('s008', '윤아라', '서울 강남', 4, 22, '여', '010-3333-4444', '컴퓨터');
INSERT INTO 학생 VALUES ('s009', '박찬호', '대전 유성', 3, 29, '남', '010-5555-6666', '통계');
INSERT INTO 학생 VALUES ('s010', '손흥민', '강원 춘천', 2, 24, '남', '010-7777-8888', '경영');
INSERT INTO 학생 VALUES ('s011', '윤도현', '서울 마포', 4, 28, '남', NULL, '정보통신');
INSERT INTO 학생 VALUES ('s012', '장나라', '서울 은평', 2, 25, '여', '010-9999-0000', '통계');
INSERT INTO 학생 VALUES ('s013', '최민식', '경기 일산', 3, 32, '남', '010-1234-5678', '컴퓨터');
INSERT INTO 학생 VALUES ('s014', '김혜수', '서울 송파', 4, 27, '여', '010-1111-3333', '경영');
INSERT INTO 학생 VALUES ('s015', '이정재', NULL, 1, 26, '남', '010-4444-1111', '정보통신');
INSERT INTO 학생 VALUES ('s016', '박보검', '서울 용산', 1, 21, '남', '010-5555-2222', '컴퓨터');
INSERT INTO 학생 VALUES ('s017', '윤지수', '경기 수원', 4, 23, '여', '010-6666-3333', '통계');


SELECT * FROM 학생 
WHERE 이름 LIKE '이%' 
and 성별 = '남';

select 성별, count(*) AS 남녀구분
from 학생
group by 성별;
