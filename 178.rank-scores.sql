--
-- @lc app=leetcode id=178 lang=mysql
--
-- [178] Rank Scores
--
-- @lc code=start
# Write your MySQL query statement below
select score,
    dense_rank() over (
        order by score desc
    ) "rank"
from Scores;
-- @lc code=end