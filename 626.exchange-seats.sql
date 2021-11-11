--
-- @lc app=leetcode id=626 lang=mysql
--
-- [626] Exchange Seats
--
-- @lc code=start
# Write your MySQL query statement below
select if(id % 2 = 1, if(id = counts, id, id + 1), id - 1) as id,
    student
from seat,
    (
        select count(*) as counts
        from seat
    ) x
order by id asc;
-- @lc code=end