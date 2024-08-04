DROP VIEW IF EXISTS view_usa_new_vintage_chart;

CREATE VIEW view_usa_new_vintage_chart AS
	SELECT 
	"name",
	"count",
	ROUND(("count" * 100.0 / (SELECT COUNT(*) FROM stabby_web_knife WHERE is_active = TRUE AND country_id = 16)), 2) AS percentage
FROM (
	SELECT 
		'New' AS "name",
		count(*) 
	FROM stabby_web_knife k
	WHERE 
		k.is_active = TRUE
		AND k.country_id = 16
		AND k.purchased_new = TRUE
	UNION ALL 
	SELECT 
		'Vintage' AS "name",
		count(*) 
	FROM stabby_web_knife k
	WHERE 
		k.is_active = TRUE
		AND k.country_id = 16
		AND k.purchased_new = False
) a
ORDER BY
	"count" DESC;
		
GRANT SELECT ON view_usa_new_vintage_chart TO db;