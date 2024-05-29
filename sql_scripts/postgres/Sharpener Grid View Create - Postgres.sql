DROP VIEW IF EXISTS view_sharpener_grid;

CREATE VIEW view_sharpener_grid AS
    SELECT 
        sh.sharpener_id,
        sh.name AS sharpener,
        br.name AS brand,
        ca.name AS cutting_agent,
        ba.name AS bonding_agent,
        CAST(
            (CASE 
                WHEN sh."length" IS NOT NULL 
                THEN CAST(sh."length"::REAL AS TEXT) 
                ELSE '' 
            END 
            || 
            CASE 
                WHEN uom.uom_id IS NOT NULL 
                THEN ' ' || uom.name
                ELSE ''
            END) AS TEXT) AS "length",
        CAST(
            (CASE 
                WHEN sh."width" IS NOT NULL 
                THEN CAST(sh."width"::REAL AS TEXT) 
                ELSE '' 
            END 
            || 
            CASE 
                WHEN uom.uom_id IS NOT NULL 
                THEN ' ' || uom.name
                ELSE ''
            END) AS TEXT) AS "width",
        c.name AS country,
        ba.is_friable,
        sh.is_active,
        sh.user_id
    FROM stabby_web_sharpener sh
    LEFT JOIN stabby_web_brand br ON br.brand_id = sh.brand_id
    LEFT JOIN stabby_web_cuttingagent ca ON ca.cutting_agent_id = sh.cutting_agent_id 
    LEFT JOIN stabby_web_bondingagent ba ON ba.bonding_agent_id = sh.bonding_agent_id
    LEFT JOIN stabby_web_lubricant lu ON lu.lubricant_id = sh.lubricant_id
    LEFT JOIN stabby_web_unitofmeasure uom ON uom.uom_id = sh.uom_id
    LEFT JOIN stabby_web_country c ON c.country_id = sh.country_id;