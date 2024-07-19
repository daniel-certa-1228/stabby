DROP VIEW IF EXISTS view_lock_type_chart;

CREATE VIEW view_lock_type_chart AS
	SELECT
	    CASE 
		    WHEN 
		    	lt.name IS NOT NULL 
		    THEN 
		    	lt.name 
		    ELSE 'Unknown' 
		END AS "name",
	    COUNT(k.knife_id) AS "count",
	    ROUND((COUNT(k.knife_id) * 100.0 / (SELECT COUNT(*) FROM stabby_web_knife WHERE is_active = true)), 2) AS percentage
	FROM 
		stabby_web_knife k
	LEFT JOIN 
		stabby_web_locktype lt ON lt.lock_type_id  = k.lock_type_id  
	WHERE 
		k.is_active = true
	GROUP BY 
		lt.name
	ORDER BY 
		"count" DESC, 
		lt.name;
		
GRANT SELECT ON view_lock_type_chart TO db;