SELECT 
    table_name,
    pg_size_pretty(pg_total_relation_size('"' || t.table_schema || '"."' || t.table_name || '"')) AS table_size,
    pg_size_pretty(pg_indexes_size('"' || t.table_schema || '"."' || t.table_name || '"')) AS index_size,
    pg_size_pretty(pg_total_relation_size('"' || t.table_schema || '"."' || t.table_name || '"') + pg_indexes_size('"' || t.table_schema || '"."' || t.table_name || '"')) AS total_size
FROM information_schema.tables t
WHERE 
    t.table_schema = 'public'
    AND t.table_type = 'BASE TABLE'
ORDER BY 
    pg_total_relation_size('"' || t.table_schema || '"."' || t.table_name || '"') + pg_indexes_size('"' || t.table_schema || '"."' || t.table_name || '"') DESC;
