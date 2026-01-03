'use strict'

export class knife_filter_model {
    brand: string | null = null;
    vendor: string | null = null;
    blade_material: string | null = null;
    handle_material: string | null = null;
    knife_type: string | null = null;
    purchased_new: boolean | null = null;
    blade_shape_id: number | null = null;
    country: string | null = null;
    deployment_type: string | null = null;
    lock_type: string | null = null;
  
    constructor(
        brand: string | null = null,
        vendor: string | null = null,
        blade_material: string | null = null,
        handle_material: string | null = null,
        knife_type: string | null = null,
        purchased_new: boolean | null = null,
        blade_shape_id: number | null = null,
        country: string | null = null,
        deployment_type: string | null = null,
        lock_type: string | null = null,
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