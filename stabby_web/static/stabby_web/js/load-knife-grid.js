document.addEventListener('DOMContentLoaded', function() {
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
        xhr.open('GET', 'http://127.0.0.1:8000/api/get_knife_grid/', true);
        xhr.onreadystatechange = function() {
            if (xhr.readyState === 4 && xhr.status === 200) {
                var responseData = JSON.parse(xhr.responseText);
                gridOptions.api.setRowData(responseData);
            }
        };
        xhr.send();
    }
});