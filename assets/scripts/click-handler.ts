'use strict';

import { redirect_handler } from './index';
import { delete_handler } from './index';

document.addEventListener("click", function (e) {
  const knifeDetailTarget = (e.target as Element)?.closest(".knife-detail-btn");
  const sharpenerDetailTarget = (e.target as Element)?.closest(".sharpener-detail-btn");
  const bladeEditTarget = (e.target as Element)?.closest(".blade-edit-btn");
  const workLogEditTarget = (e.target as Element)?.closest(".wl-edit-btn");

  const knifeDeleteTarget = (e.target as Element)?.closest("#knife-delete-btn");
  const sharpenerDeleteTarget = (e.target as Element)?.closest("#sharpener-delete-btn");
  const bladeDeleteTarget = (e.target as Element)?.closest(".blade-delete-btn");
  const workLogDeleteTarget = (e.target as Element)?.closest(".wl-delete-btn");
  const photoDeleteTarget = (e.target as Element)?.closest("#photo-delete-btn");

  if (knifeDetailTarget) {
    const knife_id = parseInt((knifeDetailTarget as HTMLInputElement).value);

    if (!isNaN(knife_id)) {
      redirect_handler.redirectToKnifeDetailPage_rel(knife_id);
    }
  } else if (sharpenerDetailTarget) {
    const sharpener_id = parseInt((sharpenerDetailTarget as HTMLInputElement).value);

    if (!isNaN(sharpener_id)) {
      redirect_handler.redirectToSharpenerDetailPage_rel(sharpener_id);
    }

  } else if (bladeEditTarget) {
    const bladeEditTargetInput = bladeEditTarget as HTMLInputElement;
    const arr = JSON.parse(bladeEditTargetInput.value);

    if (Array.isArray(arr)
      && arr.length === 2) {
      const blade_id = arr[0];
      const knife_id = arr[1];

      if (!isNaN(blade_id) && !isNaN(knife_id)) {
        redirect_handler.redirectToBladeEditPage_abs(blade_id, knife_id);
      }
    }
  } else if (workLogEditTarget) {
    const workLogEditTargetInput = workLogEditTarget as HTMLInputElement;
    const arr = JSON.parse(workLogEditTargetInput.value);

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
  } else if (knifeDeleteTarget) {
    const knife_id = parseInt((knifeDeleteTarget as HTMLInputElement).value);

    if (!isNaN(knife_id)) {
      delete_handler.deleteKnife(knife_id);
    }
  } else if (sharpenerDeleteTarget) {
    const sharpener_id = parseInt((sharpenerDeleteTarget as HTMLInputElement).value);

    if (!isNaN(sharpener_id)) {
      delete_handler.deleteSharpener(sharpener_id);
    }
  } else if (bladeDeleteTarget) {
    const bladeDeleteTargetInput = bladeDeleteTarget as HTMLInputElement; // Cast bladeDeleteTarget to HTMLInputElement
    const arr = JSON.parse(bladeDeleteTargetInput.value);

    if (Array.isArray(arr)
      && arr.length === 2) {
      const blade_id = arr[0];
      const knife_id = arr[1];

      if (!isNaN(blade_id) && !isNaN(knife_id)) {
        delete_handler.deleteBlade(blade_id, knife_id);
      }
    }
  } else if (workLogDeleteTarget) {
    const workLogDeleteTargetInput = workLogDeleteTarget as HTMLInputElement; // Cast workLogDeleteTarget to HTMLInputElement
    const arr = JSON.parse(workLogDeleteTargetInput.value);

    if (Array.isArray(arr)
      && arr.length === 3) {
      const work_log_id = arr[0];
      const entity_id = arr[1];
      const is_knife_wl = arr[2];

      if (!isNaN(work_log_id) && !isNaN(entity_id)) {
        delete_handler.deleteWorkLog(work_log_id, entity_id, is_knife_wl);
      }
    }
  } else if (photoDeleteTarget) {
    const photoDeleteTargetInput = photoDeleteTarget as HTMLInputElement; // Cast photoDeleteTarget to HTMLInputElement
    const arr = JSON.parse(photoDeleteTargetInput.value);
    
    if (Array.isArray(arr)
      && arr.length === 3) {
      const photo_id = arr[0];
      const entity_id = arr[1];
      const is_knife_photo = arr[2];

      if (!isNaN(photo_id) && !isNaN(entity_id)) {
        delete_handler.deletePhoto(photo_id, entity_id, is_knife_photo);
      }
    }
  }
});