BEGIN TRANSACTION;

-- BLADE SHAPE
INSERT INTO stabby_web_bladeshape(blade_shape_id, name) VALUES(	1, 'Cleaver');
INSERT INTO stabby_web_bladeshape(blade_shape_id, name) VALUES(	2, 'Clip Point');
INSERT INTO stabby_web_bladeshape(blade_shape_id, name) VALUES(	3, 'Drop Point');
INSERT INTO stabby_web_bladeshape(blade_shape_id, name) VALUES(	4, 'Hawkbill');
INSERT INTO stabby_web_bladeshape(blade_shape_id, name) VALUES(	5, 'Leaf');
INSERT INTO stabby_web_bladeshape(blade_shape_id, name) VALUES(	6, 'Pen');
INSERT INTO stabby_web_bladeshape(blade_shape_id, name) VALUES(	7, 'Recurve');
INSERT INTO stabby_web_bladeshape(blade_shape_id, name) VALUES(	8, 'Reverse Tanto');
INSERT INTO stabby_web_bladeshape(blade_shape_id, name) VALUES(	9, 'Sheepsfoot');
INSERT INTO stabby_web_bladeshape(blade_shape_id, name) VALUES(	10, 'Spear Point');
INSERT INTO stabby_web_bladeshape(blade_shape_id, name) VALUES(	11, 'Tanto');
INSERT INTO stabby_web_bladeshape(blade_shape_id, name) VALUES(	12, 'Turkish Clip');
INSERT INTO stabby_web_bladeshape(blade_shape_id, name) VALUES(	13, 'Upswept');
INSERT INTO stabby_web_bladeshape(blade_shape_id, name) VALUES(	14, 'Wharncliff');

-- BONDING AGENT
INSERT INTO stabby_web_bondingagent(bonding_agent_id, name, is_friable) VALUES(1, 'Ceramic (Friable)', 1);
INSERT INTO stabby_web_bondingagent(bonding_agent_id, name, is_friable) VALUES(2, 'Ceramic (Non-Friable)', 0);
INSERT INTO stabby_web_bondingagent(bonding_agent_id, name, is_friable) VALUES(3, 'Steel Plate', 0);

-- COUNTRY
INSERT INTO stabby_web_country(country_id, name, code) VALUES(1, 'Austria', 'AUT');
INSERT INTO stabby_web_country(country_id, name, code) VALUES(2, 'China', 'CHN');
INSERT INTO stabby_web_country(country_id, name, code) VALUES(3, 'Czech Republic', 'CZE');
INSERT INTO stabby_web_country(country_id, name, code) VALUES(4, 'England', 'GBR');
INSERT INTO stabby_web_country(country_id, name, code) VALUES(5, 'France', 'FRA');
INSERT INTO stabby_web_country(country_id, name, code) VALUES(6, 'Germany', 'DEU');
INSERT INTO stabby_web_country(country_id, name, code) VALUES(7, 'Hong Kong', 'HKG');
INSERT INTO stabby_web_country(country_id, name, code) VALUES(8, 'Italy', 'ITA');
INSERT INTO stabby_web_country(country_id, name, code) VALUES(9, 'Japan', 'JPN');
INSERT INTO stabby_web_country(country_id, name, code) VALUES(10, 'New Zealand', 'NZL');
INSERT INTO stabby_web_country(country_id, name, code) VALUES(11, 'Portugal', 'PRT');
INSERT INTO stabby_web_country(country_id, name, code) VALUES(12, 'South Africa', 'ZAF');
INSERT INTO stabby_web_country(country_id, name, code) VALUES(13, 'Sweden', 'SWE');
INSERT INTO stabby_web_country(country_id, name, code) VALUES(14, 'Switzerland', 'CHE');
INSERT INTO stabby_web_country(country_id, name, code) VALUES(15, 'Taiwan', 'TWN');
INSERT INTO stabby_web_country(country_id, name, code) VALUES(16, 'U.S.A.', 'USA');

