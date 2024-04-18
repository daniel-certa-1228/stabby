DROP VIEW IF EXISTS view_knife_grid;

CREATE VIEW IF NOT EXISTS view_knife_grid AS
	SELECT
		k.knife_id,
		k.name AS knife,
		kt.name AS knife_type,
		b.name AS brand,
		COUNT(CASE WHEN bl.blade_id IS NOT NULL THEN bl.blade_id ELSE NULL END) AS num_of_blades,
		bm.name AS blade_material,
		hm.name AS handle_material,
		lt.name AS lock_type,
		dt.name AS deployment_type,
		c.name AS country,
		v.name  AS vendor,
		k.needs_work,
		k.is_active,
		k.user_id
	FROM stabby_web_knife k
	LEFT JOIN stabby_web_brand b on b.brand_id = k.brand_id 
	LEFT JOIN stabby_web_bladematerial bm on bm.blade_material_id = k.blade_material_id
	LEFT JOIN stabby_web_locktype lt on lt.lock_type_id  = k.lock_type_id 
	LEFT JOIN stabby_web_deploymenttype dt on dt.deployment_type_id = k.deployment_type_id
	LEFT JOIN stabby_web_country c on c.country_id = k.country_id 
	LEFT JOIN stabby_web_handlematerial hm on hm.handle_material_id = k.handle_material_id
	LEFT JOIN stabby_web_vendor v on v.vendor_id = k.vendor_id
	LEFT JOIN stabby_web_knifetype kt on kt.knife_type_id = k.knife_type_id
	LEFT JOIN stabby_web_blade bl on bl.knife_id = k.knife_id
	GROUP BY
		k.knife_id,
		k.name,
		kt.name,
		b.name,
		bm.name,
		hm.name,
		lt.name,
		dt.name,
		c.name,
		v.name,
		k.needs_work,
		k.is_active,
		k.user_id

