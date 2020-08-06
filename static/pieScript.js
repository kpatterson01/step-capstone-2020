/*Created by Kayla L. Patterson on 07/27/20
Description: Creates the Provision and Recall
Pie Charts, and populates them from data on the backend*/

var precisionCanvas = document.getElementById("precision-chart");
var recallCanvas = document.getElementById("recall-chart");

//Precision Pie Chart
var precisionChart = new Chart(precisionCanvas, {
    type: 'pie',
    data: {
      labels: ["Should of had Access", "Should Not of had Access"],
      datasets: [{
        backgroundColor: ["#3e95cd", "#8e5ea2"],
        data: [100,0] //mock data
      }]
    },
    options: {
      title: {
        display: true,
        text: 'Precision Resource Chart'
      }
    }
});

//Recall Pie Chart
var recallChart = new Chart(recallCanvas, {
    type: 'pie',
    data: {
      labels: ["Users who got Access", "Users who should of had Access but did not"],
      datasets: [{
        backgroundColor: ["#e8c3b9","#c45850"],
        data: [100,0] //mock data
      }]
    },
    options: {
      title: {
        display: true,
        text: 'Recall Resource Chart'
      }
    }
});

// Calcuate provision metrics
async function calculate() {
  var resource_attr_1 = document.getElementById("resource_id_1");
  var resource_attr_2 = document.getElementById("resource_id_2");
  var rule = document.getElementById("rule");

  var data = {
    "resource_attr_1": resource_attr_1.value,
    "resource_attr_2": resource_attr_2.value,
    "rule": rule.value
  }
  console.log(data);

  //Make requests to backend
  var provisionResponse = await fetch(`${window.origin}/api/provisioning`, {
    method: "POST",
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(data)
  });

  provisionData = await provisionResponse.json();
  console.log(provisionData);

  // Display response on charts and sidebar
  if(provisionResponse.status == 200) {
    document.getElementById("precision").innerHTML = 'Precision: '+ provisionData.data[0];
    document.getElementById("recall").innerHTML = 'Recall: '+ provisionData.data[1];

    precisionChart.data.datasets[0].data = [provisionData.data[0], 1 - provisionData.data[0]];
    recallChart.data.datasets[0].data = [provisionData.data[1], 1 - provisionData.data[1]];
    precisionChart.update();
    recallChart.update();
  } else {
    document.getElementById("precision").innerHTML = 'Invalid rule or resource entered.';
    document.getElementById("recall").innerHTML = '';
  }
}
