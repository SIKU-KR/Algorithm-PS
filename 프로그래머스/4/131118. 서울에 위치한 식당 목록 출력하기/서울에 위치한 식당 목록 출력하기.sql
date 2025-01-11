SELECT 
    i.REST_ID, 
    i.REST_NAME, 
    i.FOOD_TYPE, 
    i.FAVORITES, 
    i.ADDRESS, 
    ROUND(AVG(r.REVIEW_SCORE),2) as SCORE
FROM
    REST_INFO as i
    JOIN REST_REVIEW as r
    ON i.REST_ID = r.REST_ID
WHERE 
    i.REST_ID = r.REST_ID AND 
    i.ADDRESS LIKE '서울%'
GROUP BY 
    1, 2, 3, 4, 5
ORDER BY
    SCORE desc,
    FAVORITES desc