-- CUTTING AGENT
INSERT INTO stabby_web_cuttingagent(cutting_agent_id, name) VALUES(1, 'Alumina Oxide');
INSERT INTO stabby_web_cuttingagent(cutting_agent_id, name) VALUES(2, 'Diamond');
INSERT INTO stabby_web_cuttingagent(cutting_agent_id, name) VALUES(3, 'Silicon Carbide');

-- DEPLOYMENT TYPE
INSERT INTO stabby_web_deploymenttype(deployment_type_id, name) VALUES(1, 'Flipper');
INSERT INTO stabby_web_deploymenttype(deployment_type_id, name) VALUES(2, 'Nail Nick');
INSERT INTO stabby_web_deploymenttype(deployment_type_id, name) VALUES(3, 'Pinch');
INSERT INTO stabby_web_deploymenttype(deployment_type_id, name) VALUES(4, 'Slide');
INSERT INTO stabby_web_deploymenttype(deployment_type_id, name) VALUES(5, 'Thumb Hole');
INSERT INTO stabby_web_deploymenttype(deployment_type_id, name) VALUES(6, 'Thumb Stud');

-- HANDLE MATERIAL
INSERT INTO stabby_web_handlematerial(handle_material_id, name) VALUES(1, 'Aluminum');
INSERT INTO stabby_web_handlematerial(handle_material_id, name) VALUES(2,' Beech Wood');
INSERT INTO stabby_web_handlematerial(handle_material_id, name) VALUES(3, 'Brass');
INSERT INTO stabby_web_handlematerial(handle_material_id, name) VALUES(4, 'Bronze');
INSERT INTO stabby_web_handlematerial(handle_material_id, name) VALUES(5, 'Burlwood');
INSERT INTO stabby_web_handlematerial(handle_material_id, name) VALUES(6, 'Carbon Fiber');
INSERT INTO stabby_web_handlematerial(handle_material_id, name) VALUES(7, 'Cellidor');
INSERT INTO stabby_web_handlematerial(handle_material_id, name) VALUES(8, 'Cocobolo');
INSERT INTO stabby_web_handlematerial(handle_material_id, name) VALUES(9, 'Copper');
INSERT INTO stabby_web_handlematerial(handle_material_id, name) VALUES(10, 'Corelon');
INSERT INTO stabby_web_handlematerial(handle_material_id, name) VALUES(11, 'Delrin');
INSERT INTO stabby_web_handlematerial(handle_material_id, name) VALUES(12, 'Dymondwood');
INSERT INTO stabby_web_handlematerial(handle_material_id, name) VALUES(13, 'Ebony');
INSERT INTO stabby_web_handlematerial(handle_material_id, name) VALUES(14, 'Fat Carbon');
INSERT INTO stabby_web_handlematerial(handle_material_id, name) VALUES(15, 'FRN');
INSERT INTO stabby_web_handlematerial(handle_material_id, name) VALUES(16, 'G-10');
INSERT INTO stabby_web_handlematerial(handle_material_id, name) VALUES(17, 'GFN');
INSERT INTO stabby_web_handlematerial(handle_material_id, name) VALUES(18, 'Ironwood');
INSERT INTO stabby_web_handlematerial(handle_material_id, name) VALUES(19, 'Kirinite');
INSERT INTO stabby_web_handlematerial(handle_material_id, name) VALUES(20, 'Metal');
INSERT INTO stabby_web_handlematerial(handle_material_id, name) VALUES(21, 'Micarta');
INSERT INTO stabby_web_handlematerial(handle_material_id, name) VALUES(22, 'Mother of Pearl');
INSERT INTO stabby_web_handlematerial(handle_material_id, name) VALUES(23, 'Nylon');
INSERT INTO stabby_web_handlematerial(handle_material_id, name) VALUES(24, 'Oak');
INSERT INTO stabby_web_handlematerial(handle_material_id, name) VALUES(25, 'Olive Wood');
INSERT INTO stabby_web_handlematerial(handle_material_id, name) VALUES(26, 'Rosewood');
INSERT INTO stabby_web_handlematerial(handle_material_id, name) VALUES(27, 'Rubber');
INSERT INTO stabby_web_handlematerial(handle_material_id, name) VALUES(28, 'Shell (Metal)');
INSERT INTO stabby_web_handlematerial(handle_material_id, name) VALUES(29, 'Shell (Plastic over metal)');
INSERT INTO stabby_web_handlematerial(handle_material_id, name) VALUES(30, 'Stag');
INSERT INTO stabby_web_handlematerial(handle_material_id, name) VALUES(31, 'Steel');
INSERT INTO stabby_web_handlematerial(handle_material_id, name) VALUES(32, 'Stone');
INSERT INTO stabby_web_handlematerial(handle_material_id, name) VALUES(33, 'Synthetic');
INSERT INTO stabby_web_handlematerial(handle_material_id, name) VALUES(34, 'Titanium');
INSERT INTO stabby_web_handlematerial(handle_material_id, name) VALUES(35, 'Walnut');
INSERT INTO stabby_web_handlematerial(handle_material_id, name) VALUES(36, 'Wood');
INSERT INTO stabby_web_handlematerial(handle_material_id, name) VALUES(37, 'Zytel');

