use world;

show tables; # 어떤 테이블이 있는지 보기
select * from country; # 테이블 내용 보기
SELECT * FROM country WHERE Code = 'KOR';

select * from country where region like '%Asia%';
select *  from country where region like concat('%','Asia','%');

select * from country where char_length(name)= 5;
select * from country where name like '_____';

select * from country order by population desc;

select * from country where lifeExpectancy >= 60 and lifeExpectancy<=70
order by LifeExpectancy asc;
select *from country where lifeexpectancy between 60 and 70
order by lifeexpectancy desc;

SELECT * FROM country 
WHERE Region NOT LIKE '%Asia%' and
name LIKE '%g%' OR name LIKE '%u%'
ORDER BY Population DESC;

SELECT * FROM country 
WHERE Region NOT LIKE '%Asia%' and
name regexp '[g, u]'
ORDER BY Population DESC;
