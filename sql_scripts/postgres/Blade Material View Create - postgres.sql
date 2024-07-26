
DROP VIEW IF EXISTS view_blade_material_chart;

CREATE VIEW view_blade_material_chart AS
	SELECT
	    CASE 
		    WHEN 
		    	bm.name IS NOT NULL 
		    THEN 
		    	bm.name 
		    ELSE 
		    	'Unknown' 
		END AS "name",
	    COUNT(k.knife_id) AS "count",
	    ROUND((COUNT(k.knife_id) * 100.0 / (SELECT COUNT(*) FROM stabby_web_knife WHERE is_active = true)), 2) AS percentage
	FROM 
		stabby_web_knife k
	LEFT JOIN 
		stabby_web_bladematerial bm ON bm.blade_material_id  = k.blade_material_id 
	WHERE 
		k.is_active = true
	GROUP BY 
		bm.name
	ORDER BY 
		"count" DESC, 
		bm.name;
		
GRANT SELECT ON view_blade_material_chart TO db;