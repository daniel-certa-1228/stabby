'use strict';

let baseUrl: string = "https://stabby.tech/";

const setBaseUrl = (isProduction: boolean) => {
    if (!isProduction) {
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
