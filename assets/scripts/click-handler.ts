'use strict';

import { 
  delete_handler, 
  redirect_handler } from './index';

document.addEventListener("click", function (e) {
  //DETAIL
  const knifeDetailTarget: Element | null = (e.target as Element)?.closest(".knife-detail-btn");
  const sharpenerDetailTarget: Element | null = (e.target as Element)?.closest(".sharpener-detail-btn");
  //EDIT
  const bladeEditTarget: Element | null = (e.target as Element)?.closest(".blade-edit-btn");
  const workLogEditTarget: Element | null = (e.target as Element)?.closest(".wl-edit-btn");
  //DELETE
  const knifeDeleteTarget: Element | null = (e.target as Element)?.closest("#knife-delete-btn");
  const sharpenerDeleteTarget: Element | null = (e.target as Element)?.closest("#sharpener-delete-btn");
  const bladeDeleteTarget: Element | null = (e.target as Element)?.closest(".blade-delete-btn");
  const workLogDeleteTarget: Element | null = (e.target as Element)?.closest(".wl-delete-btn");
  const photoDeleteTarget: Element | null = (e.target as Element)?.closest("#photo-delete-btn");

  if (knifeDetailTarget) {
    const knife_id: number = parseInt((knifeDetailTarget as HTMLInputElement).value);

    if (!isNaN(knife_id)) {
      redirect_handler.redirectToKnifeDetailPage_rel(knife_id);
    }
  } else if (sharpenerDetailTarget) {
    const sharpener_id = parseInt((sharpenerDetailTarget as HTMLInputElement).value);

    if (!isNaN(sharpener_id)) {
      redirect_handler.redirectToSharpenerDetailPage_rel(sharpener_id);
    }

  } else if (bladeEditTarget) {
    const bladeEditTargetInput: HTMLInputElement = bladeEditTarget as HTMLInputElement;

    const arr: number[] = JSON.parse(bladeEditTargetInput.value);

    if (Array.isArray(arr)
      && arr.length === 2) {
      const blade_id: number = arr[0];
      const knife_id: number = arr[1];

      if (!isNaN(blade_id) && !isNaN(knife_id)) {
        redirect_handler.redirectToBladeEditPage_abs(blade_id, knife_id);
      }
    }
  } else if (workLogEditTarget) {
    const workLogEditTargetInput: HTMLInputElement = workLogEditTarget as HTMLInputElement;

    const arr: [number, number, boolean] = JSON.parse(workLogEditTargetInput.value);

    if (Array.isArray(arr)
      && arr.length === 3) {
      const work_log_id: number = arr[0];
      const entity_id: number = arr[1];
      const is_knife_wl: boolean = arr[2];

      if (!isNaN(work_log_id) && !isNaN(entity_id)) {
        if (is_knife_wl) {
          redirect_handler.redirectToWorkLogEditPage_rel(work_log_id, entity_id, is_knife_wl);
        } else {
          redirect_handler.redirectToWorkLogEditPage_rel(work_log_id, entity_id, is_knife_wl);
        }
      }
    }
  } else if (knifeDeleteTarget) {
    const knife_id: number = parseInt((knifeDeleteTarget as HTMLInputElement).value);

    if (!isNaN(knife_id)) {
      delete_handler.deleteKnife(knife_id);
    }
  } else if (sharpenerDeleteTarget) {
    const sharpener_id: number = parseInt((sharpenerDeleteTarget as HTMLInputElement).value);

    if (!isNaN(sharpener_id)) {
      delete_handler.deleteSharpener(sharpener_id);
    }
  } else if (bladeDeleteTarget) {
    const bladeDeleteTargetInput: HTMLInputElement = bladeDeleteTarget as HTMLInputElement; // Cast bladeDeleteTarget to HTMLInputElement

    const arr: number[] = JSON.parse(bladeDeleteTargetInput.value);

    if (Array.isArray(arr)
      && arr.length === 2) {
      const blade_id: number = arr[0];
      const knife_id: number = arr[1];

      if (!isNaN(blade_id) && !isNaN(knife_id)) {
        delete_handler.deleteBlade(blade_id, knife_id);
      }
    }
  } else if (workLogDeleteTarget) {
    const workLogDeleteTargetInput: HTMLInputElement = workLogDeleteTarget as HTMLInputElement; // Cast workLogDeleteTarget to HTMLInputElement

    const arr: [number, number, boolean] = JSON.parse(workLogDeleteTargetInput.value);

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
    const photoDeleteTargetInput: HTMLInputElement = photoDeleteTarget as HTMLInputElement; // Cast photoDeleteTarget to HTMLInputElement

    const arr: [number, number, boolean] = JSON.parse(photoDeleteTargetInput.value);
    
    if (Array.isArray(arr)
      && arr.length === 3) {
      const photo_id: number = arr[0];
      const entity_id: number = arr[1];
      const is_knife_photo: boolean = arr[2];

      if (!isNaN(photo_id) && !isNaN(entity_id)) {
        delete_handler.deletePhoto(photo_id, entity_id, is_knife_photo);
      }
    }
  }
});