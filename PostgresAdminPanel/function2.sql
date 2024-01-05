SELECT
    client_addr,
    usename,
    COUNT(*) AS num_connections
FROM pg_stat_activity
GROUP BY client_addr, usename
ORDER BY num_connections DESC;
