SELECT * FROM note.성적;

SELECT 소속학과, 
       COUNT(*) AS 인원수,
       AVG(점수) AS 평균점수
FROM 성적
GROUP BY 소속학과
HAVING AVG(점수) >= 80;  


select 소속학과, 점수
from 성적 
where 점수 >= 85
ORDER BY 소속학과 asc;