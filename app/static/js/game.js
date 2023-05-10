console.log("AAAAAAA");
google.charts.load('current', {'packages':['corechart']});

var education = document.getElementById("education");//education dropdown
var unemployment = document.getElementById("unemployment");//unemployment dropdown
var edu_charts = document.getElementById('chart');//education chart div
var job_charts = document.getElementById('chart2');//unemployment chart div


var pick_graph = () =>{
  //console.log(education.value); //gets the value of the selected option
  
  if (education.value == "Pie"){
    edu_charts.style.height = "300px";//sets height of chart
    edu_charts.style.width = "540px";//sets width of chart
    google.charts.setOnLoadCallback(draw_pie_chart(edu_charts));//draws education pie chart
  }
  if (education.value == "barGraph"){
    edu_charts.style.height = "300px";//sets height of chart
    edu_charts.style.width = "540px";//sets width of chart
    google.charts.setOnLoadCallback(draw_bar_chart(edu_charts));//draws education bar chart
  }
  if (unemployment.value == "Pie"){
    job_charts.style.height = "300px";//sets height of chart
    job_charts.style.width = "540px";//sets width of chart
    google.charts.setOnLoadCallback(draw_pie_chart(job_charts));//draws education bar chart
  }
  if (unemployment.value == "barGraph"){
    job_charts.style.height = "300px";//sets height of chart
    job_charts.style.width = "540px";//sets width of chart
    google.charts.setOnLoadCallback(draw_bar_chart(job_charts));//draws education bar chart
  }
}

var draw_pie_chart = (chart_type) =>{
  var data = google.visualization.arrayToDataTable([
    ['Task', 'Hours per Day'],
    ['Work',     11],
    ['Eat',      2],
    ['Commute',  2],
    ['Watch TV', 2],
    ['Sleep',    7]
  ]);

  var options = {
    title: 'My Daily Activities' //title of chart
  };

  var chart = new google.visualization.PieChart(chart_type);

  chart.draw(data, options);
}

function draw_bar_chart(chart_type) {

  var data = google.visualization.arrayToDataTable([
     ['Year', 'Asia'],
     ['2012',  900],
     ['2013',  1000],
     ['2014',  1170],
     ['2015',  1250],
     ['2016',  1530]
  ]);

  var options = {title: 'Population (in millions)'}; 

  var chart = new google.visualization.ColumnChart(chart_type);
  chart.draw(data, options);
}


education.addEventListener("change", pick_graph);
unemployment.addEventListener("change", pick_graph);
//pie chart
/*
<html>
  <head>
    <script type="text/javascript" src="https://www.gstatic.com/charts/loader.js"></script>
    <script type="text/javascript">
      google.charts.load('current', {'packages':['corechart']});
      google.charts.setOnLoadCallback(drawChart);

      function drawChart() {

        var data = google.visualization.arrayToDataTable([
          ['Task', 'Hours per Day'],
          ['Work',     11],
          ['Eat',      2],
          ['Commute',  2],
          ['Watch TV', 2],
          ['Sleep',    7]
        ]);

        var options = {
          title: 'My Daily Activities'
        };

        var chart = new google.visualization.PieChart(document.getElementById('piechart'));

        chart.draw(data, options);
      }
    </script>
  </head>
  <body>
    <div id="piechart" style="width: 900px; height: 500px;"></div>
  </body>
</html>
*/


