DROP VIEW IF EXISTS view_blade_grid;

CREATE VIEW IF NOT EXISTS view_blade_grid AS
	SELECT 
		b.blade_id,
		b.knife_id,
		sh.name blade_shape,
		CAST(
			(CASE 
				WHEN 
					b."length" IS NOT NULL 
				THEN 
					CAST(b."length" AS TEXT) 
				ELSE '' 
			END 
			|| 
			CASE 	
				WHEN 
					uom.uom_id IS NOT NULL 
				THEN 
					' ' || uom.name
				ELSE ''
			END) AS TEXT) as "length",
			CAST(
			(CASE 
				WHEN 
					b."length_cutting_edge" IS NOT NULL 
				THEN 
					CAST(b."length_cutting_edge" AS TEXT) 
				ELSE '' 
			END 
			|| 
			CASE 	
				WHEN 
					uom.uom_id IS NOT NULL 
				THEN 
					' ' || uom.name
				ELSE ''
			END) AS TEXT) as "length_cutting_edge",
		b.has_half_stop,
		b.is_main_blade,
		b.is_active 
	FROM stabby_web_blade b
	LEFT JOIN stabby_web_unitofmeasure uom ON uom.uom_id = b.uom_id 
	LEFT JOIN stabby_web_bladeshape sh ON sh.blade_shape_id = b.blade_shape_id 
