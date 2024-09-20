DROP VIEW IF EXISTS view_knife_blade_grid;

CREATE VIEW view_knife_blade_grid AS
	SELECT DISTINCT
		k.knife_id,
		bl.blade_shape_id,
		k.name AS knife,
		b.name AS brand,
		kt.name AS knife_type,
		COUNT(*) OVER (PARTITION BY k.knife_id) AS num_of_blades,
		CASE WHEN bm.steel_manufacturer_id IS NOT NULL THEN sm.name || ' ' || bm.name ELSE bm.name END AS blade_material,
	    hm.name AS handle_material,
	    lt.name AS lock_type,
	    dt.name AS deployment_type,
	    c.name AS country,
	    v.name AS vendor,
	    k.needs_work,
	    k.purchased_new,
	    k.is_active,
	    k.create_date,
	    k.user_id
	FROM
		stabby_web_blade bl
	LEFT JOIN
		stabby_web_knife k ON k.knife_id = bl.knife_id 
	LEFT JOIN
		stabby_web_brand b ON b.brand_id = k.brand_id 
	LEFT JOIN 
		stabby_web_bladematerial bm ON bm.blade_material_id = k.blade_material_id
	LEFT JOIN 
		stabby_web_steelmanufacturer sm ON sm.steel_manufacturer_id = bm.steel_manufacturer_id
	LEFT JOIN 
		stabby_web_locktype lt ON lt.lock_type_id = k.lock_type_id 
	LEFT JOIN 
		stabby_web_deploymenttype dt ON dt.deployment_type_id = k.deployment_type_id
	LEFT JOIN 
		stabby_web_country c ON c.country_id = k.country_id 
	LEFT JOIN 
		stabby_web_handlematerial hm ON hm.handle_material_id = k.handle_material_id
	LEFT JOIN 	
		stabby_web_vendor v ON v.vendor_id = k.vendor_id
	LEFT JOIN 
		stabby_web_knifetype kt ON kt.knife_type_id = k.knife_type_id
	WHERE 
		bl.is_active = TRUE
		AND k.is_active = TRUE;

GRANT SELECT ON view_knife_blade_grid TO db;