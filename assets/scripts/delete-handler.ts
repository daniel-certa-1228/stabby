'use strict';

import { constants } from "./index";
import { redirect_handler } from "./index";
import { ajax_handler } from "./index";

const deleteBlade = async (blade_id: number, knife_id: number): Promise<void> => {
  if (window.confirm("Are you sure you want to delete this Blade?")) {
    const url: string = `${constants.getBaseUrl()}api/delete_blade/${blade_id}/`;

    const delete_successful: boolean | undefined = await ajax_handler.deleteEntity(url);

    if (delete_successful) {
      redirect_handler.redirectToKnifeDetailPage_abs(knife_id);
    }
  };
};

const deleteKnife = async (knife_id: number): Promise<void> => {
  if (window.confirm("Are you sure you want to delete this Knife?")) {
    const url: string = `${constants.getBaseUrl()}api/delete_knife/${knife_id}/`;

    const delete_successful: boolean | undefined = await ajax_handler.deleteEntity(url);

    if (delete_successful) {
      redirect_handler.redirectToIndexPage_abs();
    }
  }
};

const deleteSharpener = async (sharpener_id: number): Promise<void> => {
  if (window.confirm("Are you sure you want to delete this Sharpener?")) {
    const url: string = `${constants.getBaseUrl()}api/delete_sharpener/${sharpener_id}/`;

    const delete_successful: boolean | undefined = await ajax_handler.deleteEntity(url);

    if (delete_successful) {
      redirect_handler.redirectToSharpenerGridPage_abs();
    }
  }
};

const deleteWorkLog = async (work_log_id: number, entity_id: number, is_knife_wl: boolean): Promise<void> => {
  if (window.confirm("Are you sure you want to delete this Work Log?")) {
    const url: string = `${constants.getBaseUrl()}api/delete_work_log/${work_log_id}/`;

    const delete_successful: boolean | undefined = await ajax_handler.deleteEntity(url);

    if (delete_successful) {
      if (is_knife_wl) {
        redirect_handler.redirectToKnifeDetailPageWlCard_abs(entity_id);
      } else {
        redirect_handler.redirectToSharpenerDetailPageWlCard_abs(entity_id);
      }
    }
  }
};

const deletePhoto = async (photo_id: number, entity_id: number, is_knife_photo: boolean): Promise<void> => {
  if (window.confirm("Are you sure you want to delete this Photo?")) {
    const url: string = `${constants.getBaseUrl()}api/delete_photo/${photo_id}/`;

    const delete_successful: boolean | undefined = await ajax_handler.deleteEntity(url);

    if (delete_successful) {
      if (is_knife_photo) {
        redirect_handler.redirectToKnifeDetailPage_abs(entity_id);
      } else {
        redirect_handler.redirectToSharpenerDetailPage_abs(entity_id);
      }
    }
  }
};

export {
  deleteBlade,
  deleteKnife,
  deletePhoto,
  deleteSharpener,
  deleteWorkLog
};