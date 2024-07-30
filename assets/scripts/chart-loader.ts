'use strict';

import {
    agCharts,
    ajax_handler,
    chart_data_model,
    constants
}  from './index';

const fill_1: string[] = ["#4D4993", "#00764E", "#FD7E6D", "#82438B", "#CE5482", "#FFB85D", "#C4C454", "#006676", "#E6A902"];
const fill_2: string[] = ["#5166AF", "#444655", "#D1A617", "#7BB6B2", "#857555", "#741429", "#FF8FDB", "#853F00", "#5DE602"];

const loadCountryChart = async (): Promise<void> => {
    const chartDiv: HTMLElement = document.querySelector('#country-chart')!;

    const spinner: HTMLElement | null = document.querySelector('#country-chart-spinner');

    const url: string = `${constants.getBaseUrl()}api/get_country_chart_data`;

    const chartData: chart_data_model[] | undefined = await ajax_handler.getChartData(url);

    const donut_1: chart_data_model[] | undefined = chartData?.filter(x => x.count >= 6);
    
    //Aggregate "OTHER"
    const donut_2_raw: chart_data_model[] | undefined = chartData?.filter(x => x.count < 6 && x.count > 2);
    const other_raw: chart_data_model[] | undefined = chartData?.filter(x => x.count <= 2);
    const other: chart_data_model | null = convertToOther(other_raw);

    let donut_2: chart_data_model[];

    if (other) {
        donut_2 = [...(donut_2_raw || []), other];
    } else {
        donut_2 = [...(donut_2_raw || [])];
    }

    const options: agCharts.AgChartOptions = {
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
                    return {
                    content: `<b>Count:</b> ${params.datum.count}<br /><b>Percent:</b> ${params.datum.percentage.toFixed(2)}%`
                    };
                }
            }
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
                    return {
                    title: `${params.datum.name}`,
                    content: `<b>Count:</b> ${params.datum.count}<br /><b>Percent:</b> ${params.datum.percentage.toFixed(2)}%`
                    };
                }
            }
        },
    ]};
   
    spinner?.remove();

    const chart: agCharts.AgChartInstance<agCharts.AgPolarChartOptions> = agCharts.AgCharts.create(options);
}

const loadLockTypeChart = async (): Promise<void> => {
    const chartDiv: HTMLElement = document.querySelector('#lock-type-chart')!;

    const spinner: HTMLElement | null = document.querySelector('#lt-chart-spinner');

    const url: string = `${constants.getBaseUrl()}api/get_lock_type_chart_data`;

    const chartData: chart_data_model[] | undefined = await ajax_handler.getChartData(url);

    const donut_1: chart_data_model[] | undefined = chartData?.filter(x => x.count >= 6);

    const donut_2: chart_data_model[] | undefined = chartData?.filter(x => x.count < 6);

    const options: agCharts.AgChartOptions = {
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
                        return {
                        content: `<b>Count:</b> ${params.datum.count}<br /><b>Percent:</b> ${params.datum.percentage.toFixed(2)}%`
                        };
                    }
                }
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
                        return {
                        title: `${params.datum.name}`,
                        content: `<b>Count:</b> ${params.datum.count}<br /><b>Percent:</b> ${params.datum.percentage.toFixed(2)}%`
                        };
                    }
                }
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

    const options: agCharts.AgChartOptions = {
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
                  return {
                    content: `<b>Count:</b> ${params.datum.count}<br /><b>Percent:</b> ${params.datum.percentage.toFixed(2)}%`
                  };
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

export {
    loadCountryChart,
    loadLockTypeChart,
    loadSteelTypeChart
}