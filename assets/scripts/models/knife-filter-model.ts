'use strict'

export class knife_filter_model {
    brand: string;
    vendor: string;
    blade_material: string;
    handle_material: string;
    knife_type: string;
    purchased_new: boolean;
    blade_shape_id: number;
    country: string;
    deployment_type: string;
    lock_type: string;
  
    constructor(
        brand: string,
        vendor: string,
        blade_material: string,
        handle_material: string,
        knife_type: string,
        purchased_new: boolean,
        blade_shape_id: number,
        country: string,
        deployment_type: string,
        lock_type: string,
    ) {
        this.brand = brand;
        this.vendor = vendor;
        this.blade_material = blade_material;
        this.handle_material = handle_material;
        this.knife_type = knife_type;
        this.purchased_new = purchased_new;
        this.blade_shape_id = blade_shape_id;
        this.country = country;
        this.deployment_type = deployment_type;
        this.lock_type = lock_type;
    }
}