DROP VIEW IF EXISTS view_blade_shape_chart;

CREATE VIEW view_blade_shape_chart AS
	SELECT 
		bs.Name,
		COUNT(bs.blade_shape_id) AS "count",
		ROUND((COUNT(bs.blade_shape_id) * 100.0 / (SELECT COUNT(*) FROM stabby_web_blade b2 LEFT JOIN stabby_web_knife k2 ON k2.knife_id = b2.knife_id AND k2.is_active = TRUE WHERE b2.is_active = true)), 2) AS percentage
	FROM 
		stabby_web_blade b
	LEFT JOIN 
		stabby_web_knife k ON k.knife_id = b.knife_id 
	LEFT JOIN 
		stabby_web_bladeshape bs ON bs.blade_shape_id = b.blade_shape_id 
	WHERE 
		b.is_active = TRUE 
		AND k.is_active = TRUE
	GROUP BY 
		bs.Name
	ORDER BY 
		"count" DESC, 
		bs.name;
		
GRANT SELECT ON view_blade_shape_chart TO db;