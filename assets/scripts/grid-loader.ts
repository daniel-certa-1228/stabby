'use strict';

import { agGrid } from './index';
import { ajax_handler } from './index';
import { constants } from './index';

const loadKnifeGrid = async (): Promise<void> => {
  const gridDiv: HTMLElement = document.querySelector('#grid')!;

  const gridOptions: any = {
    pagination: true,
    paginationPageSize: 50,
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
      },
      { headerName: 'Brand', field: 'brand', width: 220, pinned: 'left' },
      { headerName: 'Knife', field: 'knife', width: 350, pinned: 'left' },
      { headerName: '# of Blades', field: 'num_of_blades', width: 120, cellStyle: { textAlign: 'right' } },
      { headerName: 'Blade Material', field: 'blade_material', width: 280 },
      { headerName: 'Handle Material', field: 'handle_material', width: 160 },
      { headerName: 'Lock', field: 'lock_type', width: 120 },
      { headerName: 'Deployment', field: 'deployment_type', width: 140 },
      { headerName: 'Country', field: 'country', width: 140 },
      { headerName: 'Vendor', field: 'vendor', width: 220 },
      { headerName: 'Needs Work', field: 'needs_work', width: 140, cellStyle: { textAlign: 'center' } },
    ]
  };

  const gridApi = agGrid.createGrid(gridDiv, gridOptions);

  const url = `${constants.getBaseUrl()}api/get_knife_grid`;

  const rowData = await ajax_handler.getKnifeGrid(url);

  gridApi.setGridOption('rowData', rowData);
};

const loadSharpenerGrid = async (): Promise<void> => {
  const gridDiv: HTMLElement = document.querySelector('#grid')!;

  const gridOptions: any = {
    defaultColDef: {
      filter: true,
      cellStyle: { textAlign: 'left' }
    },
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
      },
      { headerName: 'Brand', field: 'brand', width: 220, pinned: 'left' },
      { headerName: 'Sharpener', field: 'sharpener', width: 400, pinned: 'left' },
      { headerName: 'Cutting Agent', field: 'cutting_agent', minWidth: 160 },
      { headerName: 'Bonding Agent', field: 'bonding_agent', minWidth: 190 },
      { headerName: 'Length', field: 'length', width: 120 },
      { headerName: 'Width', field: 'width', width: 120 },
      { headerName: 'Country', field: 'country', width: 140 },
      { headerName: 'Friable', field: 'is_friable', width: 140, cellStyle: { textAlign: 'center' } },
    ]
  };

  const gridApi = agGrid.createGrid(gridDiv, gridOptions);

  const url = `${constants.getBaseUrl()}api/get_sharpener_grid`;

  const rowData = await ajax_handler.getSharpenerGrid(url);

  gridApi.setGridOption('rowData', rowData);
};

const loadBladeGrid = async (knife_id: number): Promise<void> => {
  const gridDiv: HTMLElement = document.querySelector('#blade_grid')!;

  const gridOptions: any = {
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
          return `<button class="btn btn-sm btn-light blade-edit-btn" value="[${params.data.blade_id}, ${knife_id}]"><i class="bi bi-pencil-square"></i></button>`;
        },
      },
      { headerName: 'Shape', field: 'blade_shape', minWidth: 135, maxWidth: 185 },
      { headerName: 'Length', field: 'length', width: 95 },
      { headerName: 'C.E. Length', field: 'length_cutting_edge', width: 105 },
      { headerName: 'Half-Stop', field: 'has_half_stop', width: 95 },
      { headerName: 'Main', field: 'is_main_blade', width: 70 },
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

  const gridApi = agGrid.createGrid(gridDiv, gridOptions);

  const url = `${constants.getBaseUrl()}api/get_blade_grid/${knife_id}`;

  const rowData = await ajax_handler.getSharpenerGrid(url);

  gridApi.setGridOption('rowData', rowData);
};

const loadWorkLogGrid = async (with_buttons: boolean, is_knife_wl: boolean, entity_id: number, work_log_id: number | null = null): Promise<void> => {
  const gridDiv_wl: HTMLElement = document.querySelector('#wl_grid')!;

  const gridOptions: any = returnWorkLogGridOptions(
    with_buttons,
    is_knife_wl,
    entity_id,
    work_log_id);

  const gridApi = agGrid.createGrid(gridDiv_wl, gridOptions);

  let url: string;

  if (is_knife_wl) {
    url = `${constants.getBaseUrl()}api/get_knife_work_log_grid/${entity_id}`;
  } else {
    url = `${constants.getBaseUrl()}api/get_sharpener_work_log_grid/${entity_id}`;
  }

  const rowData: any = await ajax_handler.getSharpenerGrid(url);

  rowData.forEach((d: any) => {
    d.date = d.date ? new Date(d.date) : null;
  });

  gridApi.setGridOption('rowData', rowData);
};

// Private Functions
const returnWorkLogGridOptions = (with_buttons: boolean, is_knife_wl: boolean, entity_id: number, work_log_id: number | null): any => {
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
        { headerName: 'Date', field: 'date', width: 120, cellDataType: 'date' },
        { headerName: 'Description', field: 'description', flex: 1, wrapText: true, autoHeight: true },
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
        { headerName: 'Date', field: 'date', width: 120, cellDataType: 'date' },
        { headerName: 'Description', field: 'description', flex: 1, wrapText: true, autoHeight: true }
      ]
    };
  }
};

export {
  loadBladeGrid,
  loadKnifeGrid,
  loadSharpenerGrid,
  loadWorkLogGrid
};