DROP VIEW IF EXISTS view_deployment_type_chart;

CREATE VIEW view_deployment_type_chart AS
	SELECT
	    CASE WHEN dt.name IS NOT NULL THEN dt.name ELSE 'Unknown' END AS "name",
	    COUNT(k.knife_id) AS "count",
	    ROUND((COUNT(k.knife_id) * 100.0 / (SELECT COUNT(*) FROM stabby_web_knife WHERE is_active = true)), 2) AS percentage
	FROM 
		stabby_web_knife k
	LEFT JOIN 
		stabby_web_deploymenttype dt ON dt.deployment_type_id  = k.deployment_type_id  
	WHERE 
		k.is_active = true
	GROUP BY 
		dt.name
	ORDER BY 
		"count" DESC, 
	dt.name;
		
GRANT SELECT ON view_deployment_type_chart TO db;