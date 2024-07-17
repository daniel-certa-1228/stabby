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
        width: 400,
        height: 400,
        series: [
        {
            type: "donut",
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
        width: 350,
        height: 350,
        data: chartData,
        series: [{
            type: "pie",
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
    loadSteelTypeChart
}