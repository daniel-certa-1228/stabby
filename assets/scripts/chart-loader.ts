'use strict';

import {
    agCharts,
    ajax_handler,
    chart_data_model,
    constants,
    redirect_handler
}  from './index';
import { knife_filter_model } from './models/knife-filter-model';

const fill_1: string[] = ["#4D4993", "#027600", "#FD7E6D", "#82438B", "#CE5482", "#FFB85D", "#C4C454", "#006676", "#E6A902"];
const fill_2: string[] = ["#5166AF", "#444655", "#D1A617", "#7BB6B2", "#857555", "#741429", "#FF8FDB", "#853F00", "#5DE602"];

const loadCountryChart = async (): Promise<void> => {
    const chartDiv: HTMLElement = document.querySelector('#country-chart')!;

    const spinner: HTMLElement | null = document.querySelector('#country-chart-spinner');

    const url: string = `${constants.getBaseUrl()}api/get_country_chart_data`;

    const chartData: chart_data_model[] | undefined = await ajax_handler.getChartData(url);

    const breakPoint: number = 6

    const breakPointOther: number = 2

    const donut_1: chart_data_model[] | undefined = chartData?.filter(x => x.count >= breakPoint);
    
    //Aggregate "OTHER"
    const donut_2_raw: chart_data_model[] | undefined = chartData?.filter(x => x.count < breakPoint && x.count > breakPointOther);
    const other_raw: chart_data_model[] | undefined = chartData?.filter(x => x.count <= breakPointOther);
    const other: chart_data_model | null = convertToOther(other_raw);

    let donut_2: chart_data_model[];

    if (other) {
        donut_2 = [...(donut_2_raw || []), other];
    } else {
        donut_2 = [...(donut_2_raw || [])];
    }

    const options: agCharts.AgPolarChartOptions = {
        container: chartDiv,
        padding:{
            top: 5,
            right: 5,
            bottom: 5,
            left: 5
        },
        title: {
            text: "Country of Manufacture",
          },
        series: [
        {
            type: "donut",
            fills: fill_1,
            data: donut_1,
            calloutLabelKey: "name",
            legendItemKey: "name",
            angleKey: "count",
            outerRadiusRatio: 1,
            innerRadiusRatio: 0.8,
            showInLegend: false,
            tooltip: {
                renderer: (params) => {
                    const fillColor = (params as any).fill ?? '#888';
                    
                    return `
                        <div style="padding: 8px;">
                            <div style="display: flex; align-items: center; margin-bottom: 3px;">
                            <span style="background:${fillColor}; width:10px; height:10px; margin-right:6px;"></span>
                            <b>${params.datum.name}</b>
                            </div>
                            <div><span class="text-body-secondary"><b>Count:</b></span> ${params.datum.count}</div>
                            <div><span class="text-body-secondary"><b>Percent:</b></span> ${params.datum.percentage.toFixed(2)}%</div>
                        </div>
                    `;
                }
            },
            ...(constants.getIsMobile() ? {} : {
            listeners: {
                nodeClick: (event: agCharts.AgNodeClickEvent<"nodeClick", any>) => {
                    if (event) {
                        knife_grid_redirect(event, 'country');
                    }
                }
            }})
        },
        {
            type: "donut",
            fills: fill_2,
            data: donut_2,
            legendItemKey: "name",
            calloutLabelKey: "name",
            angleKey: "count",
            outerRadiusRatio: 0.5,
            innerRadiusRatio: 0.3,
            showInLegend: false,
            tooltip: {
                renderer: (params) => {
                  const fillColor = (params as any).fill ?? '#888';
                    
                    return `
                        <div style="padding: 8px;">
                            <div style="display: flex; align-items: center; margin-bottom: 3px;">
                            <span style="background:${fillColor}; width:10px; height:10px; margin-right:6px;"></span>
                            <b>${params.datum.name}</b>
                            </div>
                            <div><span class="text-body-secondary"><b>Count:</b></span> ${params.datum.count}</div>
                            <div><span class="text-body-secondary"><b>Percent:</b></span> ${params.datum.percentage.toFixed(2)}%</div>
                        </div>
                    `;
                }
            },
            ...(constants.getIsMobile() ? {} : {
            listeners: {
                nodeClick: (event: agCharts.AgNodeClickEvent<"nodeClick", any>) => {
                    if (event) {
                        knife_grid_redirect(event, 'country');
                    }
                }
            }})
        }
    ]};
   
    spinner?.remove();

    const chart: agCharts.AgChartInstance<agCharts.AgPolarChartOptions> = agCharts.AgCharts.create(options);
}

