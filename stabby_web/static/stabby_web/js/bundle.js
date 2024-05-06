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
eval("__webpack_require__.r(__webpack_exports__);\n/* harmony import */ var _load_grids__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! ./load-grids */ \"./assets/scripts/load-grids.js\");\n/* harmony import */ var _load_grids__WEBPACK_IMPORTED_MODULE_0___default = /*#__PURE__*/__webpack_require__.n(_load_grids__WEBPACK_IMPORTED_MODULE_0__);\n/* harmony import */ var _styles_styles_css__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! ../styles/styles.css */ \"./assets/styles/styles.css\");\n\n\n\n//# sourceURL=webpack://stabby/./assets/scripts/index.js?");

/***/ }),

/***/ "./assets/scripts/load-grids.js":
/*!**************************************!*\
  !*** ./assets/scripts/load-grids.js ***!
  \**************************************/
/***/ (() => {

eval("/* eslint-disable no-undef */\ndocument.addEventListener('DOMContentLoaded', function () {\n  var baseUrl = \"http://127.0.0.1:8000/\";\n  deleteBlade = function deleteBlade(blade_id, knife_id) {\n    if (window.confirm(\"Are you sure you want to delete this Blade?\")) {\n      var url = \"\".concat(baseUrl, \"api/delete_blade/\").concat(blade_id, \"/\");\n      var xhr_wl = new XMLHttpRequest();\n      xhr_wl.open('GET', url, true);\n      xhr_wl.onreadystatechange = function () {\n        if (xhr_wl.readyState === 4 && xhr_wl.status === 200) {\n          var responseData = JSON.parse(xhr_wl.responseText);\n          if (responseData) {\n            window.location.href = \"\".concat(baseUrl, \"/knives/detail/\").concat(knife_id);\n          }\n        }\n      };\n      xhr_wl.send();\n    }\n  };\n  deleteKnife = function deleteKnife(knife_id) {\n    if (window.confirm(\"Are you sure you want to delete this Knife?\")) {\n      var url = \"\".concat(baseUrl, \"api/delete_knife/\").concat(knife_id, \"/\");\n      var xhr_wl = new XMLHttpRequest();\n      xhr_wl.open('GET', url, true);\n      xhr_wl.onreadystatechange = function () {\n        if (xhr_wl.readyState === 4 && xhr_wl.status === 200) {\n          var responseData = JSON.parse(xhr_wl.responseText);\n          if (responseData) {\n            window.location.href = \"\".concat(baseUrl);\n          }\n        }\n      };\n      xhr_wl.send();\n    }\n  };\n  deleteSharpener = function deleteSharpener(sharpener_id) {\n    if (window.confirm(\"Are you sure you want to delete this Sharpener?\")) {\n      var url = \"\".concat(baseUrl, \"api/delete_sharpener/\").concat(sharpener_id, \"/\");\n      var xhr_wl = new XMLHttpRequest();\n      xhr_wl.open('GET', url, true);\n      xhr_wl.onreadystatechange = function () {\n        if (xhr_wl.readyState === 4 && xhr_wl.status === 200) {\n          var responseData = JSON.parse(xhr_wl.responseText);\n          if (responseData) {\n            window.location.href = \"\".concat(baseUrl, \"/sharpeners\");\n          }\n        }\n      };\n      xhr_wl.send();\n    }\n  };\n  deleteWorkLog = function deleteWorkLog(work_log_id, entity_id, is_knife_wl) {\n    if (window.confirm(\"Are you sure you want to delete this Work Log?\")) {\n      var url = \"\".concat(baseUrl, \"api/delete_work_log/\").concat(work_log_id, \"/\");\n      var xhr_wl = new XMLHttpRequest();\n      xhr_wl.open('GET', url, true);\n      xhr_wl.onreadystatechange = function () {\n        if (xhr_wl.readyState === 4 && xhr_wl.status === 200) {\n          var responseData = JSON.parse(xhr_wl.responseText);\n          if (responseData) {\n            if (is_knife_wl) {\n              window.location.href = \"\".concat(baseUrl, \"/knives/detail/\").concat(entity_id, \"#work_log_card\");\n            } else {\n              window.location.href = \"\".concat(baseUrl, \"/sharpeners/detail/\").concat(entity_id, \"#work_log_card\");\n            }\n          }\n        }\n      };\n      xhr_wl.send();\n    }\n  };\n  redirectToBladeEditPage = function redirectToBladeEditPage(blade_id, knife_id) {\n    window.location.href = \"\".concat(baseUrl, \"/knives/detail/\").concat(knife_id, \"/blades/edit/\").concat(blade_id);\n  };\n  redirectToKnifeDetailPage = function redirectToKnifeDetailPage(knife_id) {\n    window.location.href = \"knives/detail/\".concat(knife_id);\n  };\n  redirectToSharpenerDetailPage = function redirectToSharpenerDetailPage(sharpener_id) {\n    window.location.href = \"detail/\".concat(sharpener_id);\n  };\n  redirectToWorkLogEditPage = function redirectToWorkLogEditPage(work_log_id, entity_id, is_knife_wl) {\n    if (is_knife_wl) {\n      window.location.href = \"/knives/detail/\".concat(entity_id, \"/work-logs/edit/\").concat(work_log_id);\n    } else {\n      window.location.href = \"/sharpeners/detail/\".concat(entity_id, \"/work-logs/edit/\").concat(work_log_id);\n    }\n  };\n  removeEmbeddedIdFromUrl = function removeEmbeddedIdFromUrl(url) {\n    var regex = /\\/(\\d+)\\//;\n    var match = url.match(regex);\n    if (match) {\n      return match[0].replaceAll('/', '');\n    } else {\n      return null;\n    }\n  };\n  removeIdFromUrl = function removeIdFromUrl(url) {\n    var regex = /(\\d+)\\/$/;\n    var match = url.match(regex);\n    if (match) {\n      var extractedNumber = match[1];\n      var modifiedString = url.replace(regex, '');\n      return [modifiedString, extractedNumber];\n    } else {\n      return [url, null];\n    }\n  };\n  returnWorkLogGridOptions = function returnWorkLogGridOptions(with_buttons) {\n    var is_knife_wl = arguments.length > 1 && arguments[1] !== undefined ? arguments[1] : null;\n    var entity_id = arguments.length > 2 && arguments[2] !== undefined ? arguments[2] : null;\n    var work_log_id = arguments.length > 3 && arguments[3] !== undefined ? arguments[3] : null;\n    if (with_buttons) {\n      return {\n        headerHeight: 35,\n        defaultColDef: {\n          cellStyle: {\n            textAlign: 'left'\n          }\n        },\n        columnDefs: [{\n          headerName: '',\n          width: 70,\n          cellStyle: {\n            textAlign: 'center'\n          },\n          cellRenderer: function cellRenderer(params) {\n            return \"<button onclick=\\\"redirectToWorkLogEditPage(\".concat(params.data.work_log_id, \", \").concat(entity_id, \", \").concat(is_knife_wl, \")\\\" class=\\\"btn btn-sm btn-light\\\"><i class=\\\"fa-solid fa-edit\\\"></i></button>\");\n          }\n        }, {\n          headerName: 'Date',\n          field: 'date',\n          width: 120,\n          cellDataType: 'date'\n        }, {\n          headerName: 'Description',\n          field: 'description',\n          flex: 1,\n          wrapText: true,\n          autoHeight: true\n        }, {\n          headerName: '',\n          width: 70,\n          cellStyle: {\n            textAlign: 'center'\n          },\n          cellRenderer: function cellRenderer(params) {\n            return \"<button onclick=\\\"deleteWorkLog(\".concat(params.data.work_log_id, \", \").concat(entity_id, \", \").concat(is_knife_wl, \")\\\" class=\\\"btn btn-sm btn-light\\\"><i class=\\\"fa-solid fa-trash\\\"></i></button>\");\n          }\n        }]\n      };\n    } else {\n      return {\n        headerHeight: 35,\n        defaultColDef: {\n          cellStyle: {\n            textAlign: 'left'\n          }\n        },\n        getRowClass: function getRowClass(params) {\n          if (params.data.work_log_id == work_log_id) {\n            return 'bg-primary-subtle';\n          }\n        },\n        columnDefs: [{\n          headerName: 'Date',\n          field: 'date',\n          width: 120,\n          cellDataType: 'date'\n        }, {\n          headerName: 'Description',\n          field: 'description',\n          flex: 1,\n          wrapText: true,\n          autoHeight: true\n        }]\n      };\n    }\n  };\n  var location = removeIdFromUrl(window.location.pathname);\n\n  // knife grid\n  if (location[0] === '/') {\n    var gridDiv = document.querySelector('#grid');\n    var gridOptions = {\n      pagination: true,\n      defaultColDef: {\n        filter: true,\n        cellStyle: {\n          textAlign: 'left'\n        }\n      },\n      columnDefs: [{\n        headerName: '',\n        width: 70,\n        pinned: 'left',\n        cellStyle: {\n          textAlign: 'center'\n        },\n        cellRenderer: function cellRenderer(params) {\n          return \"<button onclick=\\\"redirectToKnifeDetailPage(\".concat(params.data.knife_id, \")\\\" class=\\\"btn btn-sm btn-light\\\"><i class=\\\"fa-solid fa-magnifying-glass\\\"></i></button>\");\n        }\n      }, {\n        headerName: 'Brand',\n        field: 'brand',\n        width: 220,\n        pinned: 'left'\n      }, {\n        headerName: 'Knife',\n        field: 'knife',\n        width: 350,\n        pinned: 'left'\n      }, {\n        headerName: '# of Blades',\n        field: 'num_of_blades',\n        width: 120,\n        cellStyle: {\n          textAlign: 'right'\n        }\n      }, {\n        headerName: 'Blade Material',\n        field: 'blade_material',\n        width: 250\n      }, {\n        headerName: 'Handle Material',\n        field: 'handle_material',\n        width: 140\n      }, {\n        headerName: 'Lock',\n        field: 'lock_type',\n        width: 120\n      }, {\n        headerName: 'Deployment',\n        field: 'deployment_type',\n        width: 140\n      }, {\n        headerName: 'Country',\n        field: 'country',\n        width: 140\n      }, {\n        headerName: 'Vendor',\n        field: 'vendor',\n        width: 220\n      }, {\n        headerName: 'Needs Work',\n        field: 'needs_work',\n        width: 140,\n        cellStyle: {\n          textAlign: 'center'\n        }\n      }]\n    };\n    var gridApi = agGrid.createGrid(gridDiv, gridOptions);\n    var xhr = new XMLHttpRequest();\n    xhr.open('GET', \"\".concat(baseUrl, \"api/get_knife_grid\"), true);\n    xhr.onreadystatechange = function () {\n      if (xhr.readyState === 4 && xhr.status === 200) {\n        var responseData = JSON.parse(xhr.responseText);\n        gridApi.setGridOption('rowData', responseData);\n      }\n    };\n    xhr.send();\n  }\n  // sharpener grid\n  if (location[0] === '/sharpeners/') {\n    var _gridDiv = document.querySelector('#grid');\n    var _gridOptions = {\n      defaultColDef: {\n        filter: true,\n        cellStyle: {\n          textAlign: 'left'\n        }\n      },\n      columnDefs: [{\n        headerName: '',\n        width: 70,\n        pinned: 'left',\n        cellStyle: {\n          textAlign: 'center'\n        },\n        cellRenderer: function cellRenderer(params) {\n          return \"<button onclick=\\\"redirectToSharpenerDetailPage(\".concat(params.data.sharpener_id, \")\\\" class=\\\"btn btn-sm btn-light\\\"><i class=\\\"fa-solid fa-magnifying-glass\\\"></i></button>\");\n        }\n      }, {\n        headerName: 'Brand',\n        field: 'brand',\n        width: 220,\n        pinned: 'left'\n      }, {\n        headerName: 'Sharpener',\n        field: 'sharpener',\n        width: 350,\n        pinned: 'left'\n      }, {\n        headerName: 'Cutting Agent',\n        field: 'cutting_agent',\n        width: 160\n      }, {\n        headerName: 'Bonding Agent',\n        field: 'bonding_agent',\n        width: 190\n      }, {\n        headerName: 'Length',\n        field: 'length',\n        width: 120\n      }, {\n        headerName: 'Width',\n        field: 'width',\n        width: 120\n      }, {\n        headerName: 'Country',\n        field: 'country',\n        width: 140\n      }, {\n        headerName: 'Friable',\n        field: 'is_friable',\n        width: 140,\n        cellStyle: {\n          textAlign: 'center'\n        }\n      }]\n    };\n    var _gridApi = agGrid.createGrid(_gridDiv, _gridOptions);\n    var _xhr = new XMLHttpRequest();\n    _xhr.open('GET', \"\".concat(baseUrl, \"api/get_sharpener_grid\"), true);\n    _xhr.onreadystatechange = function () {\n      if (_xhr.readyState === 4 && _xhr.status === 200) {\n        var responseData = JSON.parse(_xhr.responseText);\n        _gridApi.setGridOption('rowData', responseData);\n      }\n    };\n    _xhr.send();\n  }\n  // knife detail\n  if (location[0] === '/knives/detail/') {\n    var rawId = parseInt(location[1]);\n    var knife_id = !isNaN(rawId) ? rawId : -1;\n\n    // blade grid\n    var _gridDiv2 = document.querySelector('#blade_grid');\n    var _gridOptions2 = {\n      headerHeight: 35,\n      defaultColDef: {\n        cellStyle: {\n          textAlign: 'left'\n        }\n      },\n      columnDefs: [{\n        headerName: '',\n        width: 70,\n        cellStyle: {\n          textAlign: 'center'\n        },\n        cellRenderer: function cellRenderer(params) {\n          return \"<button onclick=\\\"redirectToBladeEditPage(\".concat(params.data.blade_id, \", \").concat(knife_id, \")\\\" class=\\\"btn btn-sm btn-light\\\"><i class=\\\"fa-solid fa-edit\\\"></i></button>\");\n        }\n      }, {\n        headerName: 'Shape',\n        field: 'blade_shape',\n        width: 135\n      }, {\n        headerName: 'Length',\n        field: 'length',\n        width: 95\n      }, {\n        headerName: 'C.E. Length',\n        field: 'length_cutting_edge',\n        width: 105\n      }, {\n        headerName: 'Half-Stop',\n        field: 'has_half_stop',\n        width: 95\n      }, {\n        headerName: 'Main',\n        field: 'is_main_blade',\n        width: 70\n      }, {\n        headerName: '',\n        width: 70,\n        cellStyle: {\n          textAlign: 'center'\n        },\n        cellRenderer: function cellRenderer(params) {\n          return \"<button onclick=\\\"deleteBlade(\".concat(params.data.blade_id, \", \").concat(params.data.knife_id, \")\\\" class=\\\"btn btn-sm btn-light\\\"><i class=\\\"fa-solid fa-trash\\\"></i></button>\");\n        }\n      }]\n    };\n    var _gridApi2 = agGrid.createGrid(_gridDiv2, _gridOptions2);\n    var _xhr2 = new XMLHttpRequest();\n    _xhr2.open('GET', \"\".concat(baseUrl, \"api/get_blade_grid/\").concat(knife_id), true);\n    _xhr2.onreadystatechange = function () {\n      if (_xhr2.readyState === 4 && _xhr2.status === 200) {\n        var responseData = JSON.parse(_xhr2.responseText);\n        _gridApi2.setGridOption('rowData', responseData);\n      }\n    };\n    _xhr2.send();\n\n    // work log grid\n    var gridDiv_wl = document.querySelector('#wl_grid');\n    var gridOptions_wl = returnWorkLogGridOptions(true, true, knife_id);\n    var gridApi_wl = agGrid.createGrid(gridDiv_wl, gridOptions_wl);\n    var xhr_wl = new XMLHttpRequest();\n    xhr_wl.open('GET', \"\".concat(baseUrl, \"api/get_knife_work_log_grid/\").concat(knife_id), true);\n    xhr_wl.onreadystatechange = function () {\n      if (xhr_wl.readyState === 4 && xhr_wl.status === 200) {\n        var responseData = JSON.parse(xhr_wl.responseText);\n        responseData.forEach(function (d) {\n          d.date = d.date ? new Date(d.date) : null;\n        });\n        gridApi_wl.setGridOption('rowData', responseData);\n      }\n    };\n    xhr_wl.send();\n  }\n  // sharpener detail\n  if (location[0] === '/sharpeners/detail/') {\n    var _rawId = parseInt(location[1]);\n    var sharpener_id = !isNaN(_rawId) ? _rawId : -1;\n\n    // work log grid\n    var _gridDiv_wl = document.querySelector('#wl_grid');\n    var _gridOptions_wl = returnWorkLogGridOptions(true, false, sharpener_id);\n    var _gridApi_wl = agGrid.createGrid(_gridDiv_wl, _gridOptions_wl);\n    var _xhr_wl = new XMLHttpRequest();\n    _xhr_wl.open('GET', \"\".concat(baseUrl, \"api/get_sharpener_work_log_grid/\").concat(sharpener_id), true);\n    _xhr_wl.onreadystatechange = function () {\n      if (_xhr_wl.readyState === 4 && _xhr_wl.status === 200) {\n        var responseData = JSON.parse(_xhr_wl.responseText);\n        responseData.forEach(function (d) {\n          d.date = d.date ? new Date(d.date) : null;\n        });\n        _gridApi_wl.setGridOption('rowData', responseData);\n      }\n    };\n    _xhr_wl.send();\n  }\n  //work log add/edit\n  if (location[0].includes('work-logs/')) {\n    var extracted_related_entity_id = removeEmbeddedIdFromUrl(location[0]);\n    if (extracted_related_entity_id) {\n      var _rawId2 = parseInt(extracted_related_entity_id);\n      var related_entity_id = !isNaN(_rawId2) ? _rawId2 : -1;\n      var url;\n      if (location[0].includes('knives')) {\n        url = \"\".concat(baseUrl, \"api/get_knife_work_log_grid/\").concat(related_entity_id);\n      } else {\n        url = \"\".concat(baseUrl, \"api/get_sharpener_work_log_grid/\").concat(related_entity_id);\n      }\n      // work log grid\n      var _gridDiv_wl2 = document.querySelector('#wl_grid');\n      var _gridOptions_wl2 = returnWorkLogGridOptions(false, null, null, location[1]);\n      var _gridApi_wl2 = agGrid.createGrid(_gridDiv_wl2, _gridOptions_wl2);\n      var _xhr_wl2 = new XMLHttpRequest();\n      _xhr_wl2.open('GET', url, true);\n      _xhr_wl2.onreadystatechange = function () {\n        if (_xhr_wl2.readyState === 4 && _xhr_wl2.status === 200) {\n          var responseData = JSON.parse(_xhr_wl2.responseText);\n          responseData.forEach(function (d) {\n            d.date = d.date ? new Date(d.date) : null;\n          });\n          _gridApi_wl2.setGridOption('rowData', responseData);\n        }\n      };\n      _xhr_wl2.send();\n    }\n  }\n});\n\n//# sourceURL=webpack://stabby/./assets/scripts/load-grids.js?");

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