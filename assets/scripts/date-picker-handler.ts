'use strict';

import { 
    ajax_handler,
    bootstrap, 
    constants } from './index';

const initDateHandling = (): void => {
    const datePicker: HTMLInputElement = document.getElementById('lastPurchaseDate') as HTMLInputElement;

    const csrfToken: string = (document.querySelector('[name=csrfmiddlewaretoken]') as HTMLInputElement).value;

    const url: string = `${constants.getBaseUrl()}api/set_last_purchase_date/`;

    const successToast: bootstrap.Toast = new bootstrap.Toast(document.getElementById('successToast') as HTMLElement);

    const errorToast: bootstrap.Toast = new bootstrap.Toast(document.getElementById('errorToast') as HTMLElement);

    const handleChange = async (): Promise<void> => {
        const selectedDate = datePicker.value;

        const success = await ajax_handler.setLastPurchaseDate(url, csrfToken, selectedDate);

        if (success) {
            successToast.show();
        } else {
            errorToast.show();
        }
    };

    datePicker.addEventListener('change', handleChange);
}

export { initDateHandling }