-- KNIFE TYPE
INSERT INTO stabby_web_knifetype(knife_type_id, name) VALUES(1, 'Castration Knife');
INSERT INTO stabby_web_knifetype(knife_type_id, name) VALUES(2, 'Congress');
INSERT INTO stabby_web_knifetype(knife_type_id, name) VALUES(3, 'Copperhead');
INSERT INTO stabby_web_knifetype(knife_type_id, name) VALUES(4, 'Copperlock');
INSERT INTO stabby_web_knifetype(knife_type_id, name) VALUES(5, 'Doctor''s Knife');
INSERT INTO stabby_web_knifetype(knife_type_id, name) VALUES(6, 'Elephant Toe');
INSERT INTO stabby_web_knifetype(knife_type_id, name) VALUES(7, 'Gunstock');
INSERT INTO stabby_web_knifetype(knife_type_id, name) VALUES(8, 'Jack');
INSERT INTO stabby_web_knifetype(knife_type_id, name) VALUES(9, 'Laguiole');
INSERT INTO stabby_web_knifetype(knife_type_id, name) VALUES(10, 'Large Stockman');
INSERT INTO stabby_web_knifetype(knife_type_id, name) VALUES(11, 'MIL-K-818');
INSERT INTO stabby_web_knifetype(knife_type_id, name) VALUES(12, 'Muskrat');
INSERT INTO stabby_web_knifetype(knife_type_id, name) VALUES(13, 'Neck Knife');
INSERT INTO stabby_web_knifetype(knife_type_id, name) VALUES(14, 'Peanut');
INSERT INTO stabby_web_knifetype(knife_type_id, name) VALUES(15, 'Peasant Knife');
INSERT INTO stabby_web_knifetype(knife_type_id, name) VALUES(16, 'Pen');
INSERT INTO stabby_web_knifetype(knife_type_id, name) VALUES(17, 'Razor');
INSERT INTO stabby_web_knifetype(knife_type_id, name) VALUES(18, 'Scout Knife');
INSERT INTO stabby_web_knifetype(knife_type_id, name) VALUES(19, 'Sowbelly');
INSERT INTO stabby_web_knifetype(knife_type_id, name) VALUES(20, 'Stockman');
INSERT INTO stabby_web_knifetype(knife_type_id, name) VALUES(21, 'Swayback');
INSERT INTO stabby_web_knifetype(knife_type_id, name) VALUES(22, 'Swiss Army Knife');
INSERT INTO stabby_web_knifetype(knife_type_id, name) VALUES(23, 'Toothpick');
INSERT INTO stabby_web_knifetype(knife_type_id, name) VALUES(24, 'Trapper');
INSERT INTO stabby_web_knifetype(knife_type_id, name) VALUES(25, 'Whittler');

