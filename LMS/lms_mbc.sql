USE LMS; # LMS 데이터베이스를 사용하겠다.

#DROP TABLE members;

CREATE TABLE members( #members테이블 생성
# 	필드명     타입    옵션
	id INT AUTO_INCREMENT PRIMARY KEY,
	uid VARCHAR(50) NOT NULL UNIQUE,
	password VARCHAR(255) NOT NULL,
	name VARCHAR(50) NOT NULL,
	role ENUM('admin', 'manager' , 'user') DEFAULT 'user',
	active BOOLEAN DEFAULT TRUE,
created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);
DESC members;

#더미데이터 입력
insert into members(uid,password, name, role, active)
values
('kkw','1234','김기원','admin',true),
('bob','111','밥','admin',true),
('lhj', '5678', '임효정', 'manager',true),
('kdg', '1111', '김도균', 'user', true),
('ksb', '2222', '김수빈' , 'user', true),
('kjy', '3333','김지영', 'user', true); # 여러개 추가시 ctrl+shift+enter

#더미데이터 출력
select * From members; # 전체 출력

# 로그인 할 때 
select*from members where uid='kkw' and password='1234' and active=true;

#더미데이터 수정
UPDATE members set password = '1111' where uid = 'kkw';

#회원삭제
delete from members where id=1;
update members set active = false Where id = '7'; #회원 비활성화


