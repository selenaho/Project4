// light vs dark mode
var theme = document.getElementById("theme");
var theme_text = document.getElementById("theme_text");
const mode = localStorage.getItem("mode");//get cookie with mode
document.documentElement.setAttribute('data-bs-theme', mode); //makes the html remember the mode

// button handling
var button_A = document.getElementById("a");
var button_B = document.getElementById("b");
var button_C = document.getElementById("c");
var button_D = document.getElementById("d");
var next = document.getElementById("next");

//gets education data
var edu0 = document.getElementById("edu0");
var edu1 = document.getElementById("edu1");
var edu2 = document.getElementById("edu2");
var edu3 = document.getElementById("edu3");
var edu4 = document.getElementById("edu4");
var edu5 = document.getElementById("edu5");
var edu6 = document.getElementById("edu6");
var edu7 = document.getElementById("edu7");

var edu_data = new google.visualization.DataTable();

google.charts.load('current', { 'packages': ['corechart'] });

// two charts
var education = document.getElementById("education");//education dropdown
var unemployment = document.getElementById("unemployment");//unemployment dropdown
var edu_charts = document.getElementById('edu_chart');//education chart div
var job_charts = document.getElementById('job_chart');//unemployment chart div

// get data for charts
//var edu_data = document.getElementById("edu_data");
//console.log(typeof edu_data.innerText)
//let edu_string = edu_data.innerText
//var job_data = document.getElementById("job_data");

var pick_graph = () => {
  if (education.value == "Pie") {
    google.charts.setOnLoadCallback(draw_pie_chart(edu_charts));//draws education pie chart
  }
  if (education.value == "barGraph") {
    google.charts.setOnLoadCallback(draw_bar_chart(edu_charts));//draws education bar chart
  }
  if (unemployment.value == "Pie") {
    google.charts.setOnLoadCallback(draw_pie_chart(job_charts));//draws education bar chart
  }
  if (unemployment.value == "barGraph") {
    google.charts.setOnLoadCallback(draw_bar_chart(job_charts));//draws education bar chart
  }
};

var draw_pie_chart = (chart_type) => {

  // console.log(chart_type.id);
  if (chart_type.id == "edu_chart") {
    var options = {
      title: 'Education Rate' //title of chart
    }
  }
  if (chart_type.id == "job_chart") {
    var options = {
      title: 'Unemployment Rate' //title of chart
    }
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
};

function draw_bar_chart(chart_type) {

  var data = google.visualization.arrayToDataTable(
  //   [
  //   ['Year', 'Asia'],
  //   ['2012', 900],
  //   ['2013', 1000],
  //   ['2014', 1170],
  //   ['2015', 1250],
  //   ['2016', 1530]
  // ]
  edu_data.innerText
  );

  if (chart_type.id == "edu_chart") {
    var options = {
      title: 'Education Rate' //title of chart
    };
  }
  if (chart_type.id == "job_chart") {
    var options = {
      title: 'Unemployment Rate' //title of chart
    }

  }

  var chart = new google.visualization.ColumnChart(chart_type);
  chart.draw(data, options);
};


var switch_theme = () => {
  if (document.documentElement.getAttribute('data-bs-theme') == 'dark') {
    document.documentElement.setAttribute('data-bs-theme', 'light')
    localStorage.setItem("mode", "light");//makes cookie with mode
    theme_text.innerHTML = "Light";
    button_A.className = "btn btn-outline-dark";
    button_B.className = "btn btn-outline-dark";
    button_C.className = "btn btn-outline-dark";
    button_D.className = "btn btn-outline-dark";
    next.className = "btn btn-dark m-3";
  }
  else {
    document.documentElement.setAttribute('data-bs-theme', 'dark');
    localStorage.setItem("mode", "dark");//makes cookie with mode
    theme_text.innerHTML = "Dark";
    button_A.className = "btn btn-outline-warning";
    button_B.className = "btn btn-outline-warning";
    button_C.className = "btn btn-outline-warning";
    button_D.className = "btn btn-outline-warning";
    next.className = "btn btn-warning m-3";
  }
};


var mode_label = () => {
  if (mode == "light") {
    theme_text.innerHTML = 'Light';
    button_A.className = "btn btn-outline-dark";
    button_B.className = "btn btn-outline-dark";
    button_C.className = "btn btn-outline-dark";
    button_D.className = "btn btn-outline-dark";
    next.className = "btn btn-dark m-3";
  }
  else {
    theme_text.innerHTML = 'Dark';
    theme.setAttribute("checked", "");
    button_A.className = "btn btn-outline-warning";
    button_B.className = "btn btn-outline-warning";
    button_C.className = "btn btn-outline-warning";
    button_D.className = "btn btn-outline-warning";
    next.className = "btn btn-warning m-3";
  }
};

var make_table = () =>{
  edu_data.addColumn()
}

console.log(window.location.pathname);
mode_label();
theme.addEventListener("change", switch_theme);

//console.log(education.value);
//console.log(unemployment.value);
education.addEventListener("change", pick_graph);
window.onresize = pick_graph;
unemployment.addEventListener("change", pick_graph);
