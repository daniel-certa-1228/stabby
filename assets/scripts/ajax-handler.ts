'use strict';

import { 
  view_blade_grid_model,
  view_knife_grid_model, 
  view_sharpener_grid_model,
  work_log_model } from "./index";

const copyKnife = async (url: string): Promise<number | undefined> => {
  try {
    const response: Response = await fetch(url);
    const data: number | undefined = await response.json();

    return data;
  } catch (error: any) {
    console.error('Error copying:', error);
  }
};

const deleteEntity = async (url: string): Promise<boolean | undefined> => {
  try {
    const response: Response = await fetch(url);
    const data: boolean | undefined = await response.json();

    return data;
  } catch (error: any) {
    console.error('Error deleting:', error);
  }
};

const getKnifeGrid = async (url: string): Promise<view_knife_grid_model[] | undefined> => {
  try {
    const response: Response = await fetch(url);
    const data: view_knife_grid_model[] = await response.json();

    return data;
  } catch (error: any) {
    console.error('Error fetching knife grid data:', error);
  }
};

const getSharpenerGrid = async (url: string): Promise<view_sharpener_grid_model[] | undefined> => {
  try {
    const response: Response = await fetch(url);
    const data: view_sharpener_grid_model[] = await response.json();

    return data;
  } catch (error: any) {
    console.error('Error fetching sharpener grid data:', error);
  }
};

const getBladeGrid = async (url: string): Promise<view_blade_grid_model[] | undefined> => {
  try {
    const response: Response = await fetch(url);
    const data: view_blade_grid_model[] = await response.json();

    return data;
  } catch (error: any) {
    console.error('Error fetching blade grid data:', error);
  }
};

const getWorkLogGrid = async (url: string): Promise<work_log_model[] | undefined> => {
  try {
    const response: Response = await fetch(url);
    const data: work_log_model[] = await response.json();

    return data;
  } catch (error: any) {
    console.error('Error fetching work log grid data:', error);
  }
};

const setLastPurchaseDate = async (url: string, csrfToken: string, selectedDate: string): Promise<boolean | undefined> => {
  try {
    const response: Response =  await fetch(url, {
          method: 'POST',
          headers: {
              'Content-Type': 'application/x-www-form-urlencoded',
              'X-CSRFToken': csrfToken
          },
          body: JSON.stringify({ date: selectedDate }),
      })

      const data: boolean | undefined = await response.json();

      return data;
  } catch (error: any) {
    console.error('Error setting last purchase date:', error);
  }
}

export {
  copyKnife,
  deleteEntity,
  getBladeGrid,
  getKnifeGrid,
  getSharpenerGrid,
  getWorkLogGrid,
  setLastPurchaseDate
};