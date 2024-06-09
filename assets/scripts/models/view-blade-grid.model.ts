'use strict'

export class view_blade_grid_model {
    blade_id: number;
    knife_id: number;
    blade_shape: string;
    length: string;
    length_cutting_edge: string;
    has_half_stop: boolean;
    is_main_blade: boolean;
    is_active: boolean;
    constructor(
        blade_id: number,
        knife_id: number,
        blade_shape: string,
        length: string,
        length_cutting_edge: string,
        has_half_stop: boolean,
        is_main_blade: boolean,
        is_active: boolean,
    ) {
        this.blade_id = blade_id;
        this.knife_id = knife_id;
        this.blade_shape = blade_shape;
        this.length = length;
        this.length_cutting_edge = length_cutting_edge;
        this.has_half_stop = has_half_stop;
        this.is_main_blade = is_main_blade;
        this.is_active = is_active;
    }
}