const loadDeploymentTypeChart = async (): Promise<void> => {
    const chartDiv: HTMLElement = document.querySelector('#deployment-type-chart')!;

    const spinner: HTMLElement | null = document.querySelector('#dt-chart-spinner');

    const url: string = `${constants.getBaseUrl()}api/get_deployment_type_chart_data`;

    const chartData: chart_data_model[] | undefined = await ajax_handler.getChartData(url);

    const breakPoint: number = 7

    const donut_1: chart_data_model[] | undefined = chartData?.filter(x => x.count >= breakPoint);

    const donut_2: chart_data_model[] | undefined = chartData?.filter(x => x.count < breakPoint);

    const options: agCharts.AgPolarChartOptions = {
        container: chartDiv,
        padding:{
            top: 5,
            right: 5,
            bottom: 0,
            left: 5
        },
        title: {
            text: "Deployment Types",
          },
        data: chartData,
        series: [
            {
                type: "donut",
                fills: fill_1,
                data: donut_1,
                calloutLabelKey: "name",
                legendItemKey: "name",
                angleKey: "count",
                outerRadiusRatio: 1,
                innerRadiusRatio: 0.8,
                showInLegend: false,
                tooltip: {
                    renderer: (params) => {
                        const fillColor = (params as any).fill ?? '#888';
                        
                        return `
                            <div style="padding: 8px;">
                                <div style="display: flex; align-items: center; margin-bottom: 3px;">
                                <span style="background:${fillColor}; width:10px; height:10px; margin-right:6px;"></span>
                                <b>${params.datum.name}</b>
                                </div>
                                <div><span class="text-body-secondary"><b>Count:</b></span> ${params.datum.count}</div>
                                <div><span class="text-body-secondary"><b>Percent:</b></span> ${params.datum.percentage.toFixed(2)}%</div>
                            </div>
                        `;
                    }
                },
                ...(constants.getIsMobile() ? {} : {
                listeners: {
                    nodeClick: (event: agCharts.AgNodeClickEvent<"nodeClick", any>) => {
                        if (event) {
                            knife_grid_redirect(event, 'deployment_type');
                        }
                    }
                }})
            },
            {
                type: "donut",
                fills: fill_2,
                data: donut_2,
                legendItemKey: "name",
                calloutLabelKey: "name",
                angleKey: "count",
                outerRadiusRatio: 0.5,
                innerRadiusRatio: 0.3,
                showInLegend: false,
                tooltip: {
                    renderer: (params) => {
                        const fillColor = (params as any).fill ?? '#888';
                        
                        return `
                            <div style="padding: 8px;">
                                <div style="display: flex; align-items: center; margin-bottom: 3px;">
                                <span style="background:${fillColor}; width:10px; height:10px; margin-right:6px;"></span>
                                <b>${params.datum.name}</b>
                                </div>
                                <div><span class="text-body-secondary"><b>Count:</b></span> ${params.datum.count}</div>
                                <div><span class="text-body-secondary"><b>Percent:</b></span> ${params.datum.percentage.toFixed(2)}%</div>
                            </div>
                        `;
                    }
                },
                ...(constants.getIsMobile() ? {} : {
                listeners: {
                    nodeClick: (event: agCharts.AgNodeClickEvent<"nodeClick", any>) => {
                        if (event) {
                            knife_grid_redirect(event, 'deployment_type');
                        }
                    }
                }})
            },
        ],
    };

    spinner?.remove();

    const chart: agCharts.AgChartInstance<agCharts.AgPolarChartOptions> = agCharts.AgCharts.create(options);
}

