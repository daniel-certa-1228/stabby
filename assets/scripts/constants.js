'use strict';

let baseUrl = "https://stabby.tech/";

const setBaseUrl = (isProduction) => {
    if (isProduction) {
        baseUrl = 'https://stabby.tech/';
    } else {
        baseUrl = "http://127.0.0.1:8000/";
    }
};

const getBaseUrl = () => {
    return baseUrl;
};

export { 
    getBaseUrl, 
    setBaseUrl
};
