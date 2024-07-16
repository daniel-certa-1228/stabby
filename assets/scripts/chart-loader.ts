'use strict';

import {
    agCharts,
    ajax_handler,
    chart_data_model,
    constants
}  from './index';

const loadSteelTypeChart = async () => {
    const chartDiv: HTMLElement = document.querySelector('#steel-type-chart')!;

    const url: string = `${constants.getBaseUrl()}api/get_steel_type_chart_data`;

    const chartData: chart_data_model[] | undefined = await ajax_handler.getSteelTypeChart(url);

    const options: any = {
        // Container: HTML Element to hold the chart
        container: chartDiv,
        title: {
            text: "Steel Types",
          },
        width: 600,  // Set the desired width
        height: 400,  // Set the desired height
        // Data: Data to be displayed in the chart
        data: chartData,
        // Series: Defines which chart type and data to use

        series: [{
            type: "pie",
            angleKey: "count",
            legendItemKey: "name",
            angleName: "Steel Types", // Specifies the name of the angle column
            // sectorLabel: {
            //     // Use the `formatter` function to format the label
            //         formatter: ({params}: {params:  any}) => {debugger; `${Math.round(params.count)}`},
            //     },
        }],
    };
    
    // Create Chart
    const chart = agCharts.AgCharts.create(options);
}

export {
    loadSteelTypeChart
}