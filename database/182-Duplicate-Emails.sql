--Write a SQL query to find all duplicate emails in a table named Person.
--
--+----+---------+
--| Id | Email   |
--+----+---------+
--| 1  | a@b.com |
--| 2  | c@d.com |
--| 3  | a@b.com |
--+----+---------+
--For example, your query should return the following for the above table:
--
--+---------+
--| Email   |
--+---------+
--| a@b.com |
--+---------+

SELECT DISTINCT E1.Email
FROM Person E1, Person E2
WHERE E1.Email = E2.Email
AND E1.Id <> E2.Id

SELECT Email FROM Person group by Email having count(*)>1