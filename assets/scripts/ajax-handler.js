'use strict';

const deleteEntity = async (url) => {
  try {
    const response = await fetch(url);
    const data = await response.json();

    return data;
  } catch (error) {
    console.error('Error deleting:', error);
  }
};

const getKnifeGrid = async (url) => {
  try {
    const response = await fetch(url);
    const data = await response.json();

    return data;
  } catch (error) {
    console.error('Error fetching knife grid data:', error);
  }
};

const getSharpenerGrid = async (url) => {
  try {
    const response = await fetch(url);
    const data = await response.json();

    return data;
  } catch (error) {
    console.error('Error fetching sharpener grid data:', error);
  }
};

const getBladeGrid = async (url) => {
  try {
    const response = await fetch(url);
    const data = await response.json();

    return data;
  } catch (error) {
    console.error('Error fetching blade grid data:', error);
  }
};

const getWorkLogGrid = async (url) => {
  try {
    const response = await fetch(url);
    const data = await response.json();

    return data;
  } catch (error) {
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