-- LOCK TYPE
INSERT INTO stabby_web_locktype(lock_type_id, name) VALUES(1, 'Button Lock');
INSERT INTO stabby_web_locktype(lock_type_id, name) VALUES(2, 'Detent');
INSERT INTO stabby_web_locktype(lock_type_id, name) VALUES(3, 'Frame Lock');
INSERT INTO stabby_web_locktype(lock_type_id, name) VALUES(4, 'Friction');
INSERT INTO stabby_web_locktype(lock_type_id, name) VALUES(5, 'Liner Lock');
INSERT INTO stabby_web_locktype(lock_type_id, name) VALUES(6, 'Lockback');
INSERT INTO stabby_web_locktype(lock_type_id, name) VALUES(7, 'Locking Ring');
INSERT INTO stabby_web_locktype(lock_type_id, name) VALUES(8, 'Ratchet Lock');
INSERT INTO stabby_web_locktype(lock_type_id, name) VALUES(9, 'Slip Joint');

-- LUBRICANT
INSERT INTO stabby_web_lubricant(lubricant_id, name) VALUES(1, 'None');
INSERT INTO stabby_web_lubricant(lubricant_id, name) VALUES(2, 'Oil');
INSERT INTO stabby_web_lubricant(lubricant_id, name) VALUES(3, 'Water');

-- STEEL TYPE
INSERT INTO stabby_web_steeltype(steel_type_id, name) VALUES(1, 'Stainless');
INSERT INTO stabby_web_steeltype(steel_type_id, name) VALUES(2, 'Carbon');


-- UOM
INSERT INTO stabby_web_unitofmeasure(uom_id, name)VALUES(1, 'in');
INSERT INTO stabby_web_unitofmeasure(uom_id, name)VALUES(2, 'cm');

-- VENDOR
INSERT INTO stabby_web_vendor(vendor_id, name) VALUES(1, 'Baryonyx Knife Company');
INSERT INTO stabby_web_vendor(vendor_id, name) VALUES(2, 'BladeHQ');
INSERT INTO stabby_web_vendor(vendor_id, name) VALUES(3, 'C. Risner Cutlery');
INSERT INTO stabby_web_vendor(vendor_id, name) VALUES(4, 'Chicago Knife Works');
INSERT INTO stabby_web_vendor(vendor_id, name) VALUES(5, 'Collector Knives');
INSERT INTO stabby_web_vendor(vendor_id, name) VALUES(6, 'Deadwood Knives');
INSERT INTO stabby_web_vendor(vendor_id, name) VALUES(7, 'Direct From Manufacturer');
INSERT INTO stabby_web_vendor(vendor_id, name) VALUES(8, 'DLT');
INSERT INTO stabby_web_vendor(vendor_id, name) VALUES(9, 'Ebay');
INSERT INTO stabby_web_vendor(vendor_id, name) VALUES(10, 'Knifecenter');
INSERT INTO stabby_web_vendor(vendor_id, name) VALUES(11, 'Knives Plus');
INSERT INTO stabby_web_vendor(vendor_id, name) VALUES(12, 'Red Hill Cutlery');
INSERT INTO stabby_web_vendor(vendor_id, name) VALUES(13, 'Shadow Hills Cutlery');
INSERT INTO stabby_web_vendor(vendor_id, name) VALUES(14, 'Smokey Mountain Knife Works');
INSERT INTO stabby_web_vendor(vendor_id, name) VALUES(15, 'Swiss Army Flagship - London');
INSERT INTO stabby_web_vendor(vendor_id, name) VALUES(16, 'Swiss Knife Shop');

COMMIT;

BEGIN TRANSACTION;

