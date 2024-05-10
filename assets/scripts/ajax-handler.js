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

const getKnifeGrid = () => {
    console.log('getKnifeGrid');
};

const getSharpenerGrid = () => {
    console.log('getSharpenerGrid');
};

const getBladeGrid = () => {
    console.log('getSharpenerGrid');
};

const getWorkLogGrid = () => {
    console.log('getSharpenerGrid');
};

export {  
    deleteEntity, 
    getBladeGrid, 
    getKnifeGrid, 
    getSharpenerGrid, 
    getWorkLogGrid 
};