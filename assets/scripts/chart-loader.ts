'use strict';

import {
    agCharts,
    ajax_handler,
    chart_data_model,
    constants
}  from './index';

const loadCountryChart = async () => {
    const chartDiv: HTMLElement = document.querySelector('#country-chart')!;

    const spinner = document.querySelector('#country-chart-spinner');

    const url: string = `${constants.getBaseUrl()}api/get_country_chart_data`;

    const chartData: chart_data_model[] | undefined = await ajax_handler.getChartData(url);

    const donut_1 = chartData?.filter(x => x.count >= 4);

    const donut_2 = chartData?.filter(x => x.count < 4);

    const options: agCharts.AgChartOptions = {
        container: chartDiv,
        title: {
            text: "Country of Manufacture",
          },
        series: [
        {
            type: "donut",
            fills: ["#4D4993", "#00764E", "#FD7E6D", "#82438B", "#CE5482", "#FFB85D", "#F9F871"],
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
                content: `<b>Count:</b> ${params.datum.count}<br /><b>Percent:</b> ${params.datum.percentage}%`
                };
            }
            }
        },
        {
            type: "donut",
            fills:["#5166AF", "#444655", "#D1A617", "#7BB6B2", "#857555", "#741429", "#FF8FDB", "#853F00"],
            data: donut_2,
            title: {
            text: "Other",
            },
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
                content: `<b>Count:</b> ${params.datum.count}<br /><b>Percent:</b> ${params.datum.percentage}%`
                };
            }
            }
        },
    ]};
   
    spinner?.remove();

    const chart = agCharts.AgCharts.create(options);
}

const loadLockTypeChart = async () => {
    const chartDiv: HTMLElement = document.querySelector('#lock-type-chart')!;

    const spinner = document.querySelector('#lt-chart-spinner');

    const url: string = `${constants.getBaseUrl()}api/get_lock_type_chart_data`;

    const chartData: chart_data_model[] | undefined = await ajax_handler.getChartData(url);

    const donut_1 = chartData?.filter(x => x.count >= 3);

    const donut_2 = chartData?.filter(x => x.count < 3);

    const options: agCharts.AgChartOptions = {
        container: chartDiv,
        title: {
            text: "Lock Types",
          },
        data: chartData,
        series: [
            {
                type: "donut",
                fills: ["#4D4993", "#00764E", "#FD7E6D", "#82438B", "#CE5482", "#FFB85D", "#F9F871"],
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
                    content: `<b>Count:</b> ${params.datum.count}<br /><b>Percent:</b> ${params.datum.percentage}%`
                    };
                }
                }
            },
            {
                type: "donut",
                fills:["#5166AF", "#444655", "#D1A617", "#7BB6B2", "#857555", "#741429", "#FF8FDB", "#853F00"],
                data: donut_2,
                title: {
                text: "Other",
                },
                legendItemKey: "name",
                calloutLabelKey: "name",
                angleKey: "count",
                outerRadiusRatio: 0.4,
                innerRadiusRatio: 0.2,
                showInLegend: false,
                tooltip: {
                renderer: (params) => {
                    return {
                    title: `${params.datum.name}`,
                    content: `<b>Count:</b> ${params.datum.count}<br /><b>Percent:</b> ${params.datum.percentage}%`
                    };
                }
                }
            },
        ],
    };
    
    spinner?.remove();

    const chart = agCharts.AgCharts.create(options);
}

const loadSteelTypeChart = async () => {
    const chartDiv: HTMLElement = document.querySelector('#steel-type-chart')!;

    const spinner = document.querySelector('#st-chart-spinner');

    const url: string = `${constants.getBaseUrl()}api/get_steel_type_chart_data`;

    const chartData: chart_data_model[] | undefined = await ajax_handler.getChartData(url);

    const options: agCharts.AgChartOptions = {
        container: chartDiv,
        title: {
            text: "Steel Types",
          },
        data: chartData,
        series: [{
            type: "pie",
            fills: ["#4D4993", "#00764E", "#FD7E6D", "#82438B", "#CE5482", "#FFB85D", "#F9F871"],
            angleKey: "count",
            legendItemKey: "name",
            angleName: "Steel Types",
            tooltip: {
                renderer: (params) => {
                  return {
                    content: `<b>Count:</b> ${params.datum.count}<br /><b>Percent:</b> ${params.datum.percentage}%`
                  };
                }
              }
        }],
    };
    
    spinner?.remove();

    const chart = agCharts.AgCharts.create(options);
}

export {
    loadCountryChart,
    loadLockTypeChart,
    loadSteelTypeChart
}