-- BRAND
INSERT INTO stabby_web_brand(brand_id, name) VALUES(1, 'Antonini Knives');
INSERT INTO stabby_web_brand(brand_id, name) VALUES(2, 'Camillus (U.S.A.)');
INSERT INTO stabby_web_brand(brand_id, name) VALUES(3, 'Imperial (U.S.A.)');
INSERT INTO stabby_web_brand(brand_id, name) VALUES(4, 'M.C. Cognet');
INSERT INTO stabby_web_brand(brand_id, name) VALUES(5, 'Otter');
INSERT INTO stabby_web_brand(brand_id, name) VALUES(6, 'Richartz');
INSERT INTO stabby_web_brand(brand_id, name) VALUES(7, 'Smokey Mountain Knife Works');
INSERT INTO stabby_web_brand(brand_id, name) VALUES(8, 'Schrade');
INSERT INTO stabby_web_brand(brand_id, name) VALUES(9, 'United Cutlery');
INSERT INTO stabby_web_brand(brand_id, name) VALUES(10, 'Utica');
INSERT INTO stabby_web_brand(brand_id, name) VALUES(11, 'Zippo');
INSERT INTO stabby_web_brand(brand_id, name) VALUES(12, 'A.G. Russell');
INSERT INTO stabby_web_brand(brand_id, name) VALUES(13, 'Advanced Knife Bro');
INSERT INTO stabby_web_brand(brand_id, name) VALUES(14, 'Baryonyx Knife Co.');
INSERT INTO stabby_web_brand(brand_id, name) VALUES(15, 'Beretta');
INSERT INTO stabby_web_brand(brand_id, name) VALUES(16, 'Buck');
INSERT INTO stabby_web_brand(brand_id, name, parent_brand_id) VALUES(17, 'Case', 11);
INSERT INTO stabby_web_brand(brand_id, name) VALUES(18, 'Cold Steel');
INSERT INTO stabby_web_brand(brand_id, name) VALUES(19, 'Colonial');
INSERT INTO stabby_web_brand(brand_id, name) VALUES(20,'Columbia River Knife & Tool');
INSERT INTO stabby_web_brand(brand_id, name) VALUES(21, 'DMT');
INSERT INTO stabby_web_brand(brand_id, name, parent_brand_id) VALUES(22, 'Douk Douk', 4);
INSERT INTO stabby_web_brand(brand_id, name) VALUES(23, 'Eurstache');
INSERT INTO stabby_web_brand(brand_id, name) VALUES(24, 'Fox');
INSERT INTO stabby_web_brand(brand_id, name) VALUES(25, 'Frost');
INSERT INTO stabby_web_brand(brand_id, name) VALUES(26, 'G.David');
INSERT INTO stabby_web_brand(brand_id, name) VALUES(27, 'Great Eastern Cutlery');
INSERT INTO stabby_web_brand(brand_id, name, parent_brand_id) VALUES(28, 'Hammer Brand', 3);
INSERT INTO stabby_web_brand(brand_id, name, parent_brand_id) VALUES(29, 'Hibben Knives', 9);
INSERT INTO stabby_web_brand(brand_id, name) VALUES(30, 'Higonokami');
INSERT INTO stabby_web_brand(brand_id, name, parent_brand_id) VALUES(31, 'Imperial', 8);
INSERT INTO stabby_web_brand(brand_id, name) VALUES(32, 'IXL');
INSERT INTO stabby_web_brand(brand_id, name) VALUES(33, 'KA-BAR');
INSERT INTO stabby_web_brand(brand_id, name) VALUES(34, 'Kershaw');
INSERT INTO stabby_web_brand(brand_id, name, parent_brand_id) VALUES(35, 'Kingston', 3);
INSERT INTO stabby_web_brand(brand_id, name) VALUES(36, 'Knives Plus');
INSERT INTO stabby_web_brand(brand_id, name, parent_brand_id) VALUES(37, 'Kutmaster', 10);
INSERT INTO stabby_web_brand(brand_id, name) VALUES(38, 'lionSTEEL');
INSERT INTO stabby_web_brand(brand_id, name) VALUES(39, 'MAM');
INSERT INTO stabby_web_brand(brand_id, name) VALUES(40, 'Marble''s');
INSERT INTO stabby_web_brand(brand_id, name, parent_brand_id) VALUES(41, 'Mercator', 4);
INSERT INTO stabby_web_brand(brand_id, name) VALUES(42, 'Mikov');
INSERT INTO stabby_web_brand(brand_id, name) VALUES(43, 'Novelty Cutlery');
INSERT INTO stabby_web_brand(brand_id, name) VALUES(44, 'Okapi');
INSERT INTO stabby_web_brand(brand_id, name, parent_brand_id) VALUES(45, 'Old Bear', 1);
INSERT INTO stabby_web_brand(brand_id, name, parent_brand_id) VALUES(46, 'Old Timer',8) ;
INSERT INTO stabby_web_brand(brand_id, name) VALUES(47, 'Ontario Knife Company');
INSERT INTO stabby_web_brand(brand_id, name) VALUES(48, 'Opinel');
INSERT INTO stabby_web_brand(brand_id, name) VALUES(49, 'Parker Cut Co.');
INSERT INTO stabby_web_brand(brand_id, name, parent_brand_id) VALUES(50, 'Pierre Cardin', 5);
INSERT INTO stabby_web_brand(brand_id, name, parent_brand_id) VALUES(51, 'Queen	', 7);
INSERT INTO stabby_web_brand(brand_id, name) VALUES(52, 'Queen (U.S.A.)');
INSERT INTO stabby_web_brand(brand_id, name, parent_brand_id) VALUES(53, 'Queen City', 7);
INSERT INTO stabby_web_brand(brand_id, name) VALUES(54, 'Richards');
INSERT INTO stabby_web_brand(brand_id, name) VALUES(55, 'Rosecraft');
INSERT INTO stabby_web_brand(brand_id, name, parent_brand_id) VALUES(56, 'Rough Ryder', 7);
INSERT INTO stabby_web_brand(brand_id, name, parent_brand_id) VALUES(57, 'Schrade (U.S.A.)', 2);
INSERT INTO stabby_web_brand(brand_id, name) VALUES(58, 'Sharpening Supplies');
INSERT INTO stabby_web_brand(brand_id, name, parent_brand_id) VALUES(59, 'Spyderco');
INSERT INTO stabby_web_brand(brand_id, name) VALUES(60, 'Stephenson');
INSERT INTO stabby_web_brand(brand_id, name) VALUES(61, 'Svord');
INSERT INTO stabby_web_brand(brand_id, name) VALUES(62, 'Swiza');
INSERT INTO stabby_web_brand(brand_id, name) VALUES(63, 'Syracuse Knife Company');
INSERT INTO stabby_web_brand(brand_id, name, parent_brand_id) VALUES(64, 'Ulster', 3);
INSERT INTO stabby_web_brand(brand_id, name) VALUES(65, 'Ultratech');
INSERT INTO stabby_web_brand(brand_id, name, ) VALUES(66, 'Uncle Henry', 8);
INSERT INTO stabby_web_brand(brand_id, name) VALUES(67, 'Unknown');
INSERT INTO stabby_web_brand(brand_id, name) VALUES(68, 'Victorinox');
INSERT INTO stabby_web_brand(brand_id, name) VALUES(69, 'Viper');
INSERT INTO stabby_web_brand(brand_id, name) VALUES(70, 'Watchmen Brother');
INSERT INTO stabby_web_brand(brand_id, name) VALUES(71, 'Wenger');
INSERT INTO stabby_web_brand(brand_id, name, parent_brand_id) VALUES(72, 'Western (U.S.A)', 2);

