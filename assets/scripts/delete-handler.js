'use strict';

import { baseUrl } from "./constants";

const deleteBlade = (blade_id, knife_id) => {
    if (window.confirm("Are you sure you want to delete this Blade?")) {
        const url = `${baseUrl}api/delete_blade/${blade_id}/`;

        // REPLACE WITH CALL TO AJAX HANDLER AND REDIRECT HANDLER
        let xhr_wl = new XMLHttpRequest();
        xhr_wl.open('GET', url, true);
        xhr_wl.onreadystatechange = () => {
            if (xhr_wl.readyState === 4 && xhr_wl.status === 200) {
                var responseData = JSON.parse(xhr_wl.responseText);
                if (responseData) {
                    window.location.href = `${baseUrl}/knives/detail/${knife_id}`;
                }
            }
        };
        xhr_wl.send();
    }
};

const deleteKnife = (knife_id) => {
    if (window.confirm("Are you sure you want to delete this Knife?")) {
        const url = `${baseUrl}api/delete_knife/${knife_id}/`;

        // REPLACE WITH CALL TO AJAX HANDLER AND REDIRECT HANDLER
        let xhr_wl = new XMLHttpRequest();
        xhr_wl.open('GET', url, true);
        xhr_wl.onreadystatechange = () => {
            if (xhr_wl.readyState === 4 && xhr_wl.status === 200) {
                var responseData = JSON.parse(xhr_wl.responseText);
                if (responseData) {
                    window.location.href = `${baseUrl}`;
                }
            }
        };
        xhr_wl.send();
    }
};

const deleteSharpener = (sharpener_id) => {
    if (window.confirm("Are you sure you want to delete this Sharpener?")) {
        const url = `${baseUrl}api/delete_sharpener/${sharpener_id}/`;

        // REPLACE WITH CALL TO AJAX HANDLER AND REDIRECT HANDLER
        let xhr_wl = new XMLHttpRequest();
        xhr_wl.open('GET', url, true);
        xhr_wl.onreadystatechange = () => {
            if (xhr_wl.readyState === 4 && xhr_wl.status === 200) {
                var responseData = JSON.parse(xhr_wl.responseText);
                if (responseData) {
                    window.location.href = `${baseUrl}/sharpeners`;
                }
            }
        };
        xhr_wl.send();
    }
};

const deleteWorkLog = (work_log_id, entity_id, is_knife_wl) => {
    if (window.confirm("Are you sure you want to delete this Work Log?")) {
        const url = `${baseUrl}api/delete_work_log/${work_log_id}/`;

        // REPLACE WITH CALL TO AJAX HANDLER AND REDIRECT HANDLER
        let xhr_wl = new XMLHttpRequest();
        xhr_wl.open('GET', url, true);
        xhr_wl.onreadystatechange = () => {
            if (xhr_wl.readyState === 4 && xhr_wl.status === 200) {
                var responseData = JSON.parse(xhr_wl.responseText);
                if (responseData) {
                    if (is_knife_wl) {
                        window.location.href = `${baseUrl}/knives/detail/${entity_id}#work_log_card`;
                    } else {
                        window.location.href = `${baseUrl}/sharpeners/detail/${entity_id}#work_log_card`;
                    }
                }
            }
        };
        xhr_wl.send();
    }
};

export { 
    deleteBlade, 
    deleteKnife, 
    deleteSharpener, 
    deleteWorkLog 
};