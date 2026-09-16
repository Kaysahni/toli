-- cache_hit_ratio.sql
-- owner: Platform Performance
-- schedule: daily 08:00
select
  date_trunc('hour', ts) as hour,
  sum(case when hit then 1 else 0 end)::float / count(*) as hit_ratio,
  count(*) as lookups
from routecache_v1.hits
where ts >= now() - interval '24 hours'
group by 1
order by 1;
