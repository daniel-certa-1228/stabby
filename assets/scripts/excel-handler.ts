'use strict';

const setKnifeExcelEventHandler = (): void => {
    const exportBtn = document.getElementById("knife-excel-btn");

    if (exportBtn) {
        exportBtn.addEventListener("click", function () {
            window.location.href = "/knives/export";
        });
    }
}

export {
    setKnifeExcelEventHandler
}