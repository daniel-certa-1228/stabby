'use strict';

import { 
  agGrid, 
  ajax_handler,
  constants,
  popover_handler,
  view_blade_grid_model, 
  view_knife_grid_model, 
  view_sharpener_grid_model, 
  work_log_model} from './index';
import { knife_filter_model } from './models/knife-filter-model';

const loadKnifeGrid = async (knife_filter: knife_filter_model | null): Promise<void> => {
  const gridDiv: HTMLElement = document.querySelector('#grid')!;

  const gridOptions: agGrid.GridOptions = {
    pagination: true,
    paginationPageSize: 50,
    suppressMenuHide: true,
    defaultColDef: {
      filter: true,
      cellStyle: { textAlign: 'left' }
    },
    columnDefs: [
      {
        headerName: '',
        width: 70,
        pinned: 'left',
        cellStyle: { textAlign: 'center' },
        cellRenderer: (params: any) => {
          return `<button class="btn btn-sm btn-light knife-detail-btn" value="${params.data.knife_id}"><i class="bi bi-search"></i></button>`;
        }, 
        filter: false
      },
      { 
        headerName: 'Brand', 
        field: 'brand', 
        width: 220, 
        pinned: 'left',
        filterParams: {
          buttons: ['reset'],
        } 
      },
      { 
        headerName: 'Knife', 
        field: 'knife', 
        width: 350, 
        pinned: 'left', 
        filterParams: {
          buttons: ['reset'],
        } 
      },
      { 
        headerName: '# of Blades', 
        field: 'num_of_blades', 
        width: 130, 
        cellStyle: { 
          textAlign: 'right' 
        }, 
        filterParams: {
          buttons: ['reset'],
        } 
      },
      { 
        headerName: 'Blade Material', 
        field: 'blade_material', 
        width: 280, 
        filterParams: {
          buttons: ['reset'],
        } 
      },
      { 
        headerName: 'Handle Material', 
        field: 'handle_material', 
        width: 160, 
        filterParams: {
          buttons: ['reset'],
        } 
      },
      { 
        headerName: 'Lock', 
        field: 'lock_type', 
        width: 120, 
        filterParams: {
          buttons: ['reset'],
        } 
      },
      { 
        headerName: 'Deployment', 
        field: 'deployment_type', 
        width: 140, 
        filterParams: {
          buttons: ['reset'],
        } 
      },
      { 
        headerName: 'Country', 
        field: 'country', 
        width: 140, 
        filterParams: {
          buttons: ['reset'],
        } 
      },
      { 
        headerName: 'Vendor', 
        field: 'vendor', 
        width: 220, 
        filterParams: {
          buttons: ['reset'],
        } 
      },
      { 
        headerName: 'Purchased New', 
        field: 'purchased_new', 
        width: 160, 
        cellStyle: { 
          textAlign: 'center' 
        }, 
        filterParams: {
          buttons: ['reset'],
        } 
      },
      { 
        headerName: 'Needs Work', 
        field: 'needs_work', 
        width: 140, 
        cellStyle: { 
          textAlign: 'center' 
        }, 
        filterParams: {
          buttons: ['reset'],
        } 
      },
      { 
        headerName: 'Date Entered', 
        field: 'create_date', 
        width: 150, 
        cellDataType: 'date', 
        filterParams: {
          buttons: ['reset'],
        } 
      },
    ]
  };

  const gridApi: agGrid.GridApi<any> = agGrid.createGrid(gridDiv, gridOptions);

  setKnifeFilter(gridApi, knife_filter);

  const url: string = `${constants.getBaseUrl()}api/get_knife_grid`;

  const rowData: view_knife_grid_model[] | undefined = await ajax_handler.getKnifeGrid(url);

  if (rowData){
    rowData.forEach((d: view_knife_grid_model) => {
      const date = d.create_date ? new Date(d.create_date) : null;

      if (date) {
        d.create_date = new Date(date.getFullYear(), date.getMonth(), date.getDate());
      }
    });
  }

  gridApi.setGridOption('rowData', rowData);
};

