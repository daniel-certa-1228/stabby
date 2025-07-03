'use strict'

export class knife_filter_model {
    brand: string;
    vendor: string;
    blade_material: string;
    handle_material: string;
    knife_type: string;
    purchased_new: boolean;
    blade_shape_id: number;
  
    constructor(
        brand: string,
        vendor: string,
        blade_material: string,
        handle_material: string,
        knife_type: string,
        purchased_new: boolean,
        blade_shape_id: number,
    ) {
        this.brand = brand;
        this.vendor = vendor;
        this.blade_material = blade_material;
        this.handle_material = handle_material;
        this.knife_type = knife_type;
        this.purchased_new = purchased_new;
        this.blade_shape_id = blade_shape_id;
    }
}