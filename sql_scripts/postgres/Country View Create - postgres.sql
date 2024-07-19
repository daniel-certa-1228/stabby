
DROP VIEW IF EXISTS view_country_chart;

CREATE VIEW view_country_chart AS
	SELECT
	    CASE 
		    WHEN 
		    	c.name IS NOT NULL 
		    THEN 
		    	c.name 
		    ELSE 
		    	'Unknown' 
		END AS "name",
	    COUNT(k.knife_id) AS "count",
	    ROUND((COUNT(k.knife_id) * 100.0 / (SELECT COUNT(*) FROM stabby_web_knife WHERE is_active = true)), 2) AS percentage
	FROM 
		stabby_web_knife k
	LEFT JOIN 
		stabby_web_country c ON c.country_id = k.country_id 
	WHERE 
		k.is_active = true
	GROUP BY 
		c.name
	ORDER BY 
		"count" DESC, 
		c.name;
		
GRANT SELECT ON view_country_chart TO db;