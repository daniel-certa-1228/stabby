DROP VIEW IF EXISTS view_vendor_chart;

CREATE VIEW view_vendor_chart AS
	SELECT
	    CASE 
		    WHEN 
		    	v.name IS NOT NULL 
		    THEN 
		    	v.name 
		    ELSE
		    	'Unknown' 
		END AS "name",
	    COUNT(k.knife_id) AS "count",
	    ROUND((COUNT(k.knife_id) * 100.0 / (SELECT COUNT(*) FROM stabby_web_knife WHERE is_active = true)), 2) AS percentage
	FROM 
		stabby_web_knife k
	LEFT JOIN 
		stabby_web_vendor v ON v.vendor_id  = k.vendor_id  
	WHERE 
		k.is_active = true
	GROUP BY 
		v.name
	ORDER BY 
		"count" DESC, 
		v.name;
		
GRANT SELECT ON view_vendor_chart TO stabby_app;