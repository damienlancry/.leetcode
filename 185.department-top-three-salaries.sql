--
-- @lc app=leetcode id=185 lang=mysql
--
-- [185] Department Top Three Salaries
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
            dense_rank() over (
                partition by departmentId
                order by salary desc
            ) rk
        from Employee
    ) x
    join Department d on d.id = x.departmentId
where rk < 4;
-- @lc code=end