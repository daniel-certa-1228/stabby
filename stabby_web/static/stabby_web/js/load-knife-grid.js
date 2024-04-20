document.addEventListener('DOMContentLoaded', function() {
    const baseUrl = "http://127.0.0.1:8000/api/";
    // knife grid
    if (window.location.pathname === '/') {
        const gridDiv = document.querySelector('#grid');

        const gridOptions = {
            pagination: true,
            defaultColDef: {
                filter: true,
                cellStyle: {textAlign: 'left'}
              },
            columnDefs: [
                { headerName: 'Id', field: 'knife_id', width: 70, pinned: 'left', cellStyle: {textAlign: 'center'} },
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

        new agGrid.Grid(gridDiv, gridOptions);

        let xhr = new XMLHttpRequest();
        xhr.open('GET', `${baseUrl}get_knife_grid`, true);
        xhr.onreadystatechange = function() {
            if (xhr.readyState === 4 && xhr.status === 200) {
                var responseData = JSON.parse(xhr.responseText);
                gridOptions.api.setRowData(responseData);
            }
        };
        xhr.send();
    }
    // sharpener grid
    if (window.location.pathname === '/sharpeners/') {
        const gridDiv = document.querySelector('#grid');

        const gridOptions = {
            defaultColDef: {
                filter: true,
                cellStyle: {textAlign: 'left'}
              },
            columnDefs: [
                { headerName: 'Id', field: 'sharpener_id', width: 70, pinned: 'left', cellStyle: {textAlign: 'center'} },
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

        new agGrid.Grid(gridDiv, gridOptions);

        let xhr = new XMLHttpRequest();
        xhr.open('GET', `${baseUrl}get_sharpener_grid`, true);
        xhr.onreadystatechange = function() {
            debugger;
            if (xhr.readyState === 4 && xhr.status === 200) {
                var responseData = JSON.parse(xhr.responseText);
                gridOptions.api.setRowData(responseData);
            }
        };
        xhr.send();
    }
});