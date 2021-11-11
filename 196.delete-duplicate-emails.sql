--
-- @lc app=leetcode id=196 lang=mysql
--
-- [196] Delete Duplicate Emails
--
-- @lc code=start
# Write your MySQL query statement below
delete p2
from Person p2,
    Person p1
where p1.id < p2.id
    and p1.email = p2.email;
-- @lc code=end