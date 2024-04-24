/*
 * ATTENTION: The "eval" devtool has been used (maybe by default in mode: "development").
 * This devtool is neither made for production nor for readable output files.
 * It uses "eval()" calls to create a separate source file in the browser devtools.
 * If you are trying to read the output file, select a different devtool (https://webpack.js.org/configuration/devtool/)
 * or disable the default devtool with "devtool: false".
 * If you are looking for production-ready output files, see mode: "production" (https://webpack.js.org/configuration/mode/).
 */
/******/ (() => { // webpackBootstrap
/******/ 	var __webpack_modules__ = ({

/***/ "./assets/scripts/index.js":
/*!*********************************!*\
  !*** ./assets/scripts/index.js ***!
  \*********************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

"use strict";
eval("__webpack_require__.r(__webpack_exports__);\n/* harmony import */ var _load_grids__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! ./load-grids */ \"./assets/scripts/load-grids.js\");\n/* harmony import */ var _load_grids__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_load_grids__WEBPACK_IMPORTED_MODULE_0__);\n/* harmony import */ var _styles_styles_css__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! ../styles/styles.css */ \"./assets/styles/styles.css\");\n\r\n\r\n\n\n//# sourceURL=webpack://stabby/./assets/scripts/index.js?");

/***/ }),

/***/ "./assets/scripts/load-grids.js":
/*!**************************************!*\
  !*** ./assets/scripts/load-grids.js ***!
  \**************************************/
/***/ (() => {

eval("document.addEventListener('DOMContentLoaded', function() {\r\n    const baseUrl = \"http://127.0.0.1:8000/api/\";\r\n    const location = removeIdFromUrl(window.location.pathname);\r\n    // knife grid\r\n    if (location[0] === '/') {\r\n        const gridDiv = document.querySelector('#grid');\r\n\r\n        const gridOptions = {\r\n            pagination: true,\r\n            defaultColDef: {\r\n                filter: true,\r\n                cellStyle: {textAlign: 'left'}\r\n              },\r\n            columnDefs: [\r\n                { \r\n                    headerName: '', \r\n                    width: 70, \r\n                    pinned: 'left', \r\n                    cellStyle: {textAlign: 'center'}, \r\n                    cellRenderer: (params) => {\r\n                        return `<button onclick=\"redirectToKnifeDetailPage(${params.data.knife_id})\" class=\"btn btn-sm btn-light\"><i class=\"fa-solid fa-magnifying-glass\"></i></button>`;\r\n                    }, \r\n                },\r\n                { headerName: 'Brand', field: 'brand', width: 220, pinned: 'left' },\r\n                { headerName: 'Knife', field: 'knife', width: 350, pinned: 'left' }, \r\n                { headerName: '# of Blades', field: 'num_of_blades', width: 120, cellStyle: {textAlign: 'right'} },\r\n                { headerName: 'Blade Material', field: 'blade_material', width: 250 },\r\n                { headerName: 'Handle Material', field: 'handle_material', width: 140 },\r\n                { headerName: 'Lock', field: 'lock_type', width: 120 },\r\n                { headerName: 'Deployment', field: 'deployment_type', width: 140 },\r\n                { headerName: 'Country', field: 'country', width: 140 },\r\n                { headerName: 'Vendor', field: 'vendor', width: 220 },\r\n                { headerName: 'Needs Work', field: 'needs_work', width: 140, cellStyle: {textAlign: 'center'} },\r\n            ]\r\n        };\r\n\r\n        const gridApi = agGrid.createGrid(gridDiv, gridOptions);\r\n\r\n        let xhr = new XMLHttpRequest();\r\n        xhr.open('GET', `${baseUrl}get_knife_grid`, true);\r\n        xhr.onreadystatechange = () => {\r\n            if (xhr.readyState === 4 && xhr.status === 200) {\r\n                var responseData = JSON.parse(xhr.responseText);\r\n                gridApi.setGridOption('rowData', responseData);\r\n            }\r\n        };\r\n        xhr.send();\r\n\r\n        redirectToKnifeDetailPage = (knife_id) => {\r\n            window.location.href = \"knives/detail/\" + knife_id; \r\n        }\r\n    }\r\n    // sharpener grid\r\n    if (location[0] === '/sharpeners/') {\r\n        const gridDiv = document.querySelector('#grid');\r\n\r\n        const gridOptions = {\r\n            defaultColDef: {\r\n                filter: true,\r\n                cellStyle: {textAlign: 'left'}\r\n              },\r\n            columnDefs: [\r\n                { \r\n                    headerName: '', \r\n                    width: 70, \r\n                    pinned: 'left', \r\n                    cellStyle: {textAlign: 'center'}, \r\n                    cellRenderer: (params) => {\r\n                        return `<button onclick=\"redirectToSharpenerDetailPage(${params.data.sharpener_id})\" class=\"btn btn-sm btn-light\"><i class=\"fa-solid fa-magnifying-glass\"></i></button>`;\r\n                    }, \r\n                },\r\n                { headerName: 'Brand', field: 'brand', width: 220, pinned: 'left' },\r\n                { headerName: 'Sharpener', field: 'sharpener', width: 350, pinned: 'left' }, \r\n                { headerName: 'Cutting Agent', field: 'cutting_agent', width: 160 },\r\n                { headerName: 'Bonding Agent', field: 'bonding_agent', width: 190 },\r\n                { headerName: 'Length', field: 'length', width: 120 },\r\n                { headerName: 'Width', field: 'width', width: 120 },\r\n                { headerName: 'Country', field: 'country', width: 140 },\r\n                { headerName: 'Friable', field: 'is_friable', width: 140, cellStyle: {textAlign: 'center'} },\r\n            ]\r\n        };\r\n\r\n        const gridApi = agGrid.createGrid(gridDiv, gridOptions);\r\n\r\n        let xhr = new XMLHttpRequest();\r\n        xhr.open('GET', `${baseUrl}get_sharpener_grid`, true);\r\n        xhr.onreadystatechange = () => {\r\n            if (xhr.readyState === 4 && xhr.status === 200) {\r\n                var responseData = JSON.parse(xhr.responseText);\r\n                gridApi.setGridOption('rowData', responseData);\r\n            }\r\n        };\r\n        xhr.send();\r\n\r\n        redirectToSharpenerDetailPage = (sharpener_id) => {\r\n            window.location.href = \"detail/\" + sharpener_id; \r\n        }\r\n    }\r\n    // knife detail\r\n    if (location[0] === '/knives/detail/') {\r\n        const rawId = parseInt(location[1]);\r\n        const knife_id = !isNaN(rawId) ? rawId : -1;\r\n\r\n        // blade grid\r\n        const gridDiv = document.querySelector('#blade_grid');\r\n\r\n        const gridOptions = {\r\n            headerHeight: 35,\r\n            defaultColDef: {\r\n                cellStyle: {textAlign: 'left'}\r\n              },\r\n            columnDefs: [\r\n                { \r\n                    headerName: '', \r\n                    width: 70, \r\n                    cellStyle: {textAlign: 'center'}, \r\n                    cellRenderer: (params) => {\r\n                        return `<button onclick=\"redirectToBladeEditPage(${params.data.blade_id})\" class=\"btn btn-sm btn-light\"><i class=\"fa-solid fa-edit\"></i></button>`;\r\n                    }, \r\n                },\r\n                { headerName: 'Shape', field: 'blade_shape', width: 150},\r\n                { headerName: 'Length', field: 'length', width: 100 },\r\n                { headerName: 'Edge Length', field: 'length_cutting_edge', width: 120 },\r\n                { headerName: 'Half-Stop', field: 'has_half_stop', width: 100},\r\n                { headerName: 'Main', field: 'is_main_blade', width: 100},\r\n            ]\r\n        };\r\n\r\n        const gridApi = agGrid.createGrid(gridDiv, gridOptions);\r\n\r\n        let xhr = new XMLHttpRequest();\r\n        xhr.open('GET', `${baseUrl}get_blade_grid/${knife_id}`, true);\r\n        xhr.onreadystatechange = () => {\r\n            if (xhr.readyState === 4 && xhr.status === 200) {\r\n                var responseData = JSON.parse(xhr.responseText);\r\n                gridApi.setGridOption('rowData', responseData);\r\n            }\r\n        };\r\n        xhr.send();\r\n\r\n        // work log grid\r\n        const gridDiv_wl = document.querySelector('#wl_grid');\r\n\r\n        const gridOptions_wl = {\r\n            headerHeight: 35,\r\n            defaultColDef: {\r\n                cellStyle: {textAlign: 'left'}\r\n              },\r\n            columnDefs: [\r\n                { \r\n                    headerName: '', \r\n                    width: 70, \r\n                    cellStyle: {textAlign: 'center'}, \r\n                    cellRenderer: (params) => {\r\n                        return `<button onclick=\"redirectToWorkLogEditPage(${params.data.work_log_id})\" class=\"btn btn-sm btn-light\"><i class=\"fa-solid fa-edit\"></i></button>`;\r\n                    }, \r\n                },\r\n                { headerName: 'Date', field: 'date', width: 120, cellDataType: 'date' },\r\n                { headerName: 'Description', field: 'description', flex: 1, wrapText: true, autoHeight: true }\r\n            ]\r\n        };\r\n\r\n        const gridApi_wl = agGrid.createGrid(gridDiv_wl, gridOptions_wl);\r\n\r\n        let xhr_wl = new XMLHttpRequest();\r\n        xhr_wl.open('GET', `${baseUrl}get_work_log_grid/${knife_id}`, true);\r\n        xhr_wl.onreadystatechange = () => {\r\n            if (xhr_wl.readyState === 4 && xhr_wl.status === 200) {\r\n                var responseData = JSON.parse(xhr_wl.responseText);\r\n\r\n                responseData.forEach(d => {\r\n                    d.date = d.date ? new Date(d.date) : null;\r\n                });\r\n\r\n                gridApi_wl.setGridOption('rowData', responseData);\r\n            }\r\n        };\r\n        xhr_wl.send();\r\n\r\n        redirectToBladeEditPage = (blade_id) => {\r\n            // window.location.href = \"detail/\" + sharpener_id; \r\n            console.log(blade_id)\r\n        }\r\n\r\n        redirectToWorkLogEditPage = (work_log_id) => {\r\n            // window.location.href = \"detail/\" + sharpener_id; \r\n            console.log(work_log_id)\r\n        }\r\n\r\n    }\r\n    // sharpener detail\r\n    if (location[0] === '/sharpeners/detail/') {\r\n        const rawId = parseInt(location[1]);\r\n        const sharpener_id = !isNaN(rawId) ? rawId : -1;\r\n\r\n        debugger;\r\n    }\r\n});\r\n\r\nremoveIdFromUrl = (url) => {\r\n    const regex = /(\\d+)\\/$/;\r\n\r\n    const match = url.match(regex);\r\n\r\n    if (match) {\r\n        const extractedNumber = match[1];\r\n        const modifiedString = url.replace(regex, '');\r\n\r\n        return [modifiedString, extractedNumber];\r\n    } else {\r\n        return [url, null];\r\n    }\r\n}\r\n\n\n//# sourceURL=webpack://stabby/./assets/scripts/load-grids.js?");

/***/ }),

/***/ "./assets/styles/styles.css":
/*!**********************************!*\
  !*** ./assets/styles/styles.css ***!
  \**********************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

"use strict";
eval("__webpack_require__.r(__webpack_exports__);\n// extracted by mini-css-extract-plugin\n\n\n//# sourceURL=webpack://stabby/./assets/styles/styles.css?");

/***/ })

