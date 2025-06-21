'use strict';

const setKnifeExcelEventHandler = (): void => {
    const exportBtn: HTMLElement | null = document.getElementById("knife-excel-btn");

    if (exportBtn) {
        exportBtn.addEventListener("click", function () {
            window.location.href = "/knives/export";
        });
    }
}

const setSharpenerExcelEventHandler = (): void => {
    const exportBtn: HTMLElement | null = document.getElementById("sharpener-excel-btn");

    if (exportBtn) {
        exportBtn.addEventListener("click", function () {
            window.location.href = "/sharpeners/export";
        });
    }
}

export {
    setKnifeExcelEventHandler,
    setSharpenerExcelEventHandler
}