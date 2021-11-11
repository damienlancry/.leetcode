--
-- @lc app=leetcode id=627 lang=mysql
--
-- [627] Swap Salary
--
-- @lc code=start
# Write your MySQL query statement below
update Salary
set sex = if(sex = 'm', 'f', 'm');
-- @lc code=end