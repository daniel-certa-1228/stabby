'use strict'

export class chart_data_model {
    name: string;
    count: number;
    percentage: number;
  
    constructor(
        name: string,
        count: number,
        percentage: number,
    ) {
        this.name = name;
        this.count = count;
        this.percentage = percentage;
    }
}