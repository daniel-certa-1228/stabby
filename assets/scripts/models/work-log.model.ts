'use strict'

export class work_log_model {
    work_log_id: number;
    knife: number;
    sharpener: number;
    date: Date;
    description: string;
    is_active: boolean;
    create_date: Date;
    edit_date: Date;
    
    constructor(
        work_log_id: number,
        knife: number,
        sharpener: number,
        date: Date,
        description: string,
        is_active: boolean,
        create_date: Date,
        edit_date: Date,
    ) {
        this.work_log_id = work_log_id;
        this.knife = knife;
        this.sharpener = sharpener;
        this.date = date;
        this.description = description;
        this.is_active = is_active;
        this.create_date = create_date;
        this.edit_date = edit_date;
    }
}