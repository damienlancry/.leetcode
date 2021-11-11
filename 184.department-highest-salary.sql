--
-- @lc app=leetcode id=184 lang=mysql
--
-- [184] Department Highest Salary
--
-- @lc code=start
# Write your MySQL query statement below
select d.name as Department,
    x.name as Employee,
    x.salary as Salary
from (
        select name,
            departmentId,
            salary,
            dense_rank() over(
                partition by departmentId
                order by salary desc
            ) rk
        from Employee
    ) x
    join Department as d on d.id = x.departmentId
    and rk = 1;
-- @lc code=end