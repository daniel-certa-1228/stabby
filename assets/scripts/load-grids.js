document.addEventListener('DOMContentLoaded', function() {
    const baseUrl = "http://127.0.0.1:8000/api/";
    const location = removeIdFromUrl(window.location.pathname);
    // debugger;
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
        xhr.open('GET', `${baseUrl}get_knife_grid`, true);
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
        xhr.open('GET', `${baseUrl}get_sharpener_grid`, true);
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

        debugger;
    }
    // sharpener detail
    if (location[0] === '/sharpeners/detail/') {
        const rawId = parseInt(location[1]);
        const sharpener_id = !isNaN(rawId) ? rawId : -1;

        debugger;
    }
});

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
