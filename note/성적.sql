create database note;
use note;
CREATE TABLE 성적 (
    학번 CHAR(4) PRIMARY KEY,
    이름 VARCHAR(20),
    학년 INT,
    소속학과 VARCHAR(20),
    과목명 VARCHAR(20),
    점수 INT
);

# 모든 학생(s001 ~ s017) 데이터 입력
INSERT INTO 성적 VALUES ('s001', '김연아', 4, '컴퓨터', '데이터베이스', 95);
INSERT INTO 성적 VALUES ('s002', '홍길동', 1, '통계', '통계학원론', 70);
INSERT INTO 성적 VALUES ('s003', '이승엽', 3, '정보통신', '네트워크', 85);
INSERT INTO 성적 VALUES ('s004', '이영애', 2, '정보통신', '네트워크', 92);
INSERT INTO 성적 VALUES ('s005', '송윤아', 4, '컴퓨터', '데이터베이스', 88);
INSERT INTO 성적 VALUES ('s006', '홍길동', 2, '컴퓨터', '알고리즘', 82);
INSERT INTO 성적 VALUES ('s007', '이은진', 1, '경영', '마케팅', 90);
INSERT INTO 성적 VALUES ('s008', '윤아라', 4, '컴퓨터', '데이터베이스', 94);
INSERT INTO 성적 VALUES ('s009', '박찬호', 3, '통계', '통계학원론', 76);
INSERT INTO 성적 VALUES ('s010', '손흥민', 2, '경영', '회계원리', 81);
INSERT INTO 성적 VALUES ('s011', '윤도현', 4, '정보통신', '운영체제', 89);
INSERT INTO 성적 VALUES ('s012', '장나라', 2, '통계', '통계학원론', 98);
INSERT INTO 성적 VALUES ('s013', '최민식', 3, '컴퓨터', '알고리즘', 75);
INSERT INTO 성적 VALUES ('s014', '김혜수', 4, '경영', '마케팅', 91);
INSERT INTO 성적 VALUES ('s015', '이정재', 1, '정보통신', '운영체제', 84);
INSERT INTO 성적 VALUES ('s016', '박보검', 1, '컴퓨터', '데이터베이스', 100);
INSERT INTO 성적 VALUES ('s017', '윤지수', 4, '통계', '통계학원론', 87);
SELECT * FROM 성적;