const loadSharpenerGrid = async (): Promise<void> => {
  const gridDiv: HTMLElement = document.querySelector('#grid')!;

  const gridOptions: agGrid.GridOptions = {
    defaultColDef: {
      filter: true,
      cellStyle: { textAlign: 'left' }
    },
    suppressMenuHide: true,
    domLayout: "autoHeight",
    columnDefs: [
      {
        headerName: '',
        width: 70,
        pinned: 'left',
        cellStyle: { textAlign: 'center' },
        cellRenderer: (params: any) => {
          return `<button class="btn btn-sm btn-light sharpener-detail-btn" value=${params.data.sharpener_id}><i class="bi bi-search"></i></button>`;
        }, 
        filter: false
      },
      { 
        headerName: 'Brand', 
        field: 'brand', 
        width: 220, 
        pinned: 'left', 
        filterParams: {
          buttons: ['reset'],
        } 
      },
      { 
        headerName: 'Sharpener', 
        field: 'sharpener', 
        width: 400, 
        pinned: 'left', 
        filterParams: {
          buttons: ['reset'],
        } 
      },
      { 
        headerName: 'Cutting Agent', 
        field: 'cutting_agent', 
        minWidth: 160, 
        filterParams: {
          buttons: ['reset'],
        } 
      },
      { 
        headerName: 'Bonding Agent', 
        field: 'bonding_agent', 
        minWidth: 190, 
        filterParams: {
          buttons: ['reset'],
        } 
      },
      { 
        headerName: 'Length', 
        field: 'length', 
        width: 120, 
        filterParams: {
          buttons: ['reset'],
        } 
      },
      { 
        headerName: 'Width', 
        field: 'width', 
        width: 120, 
        filterParams: {
          buttons: ['reset'],
        } 
      },
      { 
        headerName: 'Country', 
        field: 'country', 
        width: 140, 
        filterParams: {
          buttons: ['reset'],
        } 
      },
      { 
        headerName: 'Friable', 
        field: 'is_friable', 
        width: 140, 
        cellStyle: { 
          textAlign: 'center' 
        }, 
        filterParams: {
          buttons: ['reset'],
        } 
      },
    ]
  };

  const gridApi: agGrid.GridApi<any> = agGrid.createGrid(gridDiv, gridOptions);

  const url: string = `${constants.getBaseUrl()}api/get_sharpener_grid`;

  const rowData: view_sharpener_grid_model[] | undefined = await ajax_handler.getSharpenerGrid(url);

  gridApi.setGridOption('rowData', rowData);
};

const loadBladeGrid = async (knife_id: number): Promise<void> => {
  const gridDiv: HTMLElement = document.querySelector('#blade_grid')!;

  const gridOptions: agGrid.GridOptions = {
    headerHeight: 35,
    onFirstDataRendered(event) {
      popover_handler.initGridPopovers();
    },
    defaultColDef: {
      cellStyle: { textAlign: 'left' }
    },
    domLayout: "autoHeight",
    columnDefs: [
      {
        headerName: '',
        width: 70,
        cellStyle: { textAlign: 'center' },
        cellRenderer: (params: any) => {
          return `<button class="btn btn-sm btn-light blade-edit-btn" value="[${params.data.blade_id}, ${knife_id}]"><i class="bi bi-pencil-square"></i></button>`;
        },
      },
      { 
        headerName: 'Shape',
        cellRenderer: (params: any) => {
          return `${params.data.blade_shape}${params.data.blade_shape_notes ? `<span class="text-primary pointer">&nbsp;&nbsp;<i class="bi bi-info-circle grid-popover" data-bs-toggle="popover" data-bs-title="Blade Shape Notes" data-bs-content="${params.data.blade_shape_notes}" data-bs-trigger="hover focus"></i></span>` : ''}`;
        },
        minWidth: 135, 
        maxWidth: 185
      },
      { 
        headerName: 'Length', 
        field: 'length', 
        width: 95 
      },
      { 
        headerName: 'C.E. Length', 
        field: 'length_cutting_edge', 
        width: 105 
      },
      { 
        headerName: 'Half-Stop', 
        field: 'has_half_stop', 
        width: 95 
      },
      { 
        headerName: 'Main', 
        field: 'is_main_blade', 
        width: 70 
      },
      {
        headerName: '',
        width: 70,
        cellStyle: { textAlign: 'center' },
        cellRenderer: (params: any) => {
          return `<button class="btn btn-sm btn-light blade-delete-btn" value="[${params.data.blade_id}, ${params.data.knife_id}]"><i class="bi bi-trash"></i></button>`;
        },
      },
    ]
  };

  const gridApi: agGrid.GridApi<any> = agGrid.createGrid(gridDiv, gridOptions);

  const url: string = `${constants.getBaseUrl()}api/get_blade_grid/${knife_id}`;

  const rowData: view_blade_grid_model[] | undefined = await ajax_handler.getBladeGrid(url);

  gridApi.setGridOption('rowData', rowData);
};

