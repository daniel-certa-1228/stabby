'use strict';

import {
    agCharts,
    ajax_handler,
    chart_data_model,
    constants
}  from './index';

const loadSteelTypeChart = async () => {
    const chartDiv: HTMLElement = document.querySelector('#steel-type-chart')!;

    const st_spinner = document.querySelector('#st-chart-spinner');

    const url: string = `${constants.getBaseUrl()}api/get_steel_type_chart_data`;

    const chartData: chart_data_model[] | undefined = await ajax_handler.getSteelTypeChart(url);

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
    
    st_spinner?.remove();

    const chart = agCharts.AgCharts.create(options);
}

export {
    loadSteelTypeChart
}