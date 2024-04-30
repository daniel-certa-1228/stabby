document.addEventListener('DOMContentLoaded', function() {
    const baseUrl = "http://127.0.0.1:8000/";
    const location = removeIdFromUrl(window.location.pathname);
    // knife grid
    if (location[0] === '/') {
        const gridDiv = document.querySelector('#grid');

        const gridOptions = {
            pagination: true,
            defaultColDef: {
                filter: true,
                cellStyle: {textAlign: 'left'}
              },
            columnDefs: [
                { 
                    headerName: '', 
                    width: 70, 
                    pinned: 'left', 
                    cellStyle: {textAlign: 'center'}, 
                    cellRenderer: (params) => {
                        return `<button onclick="redirectToKnifeDetailPage(${params.data.knife_id})" class="btn btn-sm btn-light"><i class="fa-solid fa-magnifying-glass"></i></button>`;
                    }, 
                },
                { headerName: 'Brand', field: 'brand', width: 220, pinned: 'left' },
                { headerName: 'Knife', field: 'knife', width: 350, pinned: 'left' }, 
                { headerName: '# of Blades', field: 'num_of_blades', width: 120, cellStyle: {textAlign: 'right'} },
                { headerName: 'Blade Material', field: 'blade_material', width: 250 },
                { headerName: 'Handle Material', field: 'handle_material', width: 140 },
                { headerName: 'Lock', field: 'lock_type', width: 120 },
                { headerName: 'Deployment', field: 'deployment_type', width: 140 },
                { headerName: 'Country', field: 'country', width: 140 },
                { headerName: 'Vendor', field: 'vendor', width: 220 },
                { headerName: 'Needs Work', field: 'needs_work', width: 140, cellStyle: {textAlign: 'center'} },
            ]
        };

        const gridApi = agGrid.createGrid(gridDiv, gridOptions);

        let xhr = new XMLHttpRequest();
        xhr.open('GET', `${baseUrl}api/get_knife_grid`, true);
        xhr.onreadystatechange = () => {
            if (xhr.readyState === 4 && xhr.status === 200) {
                var responseData = JSON.parse(xhr.responseText);
                gridApi.setGridOption('rowData', responseData);
            }
        };
        xhr.send();

        redirectToKnifeDetailPage = (knife_id) => {
            window.location.href = "knives/detail/" + knife_id; 
        }
    }
    // sharpener grid
    if (location[0] === '/sharpeners/') {
        const gridDiv = document.querySelector('#grid');

        const gridOptions = {
            defaultColDef: {
                filter: true,
                cellStyle: {textAlign: 'left'}
              },
            columnDefs: [
                { 
                    headerName: '', 
                    width: 70, 
                    pinned: 'left', 
                    cellStyle: {textAlign: 'center'}, 
                    cellRenderer: (params) => {
                        return `<button onclick="redirectToSharpenerDetailPage(${params.data.sharpener_id})" class="btn btn-sm btn-light"><i class="fa-solid fa-magnifying-glass"></i></button>`;
                    }, 
                },
                { headerName: 'Brand', field: 'brand', width: 220, pinned: 'left' },
                { headerName: 'Sharpener', field: 'sharpener', width: 350, pinned: 'left' }, 
                { headerName: 'Cutting Agent', field: 'cutting_agent', width: 160 },
                { headerName: 'Bonding Agent', field: 'bonding_agent', width: 190 },
                { headerName: 'Length', field: 'length', width: 120 },
                { headerName: 'Width', field: 'width', width: 120 },
                { headerName: 'Country', field: 'country', width: 140 },
                { headerName: 'Friable', field: 'is_friable', width: 140, cellStyle: {textAlign: 'center'} },
            ]
        };

        const gridApi = agGrid.createGrid(gridDiv, gridOptions);

        let xhr = new XMLHttpRequest();
        xhr.open('GET', `${baseUrl}api/get_sharpener_grid`, true);
        xhr.onreadystatechange = () => {
            if (xhr.readyState === 4 && xhr.status === 200) {
                var responseData = JSON.parse(xhr.responseText);
                gridApi.setGridOption('rowData', responseData);
            }
        };
        xhr.send();

        redirectToSharpenerDetailPage = (sharpener_id) => {
            window.location.href = "detail/" + sharpener_id; 
        }
    }
    // knife detail
    if (location[0] === '/knives/detail/') {
        const rawId = parseInt(location[1]);
        const knife_id = !isNaN(rawId) ? rawId : -1;

        // blade grid
        const gridDiv = document.querySelector('#blade_grid');

        const gridOptions = {
            headerHeight: 35,
            defaultColDef: {
                cellStyle: {textAlign: 'left'}
              },
            columnDefs: [
                { 
                    headerName: '', 
                    width: 70, 
                    cellStyle: {textAlign: 'center'}, 
                    cellRenderer: (params) => {
                        return `<button onclick="redirectToBladeEditPage(${params.data.blade_id})" class="btn btn-sm btn-light"><i class="fa-solid fa-edit"></i></button>`;
                    }, 
                },
                { headerName: 'Shape', field: 'blade_shape', width: 150},
                { headerName: 'Length', field: 'length', width: 100 },
                { headerName: 'Edge Length', field: 'length_cutting_edge', width: 120 },
                { headerName: 'Half-Stop', field: 'has_half_stop', width: 100},
                { headerName: 'Main', field: 'is_main_blade', width: 100},
            ]
        };

        const gridApi = agGrid.createGrid(gridDiv, gridOptions);

        let xhr = new XMLHttpRequest();
        xhr.open('GET', `${baseUrl}api/get_blade_grid/${knife_id}`, true);
        xhr.onreadystatechange = () => {
            if (xhr.readyState === 4 && xhr.status === 200) {
                var responseData = JSON.parse(xhr.responseText);
                gridApi.setGridOption('rowData', responseData);
            }
        };
        xhr.send();

        // work log grid
        const gridDiv_wl = document.querySelector('#wl_grid');

        const gridOptions_wl = returnWorkLogGridOptions(
            true, 
            true,
            knife_id);

        const gridApi_wl = agGrid.createGrid(gridDiv_wl, gridOptions_wl);

        let xhr_wl = new XMLHttpRequest();
        xhr_wl.open('GET', `${baseUrl}api/get_knife_work_log_grid/${knife_id}`, true);
        xhr_wl.onreadystatechange = () => {
            if (xhr_wl.readyState === 4 && xhr_wl.status === 200) {
                var responseData = JSON.parse(xhr_wl.responseText);

                responseData.forEach(d => {
                    d.date = d.date ? new Date(d.date) : null;
                });

                gridApi_wl.setGridOption('rowData', responseData);
            }
        };
        xhr_wl.send();

        redirectToBladeEditPage = (blade_id) => {
            window.location.href = `${baseUrl}/knives/detail/${knife_id}/blades/edit/${blade_id}`; 
        
        }
    }
    // sharpener detail
    if (location[0] === '/sharpeners/detail/') {
        const rawId = parseInt(location[1]);
        const sharpener_id = !isNaN(rawId) ? rawId : -1;

        // work log grid
        const gridDiv_wl = document.querySelector('#wl_grid');

        const gridOptions_wl = returnWorkLogGridOptions(
            true, 
            false, 
            sharpener_id);

        const gridApi_wl = agGrid.createGrid(gridDiv_wl, gridOptions_wl);

        let xhr_wl = new XMLHttpRequest();
        xhr_wl.open('GET', `${baseUrl}api/get_sharpener_work_log_grid/${sharpener_id}`, true);
        xhr_wl.onreadystatechange = () => {
            if (xhr_wl.readyState === 4 && xhr_wl.status === 200) {
                var responseData = JSON.parse(xhr_wl.responseText);
  
                responseData.forEach(d => {
                    d.date = d.date ? new Date(d.date) : null;
                });

                gridApi_wl.setGridOption('rowData', responseData);
            }
        };
        xhr_wl.send();
    }
    //work log add/edit
    if (location[0].includes('work-logs/')) {
        const extracted_related_entity_id = removeEmbeddedIdFromUrl(location[0]);

        if (extracted_related_entity_id) {
            const rawId = parseInt(extracted_related_entity_id);
            const related_entity_id = !isNaN(rawId) ? rawId : -1;

            let url;

            if (location[0].includes('knives')) {
                url = `${baseUrl}api/get_knife_work_log_grid/${related_entity_id}`;
            } else {
                url = `${baseUrl}api/get_sharpener_work_log_grid/${related_entity_id}`;
            }
            // work log grid
            const gridDiv_wl = document.querySelector('#wl_grid');

            const gridOptions_wl = returnWorkLogGridOptions(false, null, null, location[1]);

            const gridApi_wl = agGrid.createGrid(gridDiv_wl, gridOptions_wl);

            let xhr_wl = new XMLHttpRequest();
            xhr_wl.open('GET', url, true);
            xhr_wl.onreadystatechange = () => {
                if (xhr_wl.readyState === 4 && xhr_wl.status === 200) {
                    var responseData = JSON.parse(xhr_wl.responseText);
    
                    responseData.forEach(d => {
                        d.date = d.date ? new Date(d.date) : null;
                    });

                    gridApi_wl.setGridOption('rowData', responseData);
                }
            };
            xhr_wl.send();
        } 
    }   
});

