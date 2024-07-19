DROP VIEW IF EXISTS view_brand_chart;

CREATE VIEW view_brand_chart AS
	SELECT
	    b.name,
	    COUNT(k.knife_id) AS "count",
	    ROUND((COUNT(k.knife_id) * 100.0 / (SELECT COUNT(*) FROM stabby_web_knife WHERE is_active = true)), 2) AS percentage
	FROM 
		stabby_web_knife k
	LEFT JOIN 
		stabby_web_brand b ON b.brand_id = k.brand_id 
	WHERE 
		k.is_active = true
	GROUP BY 
		b.name
	ORDER BY 
		"count" DESC, 
		b.name;
		
GRANT SELECT ON view_brand_chart TO db;