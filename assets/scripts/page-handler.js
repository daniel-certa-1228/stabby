'use strict'

import { enums } from './index'

document.addEventListener('DOMContentLoaded', function() {
    var variables = JSON.parse(document.getElementById('template-variables').textContent);

    switch (variables['view_type']) {
        case enums.ViewTypes.KnifeGrid:
            console.log('KnifeGrid');
            break;
        case enums.ViewTypes.SharpenerGrid:
            console.log('SharpenerGrid');
            break;
        case enums.ViewTypes.KnifeDetail:
            console.log('KnifeDetail');
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