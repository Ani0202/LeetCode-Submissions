# Write your MySQL query statement below
WITH Split_IP AS (
    SELECT 
        log_id, 
        ip,
        SUBSTRING_INDEX(ip, '.', 1) AS octet1,
        SUBSTRING_INDEX(SUBSTRING_INDEX(ip, '.', 2), '.', -1) AS octet2,
        SUBSTRING_INDEX(SUBSTRING_INDEX(ip, '.', 3), '.', -1) AS octet3,
        SUBSTRING_INDEX(ip, '.', -1) AS octet4,
        LENGTH(ip) - LENGTH(REPLACE(ip, '.', '')) AS dot_count
    FROM logs
), Invalid_IPs AS (
    SELECT 
        ip,
        COUNT(*) AS invalid_count
    FROM Split_IP
    WHERE 
        dot_count != 3 -- Less or more than 4 octets
        OR octet1 REGEXP '[^0-9]' OR octet2 REGEXP '[^0-9]' OR octet3 REGEXP '[^0-9]' OR octet4 REGEXP '[^0-9]' -- Non-numeric values
        OR octet1 + 0 > 255 OR octet2 + 0 > 255 OR octet3 + 0 > 255 OR octet4 + 0 > 255 -- Numbers greater than 255
        OR octet1 REGEXP '^0[0-9]' OR octet2 REGEXP '^0[0-9]' OR octet3 REGEXP '^0[0-9]' OR octet4 REGEXP '^0[0-9]' -- Leading zeros
    GROUP BY ip
)
SELECT ip, invalid_count
FROM Invalid_IPs
ORDER BY invalid_count DESC, ip DESC;
