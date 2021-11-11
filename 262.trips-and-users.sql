--
-- @lc app=leetcode id=262 lang=mysql
--
-- [262] Trips and Users
--
-- @lc code=start
# Write your MySQL query statement below
select request_at as Day,
    round(
        avg(
            if(status = 'completed', 0, 1)
        ),
        2
    ) as 'Cancellation Rate'
from Trips t
    join Users c on t.client_id = c.users_id
    and c.banned = 'No'
    join Users d on t.driver_id = d.users_id
    and d.banned = 'No'
where request_at between '2013-10-01' and '2013-10-03'
group by request_at;
-- @lc code=end