'use strict';

import { enums } from './index';
import { grid_loader } from './index';

document.addEventListener('DOMContentLoaded', function() {
    var variables = JSON.parse(document.getElementById('template-variables').textContent);

    switch (variables['view_type']) {
        case enums.ViewTypes.KnifeGrid:
            grid_loader.loadKnifeGrid();
            break;
        case enums.ViewTypes.SharpenerGrid:
            grid_loader.loadSharpenerGrid();
            break;
        case enums.ViewTypes.KnifeDetail: {
            const knife_id = variables['knife_id'];

              if (!isNaN(knife_id)) {
                  grid_loader.loadBladeGrid(knife_id);
              } else {
                  console.log('Invalid Knife ID');
              }
            }
            break;
        case enums.ViewTypes.SharpenerDetail:
            console.log('SharpenerDetail');
            break;
        case enums.ViewTypes.KnifeAddEdit:
            console.log('KnifeAddEdit');
            break;
        case enums.ViewTypes.SharpenerAddEdit:
            console.log('SharpenerAddEdit');
            break;
        case enums.ViewTypes.BladeAddEdit:
            console.log('BladeAddEdit');
            break;
        case enums.ViewTypes.KnifeWorkLogAddEdit:
            console.log('KnifeWorkLogAddEdit');
            break;
        case enums.ViewTypes.SharpenerWorkLogAddEdit:
            console.log('SharpenerWorkLogAddEdit');
            break;
        default:
          console.log(`No Path`);
      }
  });