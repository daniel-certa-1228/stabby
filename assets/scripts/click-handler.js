'use strict';

import { redirect_handler } from './index';
import { delete_handler } from './index';

document.addEventListener("click", function(e){
    const knifeDetailTarget = e.target.closest(".knife-detail-btn");
    const sharpenerDetailTarget = e.target.closest(".sharpener-detail-btn");
    const bladeEditTarget = e.target.closest(".blade-edit-btn");
    const bladeDeleteTarget = e.target.closest(".blade-delete-btn");
    const workLogEditTarget = e.target.closest(".wl-edit-btn");
    const workLogDeleteTarget = e.target.closest(".wl-delete-btn");

    if (knifeDetailTarget) {
      const knife_id = parseInt(knifeDetailTarget.value);

      if (!isNaN(knife_id)) {
        redirect_handler.redirectToKnifeDetailPage_rel(knife_id);
      }
    } else if (sharpenerDetailTarget) {
        const sharpener_id = parseInt(sharpenerDetailTarget.value);

        if (!isNaN(sharpener_id)) {
          redirect_handler.redirectToSharpenerDetailPage_rel(sharpener_id);
        }

    } else if (bladeEditTarget) {
       const arr = JSON.parse(bladeEditTarget.value);

        if (Array.isArray(arr)
            && arr.length === 2) {
            const blade_id = arr[0];
            const knife_id = arr[1];

            if (!isNaN(blade_id) && !isNaN(knife_id)) {
                redirect_handler.redirectToBladeEditPage_abs(blade_id, knife_id);
            }
        }
    } else if (bladeDeleteTarget) {
        const arr = JSON.parse(bladeDeleteTarget.value);

        if (Array.isArray(arr)
            && arr.length === 2) {
            const blade_id = arr[0];
            const knife_id = arr[1];

            if (!isNaN(blade_id) && !isNaN(knife_id)) {
                delete_handler.deleteBlade(blade_id, knife_id);
            }
        }

    }  else if (workLogEditTarget) {
        const arr = JSON.parse(workLogEditTarget.value);

        if (Array.isArray(arr)
          && arr.length === 3) {
          const work_log_id = arr[0];
          const entity_id = arr[1];
          const is_knife_wl = arr[2];

          if (!isNaN(work_log_id) && !isNaN(entity_id)) {
              if (is_knife_wl) {
                  redirect_handler.redirectToWorkLogEditPage_rel(work_log_id, entity_id, is_knife_wl);
              } else {
                  redirect_handler.redirectToWorkLogEditPage_rel(work_log_id, entity_id, is_knife_wl);
              }
          }
      }

    } else if (workLogDeleteTarget) {
      const arr = JSON.parse(workLogDeleteTarget.value);

      if (Array.isArray(arr)
          && arr.length === 3) {
          const work_log_id = arr[0];
          const entity_id = arr[1];
          const is_knife_wl = arr[2];

          if (!isNaN(work_log_id) && !isNaN(entity_id)) {
                  delete_handler.deleteWorkLog(work_log_id, entity_id, is_knife_wl);
          }
      }
    } else {
        console.log('Error: No Target');
    }
  });