const loadLockTypeChart = async (): Promise<void> => {
    const chartDiv: HTMLElement = document.querySelector('#lock-type-chart')!;

    const spinner: HTMLElement | null = document.querySelector('#lt-chart-spinner');

    const url: string = `${constants.getBaseUrl()}api/get_lock_type_chart_data`;

    const chartData: chart_data_model[] | undefined = await ajax_handler.getChartData(url);

    const breakPoint: number = 6

    const donut_1: chart_data_model[] | undefined = chartData?.filter(x => x.count >= breakPoint);

    const donut_2: chart_data_model[] | undefined = chartData?.filter(x => x.count < breakPoint);

    const options: agCharts.AgPolarChartOptions = {
        container: chartDiv,
        padding:{
            top: 5,
            right: 5,
            bottom: 0,
            left: 5
        },
        title: {
            text: "Lock Types",
          },
        data: chartData,
        series: [
            {
                type: "donut",
                fills: fill_1,
                data: donut_1,
                calloutLabelKey: "name",
                legendItemKey: "name",
                angleKey: "count",
                outerRadiusRatio: 1,
                innerRadiusRatio: 0.8,
                showInLegend: false,
                tooltip: {
                    renderer: (params) => {
                        const fillColor = (params as any).fill ?? '#888';
                        
                        return `
                            <div style="padding: 8px;">
                                <div style="display: flex; align-items: center; margin-bottom: 3px;">
                                <span style="background:${fillColor}; width:10px; height:10px; margin-right:6px;"></span>
                                <b>${params.datum.name}</b>
                                </div>
                                <div><span class="text-body-secondary"><b>Count:</b></span> ${params.datum.count}</div>
                                <div><span class="text-body-secondary"><b>Percent:</b></span> ${params.datum.percentage.toFixed(2)}%</div>
                            </div>
                        `;
                    }
                },
                ...(constants.getIsMobile() ? {} : {
                listeners: {
                    nodeClick: (event: agCharts.AgNodeClickEvent<"nodeClick", any>) => {
                        if (event) {
                            knife_grid_redirect(event, 'lock_type');
                        }
                    }
                }})
            },
            {
                type: "donut",
                fills: fill_2,
                data: donut_2,
                legendItemKey: "name",
                calloutLabelKey: "name",
                angleKey: "count",
                outerRadiusRatio: 0.5,
                innerRadiusRatio: 0.3,
                showInLegend: false,
                tooltip: {
                    renderer: (params) => {
                        const fillColor = (params as any).fill ?? '#888';
                        
                        return `
                             <div style="padding: 8px;">
                                <div style="display: flex; align-items: center; margin-bottom: 3px;">
                                <span style="background:${fillColor}; width:10px; height:10px; margin-right:6px;"></span>
                                <b>${params.datum.name}</b>
                                </div>
                                <div><span class="text-body-secondary"><b>Count:</b></span> ${params.datum.count}</div>
                                <div><span class="text-body-secondary"><b>Percent:</b></span> ${params.datum.percentage.toFixed(2)}%</div>
                            </div>
                        `;
                    }
                },
                ...(constants.getIsMobile() ? {} : {
                listeners: {
                    nodeClick: (event: agCharts.AgNodeClickEvent<"nodeClick", any>) => {
                        if (event) {
                            knife_grid_redirect(event, 'lock_type');
                        }
                    }
                }})
            },
        ],
    };
    
    spinner?.remove();

    const chart: agCharts.AgChartInstance<agCharts.AgPolarChartOptions> = agCharts.AgCharts.create(options);
}

