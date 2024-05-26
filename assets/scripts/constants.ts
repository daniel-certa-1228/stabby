'use strict';

let baseUrl: string = "https://stabby.tech/";

const setBaseUrl = (isProduction: boolean): void => {
    if (!isProduction) {
        baseUrl = "http://127.0.0.1:8000/";
    }
};

const getBaseUrl = (): string => {
    return baseUrl;
};

export { 
    getBaseUrl, 
    setBaseUrl
};
