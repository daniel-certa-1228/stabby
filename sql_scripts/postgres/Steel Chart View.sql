DROP VIEW IF EXISTS view_steel_type_chart;

CREATE VIEW view_steel_type_chart AS
	SELECT 
		CASE 
			WHEN 
				st.name IS NOT NULL 
			THEN 
				st.name 
			ELSE 'Unknown' 
		END AS "name",
		COUNT(k.knife_id) AS "count",
	    ROUND((COUNT(k.knife_id) * 100.0 / (SELECT COUNT(*) FROM stabby_web_knife WHERE is_active = true)), 2) AS percentage
	FROM 
		stabby_web_knife k
	LEFT JOIN 
		stabby_web_bladematerial bm ON bm.blade_material_id = k.blade_material_id 
	LEFT JOIN 
		stabby_web_steeltype st ON st.steel_type_id = bm.steel_type_id 
	WHERE 
		k.is_active = TRUE
	GROUP BY 
		st.name
	ORDER BY 
		"count" DESC, 
		st.name;
		
GRANT SELECT ON view_steel_type_chart TO stabby_app;