--
-- @lc app=leetcode id=197 lang=mysql
--
-- [197] Rising Temperature
--
-- @lc code=start
# Write your MySQL query statement below
select distinct w2.id
from Weather w1
    join Weather w2 on datediff(w2.recordDate, w1.recordDate) = 1
    and w2.temperature > w1.temperature;
-- @lc code=end