redirectToWorkLogEditPage = (work_log_id, entity_id, is_knife_wl) => {
    if (is_knife_wl) {
        window.location.href = `/knives/detail/${entity_id}/work-logs/edit/${work_log_id}`; 
    } else {
        window.location.href = `/sharpeners/detail/${entity_id}/work-logs/edit/${work_log_id}`; 
    }
}

removeIdFromUrl = (url) => {
    const regex = /(\d+)\/$/;

    const match = url.match(regex);

    if (match) {
        const extractedNumber = match[1];
        const modifiedString = url.replace(regex, '');

        return [modifiedString, extractedNumber];
    } else {
        return [url, null];
    }
}

removeEmbeddedIdFromUrl = (url) => {
    const regex = /\/(\d+)\//;

    const match = url.match(regex)

    if (match) {
        return match[0].replaceAll('/', '');
    } else {
        return null;
    }
}

returnWorkLogGridOptions = (with_buttons, is_knife_wl = null, entity_id = null, work_log_id = null) => {
    if (with_buttons) {
        return {
            headerHeight: 35,
            defaultColDef: {
                cellStyle: {textAlign: 'left'}
              },
            columnDefs: [
                { 
                    headerName: '', 
                    width: 70, 
                    cellStyle: {textAlign: 'center'}, 
                    cellRenderer: (params) => {
                        return `<button onclick="redirectToWorkLogEditPage(${params.data.work_log_id}, ${entity_id}, ${is_knife_wl})" class="btn btn-sm btn-light"><i class="fa-solid fa-edit"></i></button>`;
                    }, 
                },
                { headerName: 'Date', field: 'date', width: 120, cellDataType: 'date' },
                { headerName: 'Description', field: 'description', flex: 1, wrapText: true, autoHeight: true }
            ]
        };
    } else {
        return {
            headerHeight: 35,
            defaultColDef: {
                cellStyle: {textAlign: 'left'}
              },
              getRowClass: params => {
                if (params.data.work_log_id == work_log_id) {
                    return 'bg-primary-subtle';
                }
            },
            columnDefs: [
                { headerName: 'Date', field: 'date', width: 120, cellDataType: 'date' },
                { headerName: 'Description', field: 'description', flex: 1, wrapText: true, autoHeight: true }
            ]
        };
    }
  
}
