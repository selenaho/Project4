console.log("AAAAAAA");
google.charts.load('current', { 'packages': ['corechart'] });

var education = document.getElementById("education");//education dropdown
var unemployment = document.getElementById("unemployment");//unemployment dropdown
var edu_charts = document.getElementById('edu_chart');//education chart div
var job_charts = document.getElementById('job_chart');//unemployment chart div


var pick_graph = () => {
  //console.log(education.value); //gets the value of the selected option

  if (education.value == "Pie") {
    //edu_charts.style.height = "300px";//sets height of chart
    //edu_charts.style.width = "540px";//sets width of chart
    google.charts.setOnLoadCallback(draw_pie_chart(edu_charts));//draws education pie chart
  }
  if (education.value == "barGraph") {
    //edu_charts.style.height = "300px";//sets height of chart
    //edu_charts.style.width = "540px";//sets width of chart
    google.charts.setOnLoadCallback(draw_bar_chart(edu_charts));//draws education bar chart
  }
  if (unemployment.value == "Pie") {
    //job_charts.style.height = "300px";//sets height of chart
    //job_charts.style.width = "540px";//sets width of chart
    google.charts.setOnLoadCallback(draw_pie_chart(job_charts));//draws education bar chart
  }
  if (unemployment.value == "barGraph") {
    //job_charts.style.height = "300px";//sets height of chart
    //job_charts.style.width = "540px";//sets width of chart
    google.charts.setOnLoadCallback(draw_bar_chart(job_charts));//draws education bar chart
  }
}

var draw_pie_chart = (chart_type) => {

  // console.log(chart_type.id);
  if (chart_type.id == "edu_chart") {
    var options = {
      title: 'Education Rate' //title of chart
    };
  }
  if (chart_type.id == "job_chart") {
    var options = {
      title: 'Unemployment Rate' //title of chart
    };
  }

  var data = google.visualization.arrayToDataTable([
    ['Task', 'Hours per Day'],
    ['Work', 11],
    ['Eat', 2],
    ['Commute', 2],
    ['Watch TV', 2],
    ['Sleep', 7]
  ]);


  var chart = new google.visualization.PieChart(chart_type);

  chart.draw(data, options);
}

function draw_bar_chart(chart_type) {

  var data = google.visualization.arrayToDataTable([
    ['Year', 'Asia'],
    ['2012', 900],
    ['2013', 1000],
    ['2014', 1170],
    ['2015', 1250],
    ['2016', 1530]
  ]);

  if (chart_type.id == "edu_chart") {
    var options = {
      title: 'Education Rate' //title of chart
    };
  }
  if (chart_type.id == "job_chart") {
    var options = {
      title: 'Unemployment Rate' //title of chart
    };
  }

  var chart = new google.visualization.ColumnChart(chart_type);
  chart.draw(data, options);
}

console.log(education.value);
console.log(unemployment.value);
//education.addEventListener("DOMContentLoaded", pick_graph);
education.addEventListener("change", pick_graph);
unemployment.addEventListener("change", pick_graph);
