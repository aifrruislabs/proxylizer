(function ($) {
  'use strict';

// flot chart hospital patient total
    $(function () {
      'use strict'

      var patientTotalData3 = [
        [0, 55],
        [1, 59],
        [2, 57],
        [3, 50],
        [4, 48],
        [5, 45],
        [6, 43],
        [7, 39],
        [8, 35],
        [9, 37],
        [10, 38],
        [11, 36],
        [12, 38],
        [13, 35],
        [14, 37],
        [15, 35],
        [16, 39],
        [17, 37],
        [18, 38],
        [19, 35],
        [20, 32],
        [21, 36],
        [22, 40],
        [23, 34],
        [24, 39],
        [25, 33],
        [26, 30],
        [27, 29],
        [28, 35],
        [29, 29],
        [30, 27],
        [31, 25],
        [32, 28],
        [33, 24],
        [34, 25],
        [35, 23],
        [36, 27],
        [37, 26],
        [38, 23],
        [39, 27],
        [40, 28],
        [41, 25],
        [42, 29],
        [43, 31],
        [44, 33],
        [45, 39],
        [46, 34],
        [47, 34],
        [48, 34],
        [49, 38],
        [50, 36],
        [51, 38],
        [52, 33],
        [53, 35],
        [54, 37],
        [55, 33],
        [56, 29],
        [57, 36],
        [58, 37],
        [59, 40],
        [60, 38],
        [61, 35],
        [62, 40],
        [63, 41],
        [64, 43],
        [65, 47],
        [66, 51],
        [67, 53],
        [68, 56],
        [69, 49],
        [70, 46],
        [71, 40],
        [72, 41],
        [73, 44],
        [74, 40],
        [75, 43],
        [76, 40],
        [77, 45],
        [78, 40],
        [79, 42],
        [80, 40],
        [81, 38],
        [82, 36],
        [83, 37],
        [84, 39],
        [85, 43],
        [86, 45],
        [87, 45],
        [88, 47],
        [89, 45],
        [90, 46]
      ];

      var patientTotalData4 = [
        [0, 45],
        [1, 70],
        [2, 65],
        [3, 60],
        [4, 57],
        [5, 53],
        [6, 49],
        [7, 45],
        [8, 54],
        [9, 52],
        [10, 50],
        [11, 45],
        [12, 41],
        [13, 37],
        [14, 54],
        [15, 49],
        [16, 52],
        [17, 52],
        [18, 52],
        [19, 50],
        [20, 49],
        [21, 45],
        [22, 45],
        [23, 45],
        [24, 58],
        [25, 57],
        [26, 56],
        [27, 54],
        [28, 54],
        [29, 54],
        [30, 50],
        [31, 49],
        [32, 48],
        [33, 47],
        [34, 46],
        [35, 48],
        [36, 49],
        [37, 50],
        [38, 51],
        [39, 53],
        [40, 55],
        [41, 59],
        [42, 65],
        [43, 71],
        [44, 76],
        [45, 74],
        [46, 74],
        [47, 74],
        [48, 74],
        [49, 67],
        [50, 60],
        [51, 58],
        [52, 57],
        [53, 56],
        [54, 59],
        [55, 64],
        [56, 67],
        [57, 65],
        [58, 67],
        [59, 70],
        [60, 68],
        [61, 66],
        [62, 64],
        [63, 59],
        [64, 57],
        [65, 59],
        [66, 56],
        [67, 53],
        [68, 45],
        [69, 50],
        [70, 55],
        [71, 57],
        [72, 62],
        [73, 65],
        [74, 63],
        [75, 64],
        [76, 68],
        [77, 65],
        [78, 60],
        [79, 62],
        [80, 59],
        [81, 57],
        [82, 55],
        [83, 54],
        [84, 50],
        [85, 55],
        [86, 53],
        [87, 50],
        [88, 48],
        [89, 49],
        [90, 50]
      ];

      function bgFlotData(num, val) {
        var data = [];
        for (var i = 0; i < num; ++i) {
          data.push([i, val]);
        }
        return data;
      }

      function bgFlotData(num, val) {
        var data = [];
        for (var i = 0; i < num; ++i) {
          data.push([i, val]);
        }
        return data;
      }

      var plot = $.plot('#patientTotal', [{
        data: patientTotalData4,
        color: '#00d284',
        lines: {
          fillColor: 'rgba(94, 110, 237, 0.03)'
        }
      }, {
        data: patientTotalData3,
        color: '#5e6eed',
        lines: {
          fillColor: 'rgba(239, 241, 254, .24)'
        }
      }], {
          series: {
            shadowSize: 0,
            lines: {
              show: true,
              lineWidth: 2,
              fill: true
            }
          },
          grid: {
            borderWidth: 0,
            labelMargin: 8
          },
          yaxis: {
            show: true,
            min: 0,
            max: 90,
            ticks: true,
          },
          xaxis: {
            show: true,
            color: '#fff',
            tickColor: '#eee',
            ticks: [[0, 'Sun'], [15, 'Mon'], [30, 'Tue'], [45, 'Wed'], [60, 'Thu'], [75, 'Fri'], [90, 'Sat']],
          }
        });

    });

    if ($("#deseaseReport").length) {
      var ctx = document.getElementById('deseaseReport').getContext("2d");

      var deseaseReportData = {
        datasets: [{
          data: [10, 30, 40, 20],
          backgroundColor: [
            "#00cff4",
            "#5e6eed",
            "#ff0d59",
            "#00d284"
          ],
          hoverBackgroundColor: [
            "#00cff4",
            "#5e6eed",
            "#ff0d59",
            "#00d284"
          ],
          borderColor: [
            "#00cff4",
            "#5e6eed",
            "#ff0d59",
            "#00d284"
          ],
          legendColor: [
            "#00cff4",
            "#5e6eed",
            "#ff0d59",
            "#00d284"
          ]
        }],

        // These labels appear in the legend and in the tooltips when hovering different arcs
        labels: [
          'Pneumonia',
          'diabetes',
          'Colds',
          'Flue'
        ]
      };
      var deseaseReportOptions = {
        responsive: true,
        animation: {
          animateScale: true,
          animateRotate: true
        },
        legend: false,
        legendCallback: function (chart) {
          var text = [];
          text.push('<ul class="m-auto pl-0 w-100 d-flex justify-content-between">');
          for (var i = 0; i < deseaseReportData.datasets[0].data.length; i++) {
            text.push('<li><div><span class="legend-dots" style="background:' +
            deseaseReportData.datasets[0].legendColor[i] +
              '"></span>');
            if (deseaseReportData.labels[i]) {
              text.push(deseaseReportData.labels[i]);
            }
            text.push('</div></li>');
          }
          text.push('</ul>');
          return text.join('');
        }
      };
      var deseaseReportCanvas = $("#deseaseReport").get(0).getContext("2d");
      var deseaseReport = new Chart(deseaseReportCanvas, {
        type: 'doughnut',
        data: deseaseReportData,
        options: deseaseReportOptions
      });
      $("#deseaseReport-legend3").html(deseaseReport.generateLegend());
    }
    $('#order-listing').DataTable({
      "aLengthMenu": [
        [2,5, 10, 15, -1],
        [2,5, 10, 15, "All"]
      ],
      "oLanguage": {
        "sLengthMenu": "Sort by _MENU_",
      },
      "iDisplayLength": 10,
      "language": { 
        search: ""
      },
        "paging":   true,
        "ordering": false,
        "info":     false,
        "filter": true
    });
    $('#order-listing').each(function() {
      var datatable = $(this);
      // SEARCH - Add the placeholder for Search and Turn this into in-line form control
      var search_input = datatable.closest('.dataTables_wrapper').find('div[id$=_filter] input');
      search_input.attr('placeholder', 'Search');
      search_input.removeClass('form-control-sm');
      // LENGTH - Inline-Form control
      var length_sel = datatable.closest('.dataTables_wrapper').find('div[id$=_length] select');
      length_sel.removeClass('form-control-sm');
    });

})(jQuery);
