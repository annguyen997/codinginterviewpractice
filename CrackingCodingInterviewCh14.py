
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

