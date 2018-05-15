/* 
========================================================================================
This file depends on others Javascript files.
To work with this file, the request.js must be loaded in the HTML before calling this file.
Moreover, this file works with chart.js which is a lib that allows to generate charts.
This library must also be loaded before this file.

This file is used to manage and display results of trends
========================================================================================
 */

// This function is used to make tendency requests
// and generate a plot for the results obtained
// request: It is the name of the request
// objectIdentifier: It is the HTML that will recieved the plot generated.
function tendency(request, objectIdentifier) {
    ajaxRequest({
        type: "GET",
        url: domainUrl + request + '/' + token,
        elementId: objectIdentifier
    }, generatePlot);
}

// This function is used to generate the plot for the 
// content the the ajaxRequest sent back for tendency function.
// val: It is the result of the ajaxRequest done previously
function generatePlot(val) {
    var chartData = [];
    var chartLabel = [];
    console.log("enter function");
    val.content.forEach(function (element) {
        chartData.push(element['freq']);
        if (element['latest'] != null) {
            chartLabel.push(element['type_name_en'] + " latest " + element['latest']);
        } else {
            chartLabel.push(element['type_name_en']);
        }
    });
    // Retrieves the HTML element where the plot will be generated
    var ctx = document.getElementById(val['elementId']).getContext('2d');
    ctx.height = 500;
    var myChart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: chartLabel,
            datasets: [{
                label: 'Frequency',
                data: chartData,
                backgroundColor: [
                    'rgba(255, 99, 132, 0.2)',
                    'rgba(54, 162, 235, 0.2)',
                    'rgba(255, 206, 86, 0.2)',
                    'rgba(75, 192, 192, 0.2)',
                    'rgba(153, 102, 255, 0.2)',
                    'rgba(255, 159, 64, 0.2)'
                ],
                borderColor: [
                    'rgba(255,99,132,1)',
                    'rgba(54, 162, 235, 1)',
                    'rgba(255, 206, 86, 1)',
                    'rgba(75, 192, 192, 1)',
                    'rgba(153, 102, 255, 1)',
                    'rgba(255, 159, 64, 1)'
                ],
                borderWidth: 1
            }]
        },
        options: {
            scales: {
                yAxes: [{
                    ticks: {
                        beginAtZero: true
                    }
                }],
                xAxes: [{
                    ticks: {
                        autoSkip: false
                    }
                }]
            },
            maintainAspectRatio: false,
            responsive: true
        }
    });
}