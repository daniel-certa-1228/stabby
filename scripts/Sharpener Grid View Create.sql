DROP VIEW IF EXISTS view_sharpener_grid;

CREATE VIEW IF NOT EXISTS view_sharpener_grid AS
	SELECT 
		sh.sharpener_id,
		sh.name AS sharpener,
		br.name AS brand,
		ca.name AS cutting_agent,
		ba.name AS bonding_agent_id,
		CAST(
		(CASE 
			WHEN 
				sh."length" IS NOT NULL 
			THEN 
				CAST(sh."length" AS TEXT) 
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
				sh."width" IS NOT NULL 
			THEN 
				CAST(sh."width" AS TEXT) 
			ELSE '' 
		END 
		|| 
		CASE 	
			WHEN 
				uom.uom_id IS NOT NULL 
			THEN 
				' ' || uom.name
			ELSE ''
		END) AS TEXT) as "width",
		ba.is_friable
	FROM stabby_web_sharpener sh
	LEFT JOIN stabby_web_brand br on br.brand_id = sh.brand_id
	LEFT JOIN stabby_web_cuttingagent ca on ca.cutting_agent_id = sh.cutting_agent_id 
	LEFT JOIN stabby_web_bondingagent ba on ba.bonding_agent_id = sh.bonding_agent_id
	LEFT JOIN stabby_web_lubricant lu on lu.lubricant_id = sh.lubricant_id
	LEFT JOIN stabby_web_unitofmeasure uom on uom.uom_id = sh.uom_id