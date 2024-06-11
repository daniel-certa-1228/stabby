'use strict'

export class view_sharpener_grid_model {
    sharpener_id: number;
    sharpener: string;
    brand: string;
    cutting_agent: string;
    bonding_agent: string;
    length: string;
    width: string;
    country: string;
    is_friable: boolean;
    is_active: boolean;
    user_id: number;
    
    constructor(
        sharpener_id: number,
        sharpener: string,
        brand: string,
        cutting_agent: string,
        bonding_agent: string,
        length: string,
        width: string,
        country: string,
        is_friable: boolean,
        is_active: boolean,
        user_id: number,
    ) {
        this.sharpener_id = sharpener_id;
        this.sharpener = sharpener;
        this.brand = brand;
        this.cutting_agent = cutting_agent;
        this.bonding_agent = bonding_agent;
        this.length = length;
        this.width = width;
        this.is_friable = is_friable;
        this.country = country;
        this.is_active = is_active;
        this.user_id = user_id;
    }
}