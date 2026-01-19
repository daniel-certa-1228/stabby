'use strict'

export class view_knife_grid_model {
    knife_id: number;
    knife: string;
    knife_type: string;
    brand: string;
    num_of_blades: number;
    blade_material: string;
    handle_material: string;
    lock_type: string;
    deployment_type: string;
    country: string;
    vendor: string;
    needs_work: boolean;
    purchased_new: boolean;
    is_active: boolean;
    create_date: Date | null;
    user_id: number;
    has_pocket_clip: boolean;

    constructor(
        knife_id: number,
        knife: string,
        knife_type: string,
        brand: string,
        num_of_blades: number,
        blade_material: string,
        handle_material: string,
        lock_type: string,
        deployment_type: string,
        country: string,
        vendor: string,
        needs_work: boolean,
        purchased_new: boolean,
        is_active: boolean,
        create_date: Date,
        user_id: number,
        has_pocket_clip: boolean,
    ) {
        this.knife_id = knife_id;
        this.knife = knife;
        this.knife_type = knife_type;
        this.brand = brand;
        this.num_of_blades = num_of_blades;
        this.blade_material = blade_material;
        this.handle_material = handle_material;
        this.lock_type = lock_type;
        this.deployment_type = deployment_type;
        this.country = country;
        this.vendor = vendor;
        this.needs_work = needs_work;
        this.purchased_new = purchased_new;
        this.is_active = is_active;
        this.create_date = create_date;
        this.user_id = user_id;
        this.has_pocket_clip = has_pocket_clip;
    }
}