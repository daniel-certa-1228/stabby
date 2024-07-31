DROP VIEW IF EXISTS view_blade_material_chart;

CREATE VIEW view_blade_material_chart AS
	SELECT
	    CASE 
		    WHEN 
		    	bm.name IS NOT NULL 
		    THEN
		    	CASE WHEN sm.name IS NOT NULL THEN sm.name || ' ' || bm.name ELSE bm.name END
		    ELSE 
		    	'Unknown' 
		END AS "name",
	    COUNT(k.knife_id) AS "count",
	    ROUND((COUNT(k.knife_id) * 100.0 / (SELECT COUNT(*) FROM stabby_web_knife WHERE is_active = true)), 2) AS percentage
	FROM 
		stabby_web_knife k
	LEFT JOIN 
		stabby_web_bladematerial bm ON bm.blade_material_id = k.blade_material_id 
	LEFT JOIN 
		stabby_web_steelmanufacturer sm ON sm.steel_manufacturer_id  = bm.steel_manufacturer_id 
	WHERE 
		k.is_active = true
	GROUP BY 
		bm.name,
		sm.name
	ORDER BY 
		"count" DESC, 
		sm.name,
		bm.name;
		
GRANT SELECT ON view_blade_material_chart TO db;