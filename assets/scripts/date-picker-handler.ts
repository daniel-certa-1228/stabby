'use strict';

import { 
    ajax_handler,
    bootstrap, 
    constants } from './index';

const initDateHandling = () => {
    const datePicker: HTMLInputElement = document.getElementById('lastPurchaseDate') as HTMLInputElement;

    // const successToast: bootstrap.Toast = new bootstrap.Toast(document.getElementById('successToast') as HTMLElement);

    const csrfToken: string = (document.querySelector('[name=csrfmiddlewaretoken]') as HTMLInputElement).value;

    const url: string = `${constants.getBaseUrl()}api/set_last_purchase_date/`;

    const handleChange = async () => {
        const selectedDate = datePicker.value;

        console.log(selectedDate);

        const success = await ajax_handler.setLastPurchaseDate(url, csrfToken, selectedDate);

        console.log(success)

        // if (success) {
        //     successToast.show();
        // }
    };

    datePicker.addEventListener('change', handleChange);
}

export { initDateHandling }

