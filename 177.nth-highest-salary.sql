--
-- @lc app=leetcode id=177 lang=mysql
--
-- [177] Nth Highest Salary
--
-- @lc code=start
CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT BEGIN RETURN (
  # Write your MySQL query statement below.
  select(
      select distinct salary
      from (
          select salary,
            dense_rank() over (
              order by salary desc
            ) rnk
          from Employee
        ) x
      where rnk = N
    )
);
END
END -- @lc code=end