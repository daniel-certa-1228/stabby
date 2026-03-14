DROP VIEW IF EXISTS view_needs_work_chart;

CREATE VIEW view_needs_work_chart AS
SELECT 
	"name",
	"count",
	ROUND(("count" * 100.0 / (SELECT COUNT(*) FROM stabby_web_knife WHERE is_active = TRUE)), 2) AS percentage
FROM (
	SELECT 
		'Needs Work' AS "name",
		count(*) 
	FROM stabby_web_knife k
	WHERE 
		k.is_active = TRUE
		AND k.needs_work  = TRUE
	UNION ALL 
	SELECT 
		'Good To Go' AS "name",
		count(*) 
	FROM stabby_web_knife k
	WHERE 
		k.is_active = TRUE
		AND k.needs_work = False
) a
ORDER BY
	"count" DESC;
		
GRANT SELECT ON view_needs_work_chart TO db;