/******/ 	});
/************************************************************************/
/******/ 	// The module cache
/******/ 	var __webpack_module_cache__ = {};
/******/ 	
/******/ 	// The require function
/******/ 	function __webpack_require__(moduleId) {
/******/ 		// Check if module is in cache
/******/ 		var cachedModule = __webpack_module_cache__[moduleId];
/******/ 		if (cachedModule !== undefined) {
/******/ 			return cachedModule.exports;
/******/ 		}
/******/ 		// Create a new module (and put it into the cache)
/******/ 		var module = __webpack_module_cache__[moduleId] = {
/******/ 			// no module.id needed
/******/ 			// no module.loaded needed
/******/ 			exports: {}
/******/ 		};
/******/ 	
/******/ 		// Execute the module function
/******/ 		__webpack_modules__[moduleId](module, module.exports, __webpack_require__);
/******/ 	
/******/ 		// Return the exports of the module
/******/ 		return module.exports;
/******/ 	}
/******/ 	
/************************************************************************/
/******/ 	/* webpack/runtime/compat get default export */
/******/ 	(() => {
/******/ 		// getDefaultExport function for compatibility with non-harmony modules
/******/ 		__webpack_require__.n = (module) => {
/******/ 			var getter = module && module.__esModule ?
/******/ 				() => (module['default']) :
/******/ 				() => (module);
/******/ 			__webpack_require__.d(getter, { a: getter });
/******/ 			return getter;
/******/ 		};
/******/ 	})();
/******/ 	
/******/ 	/* webpack/runtime/define property getters */
/******/ 	(() => {
/******/ 		// define getter functions for harmony exports
/******/ 		__webpack_require__.d = (exports, definition) => {
/******/ 			for(var key in definition) {
/******/ 				if(__webpack_require__.o(definition, key) && !__webpack_require__.o(exports, key)) {
/******/ 					Object.defineProperty(exports, key, { enumerable: true, get: definition[key] });
/******/ 				}
/******/ 			}
/******/ 		};
/******/ 	})();
/******/ 	
/******/ 	/* webpack/runtime/hasOwnProperty shorthand */
/******/ 	(() => {
/******/ 		__webpack_require__.o = (obj, prop) => (Object.prototype.hasOwnProperty.call(obj, prop))
/******/ 	})();
/******/ 	
/******/ 	/* webpack/runtime/make namespace object */
/******/ 	(() => {
/******/ 		// define __esModule on exports
/******/ 		__webpack_require__.r = (exports) => {
/******/ 			if(typeof Symbol !== 'undefined' && Symbol.toStringTag) {
/******/ 				Object.defineProperty(exports, Symbol.toStringTag, { value: 'Module' });
/******/ 			}
/******/ 			Object.defineProperty(exports, '__esModule', { value: true });
/******/ 		};
/******/ 	})();
/******/ 	
/************************************************************************/
/******/ 	
/******/ 	// startup
/******/ 	// Load entry module and return exports
/******/ 	// This entry module can't be inlined because the eval devtool is used.
/******/ 	var __webpack_exports__ = __webpack_require__("./assets/scripts/index.js");
/******/ 	
/******/ })()
;