const loadSteelTypeChart = async (): Promise<void> => {
    const chartDiv: HTMLElement = document.querySelector('#steel-type-chart')!;

    const spinner: HTMLElement | null = document.querySelector('#st-chart-spinner');

    const url: string = `${constants.getBaseUrl()}api/get_steel_type_chart_data`;

    const chartData: chart_data_model[] | undefined = await ajax_handler.getChartData(url);

    const options: agCharts.AgPolarChartOptions = {
        container: chartDiv,
        padding:{
            top: 5,
            right: 5,
            bottom: 5,
            left: 5
        },
        title: {
            text: "Steel Types",
          },
        data: chartData,
        series: [{
            type: "pie",
            fills: fill_1,
            angleKey: "count",
            legendItemKey: "name",
            angleName: "Steel Types",
            tooltip: {
                renderer: (params) => {
                    const fillColor = (params as any).fill ?? '#888';
                    
                    return `
                       <div style="padding: 8px;">
                            <div style="display: flex; align-items: center; margin-bottom: 3px;">
                            <span style="background:${fillColor}; width:10px; height:10px; margin-right:6px;"></span>
                            <b>${params.datum.name}</b>
                            </div>
                            <div><span class="text-body-secondary"><b>Count:</b></span> ${params.datum.count}</div>
                            <div><span class="text-body-secondary"><b>Percent:</b></span> ${params.datum.percentage.toFixed(2)}%</div>
                        </div>
                    `;
                }
              }
        }],
    };
    
    spinner?.remove();

    const chart: agCharts.AgChartInstance<agCharts.AgPolarChartOptions> = agCharts.AgCharts.create(options);
}

const loadUsaNewVintageChart = async (): Promise<void> => {
    const chartDiv: HTMLElement = document.querySelector('#usa-new-vintage-chart')!;

    const spinner: HTMLElement | null = document.querySelector('#usa-chart-spinner');

    const url: string = `${constants.getBaseUrl()}api/get_usa_new_vintage_chart_data`;

    const chartData: chart_data_model[] | undefined = await ajax_handler.getChartData(url);

    const options: agCharts.AgPolarChartOptions = {
        container: chartDiv,
        padding:{
            top: 5,
            right: 5,
            bottom: 5,
            left: 5
        },
        title: {
            text: "U.S.A.",
          },
        subtitle: {
            text: "New/Vintage"
        },
        data: chartData,
        series: [{
            type: "pie",
            fills: fill_1,
            angleKey: "count",
            legendItemKey: "name",
            angleName: "U.S.A.",
            tooltip: {
                renderer: (params) => {
                    const fillColor = (params as any).fill ?? '#888';
                    
                    return `
                        <div style="padding: 8px;">
                            <div style="display: flex; align-items: center; margin-bottom: 3px;">
                            <span style="background:${fillColor}; width:10px; height:10px; margin-right:6px;"></span>
                            <b>${params.datum.name}</b>
                            </div>
                            <div><span class="text-body-secondary"><b>Count:</b></span> ${params.datum.count}</div>
                            <div><span class="text-body-secondary"><b>Percent:</b></span> ${params.datum.percentage.toFixed(2)}%</div>
                        </div>
                    `;
                }
              }
        }],
    };
    
    spinner?.remove();

    const chart: agCharts.AgChartInstance<agCharts.AgPolarChartOptions> = agCharts.AgCharts.create(options);
}

// PRIVATE

const convertToOther = (arr: chart_data_model[] | undefined): chart_data_model | null => {
    if (arr) {
        const reducedData = arr.reduce(
            (accumulator, current) => {
                accumulator.count += current.count;
                accumulator.percentage += current.percentage;
                return accumulator;
            },
            { name: 'Other', count: 0, percentage: 0 }
        );
    
        return new chart_data_model(
            reducedData.name,
            reducedData.count,
            reducedData.percentage
        );
    }

    return null;
}

const knife_grid_redirect = (event: agCharts.AgNodeClickEvent<"nodeClick", any>, type: string): void => {
   if (event.datum?.name === 'Other') {
        return;
    }
                        
    const filterParams = new knife_filter_model();

    if (type === 'country') {
        filterParams.country = event.datum?.name;
    }

    if (type === 'deployment_type') {
        filterParams.deployment_type = event.datum?.name;
    }

    if (type === 'lock_type') {
        filterParams.lock_type = event.datum?.name;
    }

    redirect_handler.redirectToKnifeGridPage_rel(filterParams);
}

export {
    loadCountryChart,
    loadDeploymentTypeChart,
    loadLockTypeChart,
    loadSteelTypeChart,
    loadUsaNewVintageChart
}