const loadWorkLogGrid = async (with_buttons: boolean, is_knife_wl: boolean, entity_id: number, work_log_id: number | null = null): Promise<void> => {
  const gridDiv_wl: HTMLElement = document.querySelector('#wl_grid')!;

  if (gridDiv_wl) {
    const gridOptions: agGrid.GridOptions = returnWorkLogGridOptions(
      with_buttons,
      is_knife_wl,
      entity_id,
      work_log_id);
  
    const gridApi: agGrid.GridApi<any> = agGrid.createGrid(gridDiv_wl, gridOptions);
  
    let url: string;
  
    if (is_knife_wl) {
      url = `${constants.getBaseUrl()}api/get_knife_work_log_grid/${entity_id}`;
    } else {
      url = `${constants.getBaseUrl()}api/get_sharpener_work_log_grid/${entity_id}`;
    }
  
    const rowData: work_log_model[] | undefined = await ajax_handler.getWorkLogGrid(url);
  
    if (rowData){
      rowData.forEach((d: work_log_model) => {
        d.date = d.date ? new Date(d.date) : null;
      });
    }
  
    gridApi.setGridOption('rowData', rowData);
  }
};

// Private Functions
const returnWorkLogGridOptions = (with_buttons: boolean, is_knife_wl: boolean, entity_id: number, work_log_id: number | null): agGrid.GridOptions => {
  if (with_buttons) {
    return {
      headerHeight: 35,
      defaultColDef: {
        cellStyle: { textAlign: 'left' }
      },
      domLayout: "autoHeight",
      columnDefs: [
        {
          headerName: '',
          width: 70,
          cellStyle: { textAlign: 'center' },
          cellRenderer: (params: any) => {
            return `<button class="btn btn-sm btn-light wl-edit-btn" value="[${params.data.work_log_id}, ${entity_id}, ${is_knife_wl}]"><i class="bi bi-pencil-square"></i></button>`;
          },
        },
        { 
          headerName: 'Date', 
          field: 'date', 
          width: 120, 
          cellDataType: 'date' 
        },
        { 
          headerName: 'Description', 
          field: 'description', 
          flex: 1, 
          wrapText: true, 
          autoHeight: true 
        },
        {
          headerName: '',
          width: 70,
          cellStyle: { textAlign: 'center' },
          cellRenderer: (params: any) => {
            return `<button class="btn btn-sm btn-light wl-delete-btn" value="[${params.data.work_log_id}, ${entity_id}, ${is_knife_wl}]"><i class="bi bi-trash"></i></button>`;
          },
        },
      ]
    };
  } else {
    return {
      headerHeight: 35,
      domLayout: "autoHeight",
      defaultColDef: {
        cellStyle: { textAlign: 'left' }
      },
      getRowClass: (params: any) => {
        if (params.data.work_log_id == work_log_id) {
          return 'bg-primary-subtle';
        }
      },
      columnDefs: [
        { 
          headerName: 'Date', 
          field: 'date', 
          width: 120, 
          cellDataType: 'date' 
        },
        { 
          headerName: 'Description', 
          field: 'description', 
          flex: 1, 
          wrapText: true, 
          autoHeight: true 
        }
      ]
    };
  }
};

const setKnifeFilter = (gridApi: agGrid.GridApi<any>, knife_filter: knife_filter_model | null): void => {
  if (knife_filter && knife_filter.brand) {
    gridApi.setColumnFilterModel('brand', { filter: knife_filter?.brand, type: 'equals' });
  } else if (knife_filter && knife_filter.vendor) {
    if (knife_filter.vendor !== 'Unknown') {
      gridApi.setColumnFilterModel('vendor', { filter: knife_filter?.vendor, type: 'equals' });
    } else {
      gridApi.setColumnFilterModel('vendor', { type: 'blank' })
    }
  }
}

export {
  loadBladeGrid,
  loadKnifeGrid,
  loadSharpenerGrid,
  loadWorkLogGrid
};