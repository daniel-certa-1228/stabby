'use strict';

const deleteEntity = async (url: string): Promise<boolean | undefined> => {
  try {
    const response: Response = await fetch(url);
    const data: boolean | undefined = await response.json();

    return data;
  } catch (error: any) {
    console.error('Error deleting:', error);
  }
};

const getKnifeGrid = async (url: string): Promise<any> => {
  try {
    const response: Response = await fetch(url);
    const data: any = await response.json();

    return data;
  } catch (error: any) {
    console.error('Error fetching knife grid data:', error);
  }
};

const getSharpenerGrid = async (url: string): Promise<any> => {
  try {
    const response: Response = await fetch(url);
    const data: any = await response.json();

    return data;
  } catch (error: any) {
    console.error('Error fetching sharpener grid data:', error);
  }
};

const getBladeGrid = async (url: string): Promise<any> => {
  try {
    const response: Response = await fetch(url);
    const data: any = await response.json();

    return data;
  } catch (error: any) {
    console.error('Error fetching blade grid data:', error);
  }
};

const getWorkLogGrid = async (url: string): Promise<any> => {
  try {
    const response: Response= await fetch(url);
    const data: any = await response.json();

    return data;
  } catch (error: any) {
    console.error('Error fetching work log grid data:', error);
  }
};

export {
  deleteEntity,
  getBladeGrid,
  getKnifeGrid,
  getSharpenerGrid,
  getWorkLogGrid
};