'use strict';

import { constants } from "./index";
import { knife_filter_model } from "./models/knife-filter-model";

const redirectToBladeEditPage_abs = (blade_id: number, knife_id: number): void => {
    window.location.href = `${constants.getBaseUrl()}knives/detail/${knife_id}/blades/edit/${blade_id}`;
};

const redirectToKnifeDetailPage_abs = (knife_id: number): void => {
    window.location.href = `${constants.getBaseUrl()}knives/detail/${knife_id}`;
};

const redirectToKnifeDetailPage_rel = (knife_id: number): void => {
    window.location.href = `knives/detail/${knife_id}`;
};

const redirectToKnifeDetailPageWlCard_abs = (knife_id: number): void => {
    window.location.href = `${constants.getBaseUrl()}knives/detail/${knife_id}#work_log_card`;
};

const redirectToKnifeGridPage_abs = (): void => {
    window.location.href = `${constants.getBaseUrl()}knives`;
};

const redirectToLibraryPage_abs = (): void => {
    window.location.href = `${constants.getBaseUrl()}library`;
}

const redirectToKnifeGridPage_rel = (filterParams: knife_filter_model | null): void => {
    let url = '/knives';

    if (filterParams) {
        if (filterParams.country) {
            url += `?country=${filterParams.country}`;
        }
    }

    window.location.href = url;
}

const redirectToSharpenerDetailPage_abs = (sharpener_id: number): void => {
    window.location.href = `${constants.getBaseUrl()}sharpeners/detail/${sharpener_id}`;
};

const redirectToSharpenerDetailPage_rel = (sharpener_id: number): void => {
    window.location.href = `detail/${sharpener_id}`;
};

const redirectToSharpenerDetailPageWlCard_abs = (sharpener_id: number): void => {
    window.location.href = `${constants.getBaseUrl()}sharpeners/detail/${sharpener_id}#work_log_card`;
};

const redirectToSharpenerGridPage_abs = (): void => {
    window.location.href = `${constants.getBaseUrl()}sharpeners`;
};

const redirectToWorkLogEditPage_rel = (work_log_id: number, entity_id: number, is_knife_wl: boolean): void => {
    if (is_knife_wl) {
        window.location.href = `/knives/detail/${entity_id}/work-logs/edit/${work_log_id}`;
    } else {
        window.location.href = `/sharpeners/detail/${entity_id}/work-logs/edit/${work_log_id}`;
    }
};

export { 
    redirectToBladeEditPage_abs,
    redirectToKnifeDetailPage_abs,  
    redirectToKnifeDetailPage_rel, 
    redirectToKnifeDetailPageWlCard_abs,
    redirectToKnifeGridPage_abs,
    redirectToKnifeGridPage_rel,
    redirectToLibraryPage_abs,
    redirectToSharpenerDetailPage_abs,
    redirectToSharpenerDetailPage_rel,
    redirectToSharpenerDetailPageWlCard_abs,
    redirectToSharpenerGridPage_abs,
    redirectToWorkLogEditPage_rel
};