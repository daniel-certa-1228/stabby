DROP VIEW IF EXISTS view_knife_type_chart;

CREATE VIEW view_knife_type_chart AS
	SELECT 
		CASE WHEN sub."type" IS NULL THEN 'Uncategorized' ELSE sub."type" END AS Type,
		COUNT(sub.*) "count",
		ROUND((COUNT(sub.knife_id) * 100.0 / (SELECT COUNT(*) FROM stabby_web_knife WHERE is_active = true)), 2) AS percentage,
		CASE WHEN sub.Type IS NOT NULL THEN url_encode(sub.Type) ELSE 'Unknown' END AS query_str
	FROM (
		SELECT 
			k.knife_id,
			b."name" Brand,
			k."name" Knife,
			t."name" Type
			-- *
		FROM stabby_web_knife k
		LEFT JOIN stabby_web_knifetype t ON t.knife_type_id = k.knife_type_id
		LEFT JOIN stabby_web_brand b ON b.brand_id = k.brand_id
		WHERE k.is_active = TRUE
	) sub
	GROUP BY sub.TYPE
	ORDER BY "count" DESC, "type";
	
GRANT SELECT ON view_knife_type_chart TO db;
