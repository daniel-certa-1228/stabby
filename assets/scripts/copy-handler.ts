'use strict';

import { 
    ajax_handler, 
    constants, 
    redirect_handler } from "./index";

const copyKnife = async (knife_id: number): Promise<void> => {
    if (window.confirm("Are you sure you want to copy this Knife?")) {
      const url: string = `${constants.getBaseUrl()}api/copy_knife/${knife_id}/`;
  
      const new_knife_id: number | undefined = await ajax_handler.copyKnife(url);
  
      if (new_knife_id !== undefined 
            && new_knife_id !== -1) {
        redirect_handler.redirectToKnifeDetailPage_abs(new_knife_id);
      }
    }
  };

  export {
    copyKnife
  };