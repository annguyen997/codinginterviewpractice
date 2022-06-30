
'''CRACKING THE CODING INTERVIEW - Sixth Edition

Gayle Laakmann McDowell 

'''

'''Chapter 14 - Databases'''


/* 14.1 - Multiple Apartments
Write a SQL query to get a list of tenants who are renting more than one apartment. 
*/

SELECT TenantName
FROM Tenants T
INNER JOIN
    (SELECT TenantID FROM AptTenants GROUP BY TenantID HAVING COUNT(*) > 1) A
ON T.TenantID = A.TenantID 


/* 14.2 - Open Requests
Write a SQL query to get a list of all buildings and the number of open requests 
(Requests in which status equals 'Open')
*/ 
SELECT B.BuildingID, R.RequestID
FROM Buildings B, Requests R 
INNER JOIN (SELECT A.AptID FROM Apartments A WHERE B.BuildingID = A.BuildingID) AS Ap
WHERE Ap.AptID = R.AptID AND R.Status = "Open"

SELECT B.BuildingID, count(*) AS 'Count'
FROM Buildings B 
LEFT JOIN 
(SELECT A.BuildingID, count(*) as 'Count'
FROM Requests R INNER JOIN Apartments A 
ON Ap.AptID = R.AptID 
WHERE R.Status = 'Open' 
GROUP BY A.BuildingID) RequestCounts 
ON B.BuildingID = RequestCounts.BuildingID