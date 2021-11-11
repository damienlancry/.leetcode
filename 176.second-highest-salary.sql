--
-- @lc app=leetcode id=176 lang=mysql
--
-- [176] Second Highest Salary
--
-- @lc code=start
# Write your MySQL query statement below
# select max(salary) as SecondHighestSalary
# from Employee
# where salary < (
#         select max(salary)
#         from Employee
#     );
select (
        select distinct salary
        from (
                select salary,
                    dense_rank() over (
                        order by salary desc
                    ) rnk
                from Employee
            ) x
        where rnk = 2
    ) as SecondHighestSalary;
-- @lc code=end