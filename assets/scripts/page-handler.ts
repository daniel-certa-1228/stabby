'use strict';

import { enums } from './index';
import { grid_loader } from './index';
import { constants } from './index';

document.addEventListener('DOMContentLoaded', function () {
  var variables: any = JSON.parse(document.getElementById('template-variables')?.textContent || "");

  constants.setBaseUrl(variables['is_production']);

  switch (variables['view_type']) {
    case enums.ViewTypes.KnifeGrid:
      grid_loader.loadKnifeGrid();
      break;
    case enums.ViewTypes.SharpenerGrid:
      grid_loader.loadSharpenerGrid();
      break;
    case enums.ViewTypes.KnifeDetail: {
      const knife_id: number = variables['knife_id'];

      if (!isNaN(knife_id)) {
        grid_loader.loadBladeGrid(knife_id);
        grid_loader.loadWorkLogGrid(true, true, knife_id);
      } else {
        console.log('Invalid Knife ID');
      }
    }
      break;
    case enums.ViewTypes.SharpenerDetail: {
      const sharpener_id: number = variables['sharpener_id'];

      if (!isNaN(sharpener_id)) {
        grid_loader.loadWorkLogGrid(true, false, sharpener_id);
      } else {
        console.log('Invalid Sharpener ID');
      }
    }
      break;
    case enums.ViewTypes.KnifeWorkLogAddEdit: {
      const knife_id: number = variables['knife_id'];
      const work_log_id: number | null = variables['work_log_id'];

      if (!isNaN(knife_id)) {
        grid_loader.loadWorkLogGrid(false, true, knife_id, work_log_id);
      } else {
        console.log('Invalid Knife ID');
      }
    }
      break;
    case enums.ViewTypes.SharpenerWorkLogAddEdit: {
      const sharpener_id: number = variables['sharpener_id'];
      const work_log_id: number | null = variables['work_log_id'];

      if (!isNaN(sharpener_id)) {
        grid_loader.loadWorkLogGrid(false, false, sharpener_id, work_log_id);
      } else {
        console.log('Invalid Sharpener ID');
      }
    }
      break;
    case enums.ViewTypes.KnifeAddEdit:
    case enums.ViewTypes.SharpenerAddEdit:
    case enums.ViewTypes.BladeAddEdit:
    case enums.ViewTypes.KnifePhotoAddEdit:
    case enums.ViewTypes.SharpenerPhotoAddEdit:
      break;
    default:
      console.log(`Error: No Path`);
  }
});