'use strict';

let baseUrl: string = "https://stabby.tech/";
let isMobile: boolean = false;

const setBaseUrl = (isProduction: boolean): void => {
    if (!isProduction) {
        baseUrl = "http://127.0.0.1:8000/";
    }
};

const getBaseUrl = (): string => {
    return baseUrl;
};

const setIsMobile = (): void => {
    isMobile = /Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(navigator.userAgent) || window.innerWidth <= 768;
}

const getIsMobile = (): boolean => {
    return isMobile;
}
    
export { 
    getBaseUrl, 
    setBaseUrl,
    getIsMobile,
    setIsMobile
};
