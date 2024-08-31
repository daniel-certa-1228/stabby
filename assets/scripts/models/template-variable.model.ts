'use strict'

import { knife_filter_model } from "./knife-filter-model";

export class template_variable_model {
    view_type: number;
    is_production: boolean;
    knife_id: number;
    sharpener_id: number;
    blade_id: number;
    work_log_id: number;
    photo_id: number;
    knife_filter: knife_filter_model | null

    constructor(
        view_type: number,
        is_production: boolean,
        knife_id: number,
        sharpener_id: number,
        blade_id: number,
        work_log_id: number,
        photo_id: number,
        knife_filter: knife_filter_model
    ) {
        this.view_type = view_type;
        this.is_production = is_production;
        this.knife_id = knife_id;
        this.sharpener_id = sharpener_id;
        this.blade_id = blade_id;
        this.work_log_id = work_log_id;
        this.photo_id = photo_id;
        this.knife_filter = knife_filter
    }
}