-- STEEL MANUFACTURER
INSERT INTO stabby_web_steelmanufacturer(steel_manufacturer_id, name, country_id) VALUES(1, 'Bohler', 1);
INSERT INTO stabby_web_steelmanufacturer(steel_manufacturer_id, name, country_id) VALUES(2, 'Carpenter', 16);
INSERT INTO stabby_web_steelmanufacturer(steel_manufacturer_id, name, country_id) VALUES(3, 'Crucible', 16);
INSERT INTO stabby_web_steelmanufacturer(steel_manufacturer_id, name, country_id) VALUES(4, 'Hitachi', 9);
INSERT INTO stabby_web_steelmanufacturer(steel_manufacturer_id, name, country_id) VALUES(5, 'Sandvik', 13);
INSERT INTO stabby_web_steelmanufacturer(steel_manufacturer_id, name, country_id) VALUES(6, 'Uddeholm', 13);

-- BLADE MATERIAL
INSERT INTO stabby_web_bladematerial(blade_material_id, steel_type_id, steel_manufacturer_id, name) VALUES(1, 2, null, '1065');
INSERT INTO stabby_web_bladematerial(blade_material_id, steel_type_id, steel_manufacturer_id, name) VALUES(2, 2, null, '1075');
INSERT INTO stabby_web_bladematerial(blade_material_id, steel_type_id, steel_manufacturer_id, name) VALUES(3, 2, null, '1085');
INSERT INTO stabby_web_bladematerial(blade_material_id, steel_type_id, steel_manufacturer_id, name) VALUES(4, 2, null, '1095');
INSERT INTO stabby_web_bladematerial(blade_material_id, steel_type_id, steel_manufacturer_id, name) VALUES(5, 2, null, '1095 Cro Van');
INSERT INTO stabby_web_bladematerial(blade_material_id, steel_type_id, steel_manufacturer_id, name) VALUES(6, 1, 4, '12C27');
INSERT INTO stabby_web_bladematerial(blade_material_id, steel_type_id, steel_manufacturer_id, name) VALUES(7, 1, 4, '14C28N');
INSERT INTO stabby_web_bladematerial(blade_material_id, steel_type_id, steel_manufacturer_id, name) VALUES(8, 1, 3, '154CM');
INSERT INTO stabby_web_bladematerial(blade_material_id, steel_type_id, steel_manufacturer_id, name) VALUES(9, 1, null, '3Cr13MoV');
INSERT INTO stabby_web_bladematerial(blade_material_id, steel_type_id, steel_manufacturer_id, name) VALUES(10, 1, null, '420');
INSERT INTO stabby_web_bladematerial(blade_material_id, steel_type_id, steel_manufacturer_id, name) VALUES(11, 1, null, '420HC');
INSERT INTO stabby_web_bladematerial(blade_material_id, steel_type_id, steel_manufacturer_id, name) VALUES(12, 1, null, '425M');
INSERT INTO stabby_web_bladematerial(blade_material_id, steel_type_id, steel_manufacturer_id, name) VALUES(13, 1, null, '440A');
INSERT INTO stabby_web_bladematerial(blade_material_id, steel_type_id, steel_manufacturer_id, name) VALUES(14, 1, null, '440B');
INSERT INTO stabby_web_bladematerial(blade_material_id, steel_type_id, steel_manufacturer_id, name) VALUES(15, 1, null, '440C');
INSERT INTO stabby_web_bladematerial(blade_material_id, steel_type_id, steel_manufacturer_id, name) VALUES(16, 1, null, '5Cr15MoV');
INSERT INTO stabby_web_bladematerial(blade_material_id, steel_type_id, steel_manufacturer_id, name) VALUES(17, 1, null, '7Cr17MoV');
INSERT INTO stabby_web_bladematerial(blade_material_id, steel_type_id, steel_manufacturer_id, name) VALUES(18, 1, null, '8Cr13MoV');
INSERT INTO stabby_web_bladematerial(blade_material_id, steel_type_id, steel_manufacturer_id, name) VALUES(19, 1, null, '9Cr18MoV');
INSERT INTO stabby_web_bladematerial(blade_material_id, steel_type_id, steel_manufacturer_id, name) VALUES(20, 1, 5, 'AEB-L');
INSERT INTO stabby_web_bladematerial(blade_material_id, steel_type_id, steel_manufacturer_id, name) VALUES(21, 1, null, 'AUS-10');
INSERT INTO stabby_web_bladematerial(blade_material_id, steel_type_id, steel_manufacturer_id, name) VALUES(22, 1, null, 'AUS-6');
INSERT INTO stabby_web_bladematerial(blade_material_id, steel_type_id, steel_manufacturer_id, name) VALUES(23, 1, null, 'AUS-8');
INSERT INTO stabby_web_bladematerial(blade_material_id, steel_type_id, steel_manufacturer_id, name) VALUES(24, 2, 4, 'Blue Paper Steel (Blue Super)');
INSERT INTO stabby_web_bladematerial(blade_material_id, steel_type_id, steel_manufacturer_id, name) VALUES(25, 2, null, 'C67');
INSERT INTO stabby_web_bladematerial(blade_material_id, steel_type_id, steel_manufacturer_id, name) VALUES(26, 2, null, 'Case Chrome Vanadium');
INSERT INTO stabby_web_bladematerial(blade_material_id, steel_type_id, steel_manufacturer_id, name) VALUES(27, 1, null, 'Case Tru Sharp Surgical Steel');
INSERT INTO stabby_web_bladematerial(blade_material_id, steel_type_id, steel_manufacturer_id, name) VALUES(28, null, null, 'Ceramic');
INSERT INTO stabby_web_bladematerial(blade_material_id, steel_type_id, steel_manufacturer_id, name) VALUES(29, 1, null, 'CPM MagnaCut');
INSERT INTO stabby_web_bladematerial(blade_material_id, steel_type_id, steel_manufacturer_id, name) VALUES(30, 2, 3, 'CPM-3V');
INSERT INTO stabby_web_bladematerial(blade_material_id, steel_type_id, steel_manufacturer_id, name) VALUES(31, 2, 3, 'CPM-M4');
INSERT INTO stabby_web_bladematerial(blade_material_id, steel_type_id, steel_manufacturer_id, name) VALUES(32, 1, 3, 'CPM-S30V');
INSERT INTO stabby_web_bladematerial(blade_material_id, steel_type_id, steel_manufacturer_id, name) VALUES(33, 1, 3, 'CPM-S35VN');
INSERT INTO stabby_web_bladematerial(blade_material_id, steel_type_id, steel_manufacturer_id, name) VALUES(34, 2, 3, 'CruWear');
INSERT INTO stabby_web_bladematerial(blade_material_id, steel_type_id, steel_manufacturer_id, name) VALUES(35, 1, 2, 'CTS-BD1N');
INSERT INTO stabby_web_bladematerial(blade_material_id, steel_type_id, steel_manufacturer_id, name) VALUES(36, 1, 2, 'CTS-XHP');
INSERT INTO stabby_web_bladematerial(blade_material_id, steel_type_id, steel_manufacturer_id, name) VALUES(37, 2, null, 'D2');
INSERT INTO stabby_web_bladematerial(blade_material_id, steel_type_id, steel_manufacturer_id, name) VALUES(38, 1, 5, 'Elmax');
INSERT INTO stabby_web_bladematerial(blade_material_id, steel_type_id, steel_manufacturer_id, name) VALUES(39, 2, 1, 'K390');
INSERT INTO stabby_web_bladematerial(blade_material_id, steel_type_id, steel_manufacturer_id, name) VALUES(40, 1, 1, 'M390');
INSERT INTO stabby_web_bladematerial(blade_material_id, steel_type_id, steel_manufacturer_id, name) VALUES(41, 2, 2, 'Maxamet');
INSERT INTO stabby_web_bladematerial(blade_material_id, steel_type_id, steel_manufacturer_id, name) VALUES(42, 1, 1, 'N690');
INSERT INTO stabby_web_bladematerial(blade_material_id, steel_type_id, steel_manufacturer_id, name) VALUES(43, 2, null, 'T10');
INSERT INTO stabby_web_bladematerial(blade_material_id, steel_type_id, steel_manufacturer_id, name) VALUES(44, 2, null, 'Unknown Carbon Steel');
INSERT INTO stabby_web_bladematerial(blade_material_id, steel_type_id, steel_manufacturer_id, name) VALUES(45, 1, null, 'Unknown Stainless Steel');
INSERT INTO stabby_web_bladematerial(blade_material_id, steel_type_id, steel_manufacturer_id, name) VALUES(46, 1, null, 'VG-10');
INSERT INTO stabby_web_bladematerial(blade_material_id, steel_type_id, steel_manufacturer_id, name) VALUES(47, 2, 4, 'White Paper Steel (White #1)');
INSERT INTO stabby_web_bladematerial(blade_material_id, steel_type_id, steel_manufacturer_id, name) VALUES(48, 2, null, 'XC75');
INSERT INTO stabby_web_bladematerial(blade_material_id, steel_type_id, steel_manufacturer_id, name) VALUES(49, 2, null, 'XC90');

COMMIT;