// charts
var education = document.getElementById("education");//education dropdown
var unemployment = document.getElementById("unemployment");//unemployment dropdown
var edu_charts = document.getElementById('edu_chart');//education chart div
var job_charts = document.getElementById('job_chart');//unemployment chart div
var client_color = document.getElementById("barGraphColor");

// chart making functions--------------------------------------------------------------
google.charts.load('current', { 'packages': ['corechart'] });

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
    var edu_data = new google.visualization.DataTable();
    edu_data.addColumn('string', 'Category');
    edu_data.addColumn('number', 'People');
    edu_data.addRows(4);
    edu_data.setCell(0, 0, 'Percentage of adults with less than a high school diploma, 2017-21');
    edu_data.setCell(1, 0, 'Percentage of adults with a high school diploma only, 2017-21');
    edu_data.setCell(2, 0, 'Percentage of adults completing some college or associate\'s degree, 2017-21');
    edu_data.setCell(3, 0, 'Percentage of adults with a bachelor\'s degree or higher, 2017-21');

    for (let i = 4; i < 8; i++) {
      edu_data.setCell(i - 4, 1, edulist[i]);
    }

    var options = {
      title: 'Education Rate', //title of chart
      height: 300,
      is3D: true
    }

    var chart = new google.visualization.PieChart(chart_type);
    chart.draw(edu_data, options);
  };

  if (chart_type.id == "job_chart") {
    var job_data = new google.visualization.DataTable();
    job_data.addColumn('string', 'Category');
    job_data.addColumn('number', 'People');
    job_data.addRows(2);
    job_data.setCell(0, 0, "Employed population in 2020");
    job_data.setCell(0, 1, joblist[6]);
    job_data.setCell(1, 0, "Unemployed population in 2020");
    job_data.setCell(1, 1, joblist[7]);

    var options = {
      title: 'Unemployment Rate', //title of chart
      height: 300,
      is3D: true
    }

    var chart = new google.visualization.PieChart(chart_type);
    chart.draw(job_data, options);
  }

};

function draw_bar_chart(chart_type) {

  var color_from_client = client_color.value;

  if (chart_type.id == "edu_chart") {
    var edu_data = new google.visualization.DataTable();
    edu_data.addColumn('string', 'Category');
    edu_data.addColumn('number', 'People');
    edu_data.addRows(4);
    edu_data.setCell(0, 0, 'Less than a high school diploma, 2017-21');
    edu_data.setCell(1, 0, 'High school diploma only, 2017-21');
    edu_data.setCell(2, 0, 'Some college or associate\'s degree, 2017-21');
    edu_data.setCell(3, 0, 'Bachelor\'s degree or higher, 2017-21');

    for (let i = 0; i < 4; i++) {
      edu_data.setCell(i, 1, edulist[i]);//edulist is an array of edu0 to 7
    }

    var options = {
      title: 'Education Rate', //title of chart
      height: 300,
      colors: [color_from_client]
    };

    var chart = new google.visualization.ColumnChart(chart_type);
    chart.draw(edu_data, options);
  };

  if (chart_type.id == "job_chart") {
    var job_data = new google.visualization.DataTable();
    job_data.addColumn('string', 'Year');
    job_data.addColumn('number', 'Unemployment rate');
    job_data.addRows(6);
    job_data.setCell(0, 0, "2000");
    job_data.setCell(1, 0, "2004");
    job_data.setCell(2, 0, "2008");
    job_data.setCell(3, 0, "2012");
    job_data.setCell(4, 0, "2016");
    job_data.setCell(5, 0, "2020");

    for (let i = 0; i < 6; i++) {
      job_data.setCell(i, 1, joblist[i]);
    }

    var options = {
      title: 'Unemployment Rate', //title of chart
      height: 300,
      colors: [color_from_client]
    }

    var chart = new google.visualization.ColumnChart(chart_type);
    chart.draw(job_data, options);
  }
};

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

// theme handling functions--------------------------------------------------------------
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

/*
var request = new XMLHttpRequest();
request.open('POST', '/', true);
request.send(winnerIndex);
*/

var win_text = () =>{
  if (won == "y"){
    document.getElementById("message").style.color = "yellow";
  }
}

//console.log(window.location.pathname);
win_text();
mode_label();
theme.addEventListener("change", switch_theme);

window.onresize = pick_graph;
client_color.addEventListener("change", pick_graph);
education.addEventListener("change", pick_graph);
unemployment.addEventListener("change", pick_graph);

