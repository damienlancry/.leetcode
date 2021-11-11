--
-- @lc app=leetcode id=601 lang=mysql
--
-- [601] Human Traffic of Stadium
--
-- @lc code=start
# Write your MySQL query statement below
select distinct s1.*
from Stadium s1,
    Stadium s2,
    Stadium s3
where (
        s1.people >= 100
        and s2.people >= 100
        and s3.people >= 100
    )
    and (
        (
            s1.id = s2.id + 1
            and s1.id = s3.id + 2
        )
        or (
            s1.id = s2.id - 1
            and s1.id = s3.id + 1
        )
        or (
            s1.id = s2.id - 1
            and s1.id = s3.id - 2
        )
    )
order by visit_date asc;
-- @lc code=end