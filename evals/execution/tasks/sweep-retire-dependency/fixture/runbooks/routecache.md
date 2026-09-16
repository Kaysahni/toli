# RouteCache

RouteCache is a read-through cache in front of RouteCalc for the most requested
lanes. It is a separate API with its own versioning; it is not being retired
and its v1 is the only version.

Owner: Platform Performance (Signe Halvorsen).

- API: `https://routecache.core.tesselwick.internal/v1`
- Short alias: `rcache.tsw.internal`
- Warehouse table for hit statistics: `routecache_v1.hits`

## Notes

- The cache is warmed every morning by lane-cache-warmer.
- Entries expire after 6 hours or when map data is reloaded.
- If the hit ratio drops under 60%, check that the warmer ran. If it did, check
  whether RouteCalc v2 had a map data reload overnight (that flushes the cache).

RouteCache already reads from RouteCalc v2 only. Its upstream was switched in
January 2026, so the v1 retirement needs nothing from this team.
