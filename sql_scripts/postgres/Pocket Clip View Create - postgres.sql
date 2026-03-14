DROP VIEW IF EXISTS view_pocket_clip_chart;

CREATE VIEW view_pocket_clip_chart AS
SELECT 
	"name",
	"count",
	ROUND(("count" * 100.0 / (SELECT COUNT(*) FROM stabby_web_knife WHERE is_active = TRUE)), 2) AS percentage
FROM (
	SELECT 
		'Clip' AS "name",
		count(*) 
	FROM stabby_web_knife k
	WHERE 
		k.is_active = TRUE
		AND k.has_pocket_clip  = TRUE
	UNION ALL 
	SELECT 
		'No Clip' AS "name",
		count(*) 
	FROM stabby_web_knife k
	WHERE 
		k.is_active = TRUE
		AND k.has_pocket_clip = False
) a
ORDER BY
	"count" DESC;
		
GRANT SELECT ON view_pocket_clip_chart TO db;