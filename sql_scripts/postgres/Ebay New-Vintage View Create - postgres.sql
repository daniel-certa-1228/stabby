DROP VIEW IF EXISTS view_ebay_new_vintage_chart;

CREATE VIEW view_ebay_new_vintage_chart AS
SELECT 
	"name",
	"count",
	ROUND(("count" * 100.0 / (SELECT COUNT(*) FROM stabby_web_knife WHERE is_active = TRUE AND vendor_id = 9)), 2) AS percentage
FROM (
	SELECT 
		'New' AS "name",
		count(*) 
	FROM stabby_web_knife k
	WHERE 
		k.is_active = TRUE
		AND k.vendor_id = 9
		AND k.purchased_new = TRUE
	UNION ALL 
	SELECT 
		'Vintage' AS "name",
		count(*) 
	FROM stabby_web_knife k
	WHERE 
		k.is_active = TRUE
		AND k.vendor_id = 9
		AND k.purchased_new = False
) a
ORDER BY
	"count" DESC;
		
GRANT SELECT ON view_ebay_new_vintage_chart TO db;