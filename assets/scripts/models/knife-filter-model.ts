'use strict'

export class knife_filter_model {
    brand: string;
    vendor: string;
    blade_material: string;
    handle_material: string;
    purchased_new: boolean;
  
    constructor(
        brand: string,
        vendor: string,
        blade_material: string,
        handle_material: string,
        purchased_new: boolean,
    ) {
        this.brand = brand;
        this.vendor = vendor;
        this.blade_material = blade_material;
        this.handle_material = handle_material;
        this.purchased_new = purchased_new;
    }
}