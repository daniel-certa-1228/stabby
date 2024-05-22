'use strict';

import { baseUrl } from "./constants";

const redirectToBladeEditPage_abs = (blade_id, knife_id) => {
    window.location.href = `${baseUrl}/knives/detail/${knife_id}/blades/edit/${blade_id}`;
};

const redirectToKnifeDetailPage_abs = (knife_id) => {
    window.location.href = `${baseUrl}/knives/detail/${knife_id}`;
};

const redirectToKnifeDetailPage_rel = (knife_id) => {
    window.location.href = `knives/detail/${knife_id}`;
};

const redirectToKnifeDetailPageWlCard_abs = (knife_id) => {
    window.location.href = `${baseUrl}/knives/detail/${knife_id}#work_log_card`;
};

const redirectToIndexPage_abs = () => {
    window.location.href = `${baseUrl}`;
};

const redirectToSharpenerDetailPage_abs = (sharpener_id) => {
    window.location.href = `${baseUrl}/sharpeners/detail/${sharpener_id}`;
};

const redirectToSharpenerDetailPage_rel = (sharpener_id) => {
    window.location.href = `detail/${sharpener_id}`;
};

const redirectToSharpenerDetailPageWlCard_abs = (sharpener_id) => {
    window.location.href = `${baseUrl}/sharpeners/detail/${sharpener_id}#work_log_card`;
};

const redirectToSharpenerGridPage_abs = () => {
    window.location.href = `${baseUrl}/sharpeners`;
};

const redirectToWorkLogEditPage_rel = (work_log_id, entity_id, is_knife_wl) => {
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
    redirectToIndexPage_abs,
    redirectToSharpenerDetailPage_abs,
    redirectToSharpenerDetailPage_rel,
    redirectToSharpenerDetailPageWlCard_abs,
    redirectToSharpenerGridPage_abs,
    redirectToWorkLogEditPage_rel
};