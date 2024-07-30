
DROP VIEW IF EXISTS view_handle_material_chart;

CREATE VIEW view_handle_material_chart AS
	SELECT
	    CASE 
		    WHEN 
		    	hm.name IS NOT NULL 
		    THEN 
		    	hm.name 
		    ELSE 
		    	'Unknown' 
		END AS "name",
	    COUNT(k.knife_id) AS "count",
	    ROUND((COUNT(k.knife_id) * 100.0 / (SELECT COUNT(*) FROM stabby_web_knife WHERE is_active = true)), 2) AS percentage
	FROM 
		stabby_web_knife k
	LEFT JOIN 
		stabby_web_handlematerial hm ON hm.handle_material_id  = k.handle_material_id  
	WHERE 
		k.is_active = true
	GROUP BY 
		hm.name
	ORDER BY 
		"count" DESC, 
		hm.name;
		
GRANT SELECT ON view_handle_material_chart TO db;