/*Created by Kayla L. Patterson on 07/27/20
Description: Creates the Provision and Recall
Pie Charts, and populates them from data on the backend*/

//Add functions to call to backend api, and get data on pressing the buttons

// Calcuate distance and usage similarity
async function calculate() {
  var resource_attr_1 = document.getElementById("resource_id_1");
  var resource_attr_2 = document.getElementById("resource_id_2");
  var rule = document.getElementById("rule");

  var data = {
    "resource_attr_1": resource_attr_1.value,
    "resource_attr_2": resource_attr_2.value,
    "rule": rule.value
  }

  var provisioningResponse = await fetch(`${window.origin}/api/provisioning`, {
    method: "POST",
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(data)
  });
}


//Precision Pie Chart
new Chart(document.getElementById("precision-chart"), {
    type: 'pie',
    data: {
      labels: ["Should of had Access", "Should Not of had Access"],
      datasets: [{
        backgroundColor: ["#3e95cd", "#8e5ea2"],
        data: [2478,5267] //mock data
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
new Chart(document.getElementById("recall-chart"), {
    type: 'pie',
    data: {
      labels: ["Users who got Access", "Users who should of had Access but did not"],
      datasets: [{
        backgroundColor: ["#e8c3b9","#c45850"],
        data: [60,360] //mock data
      }]
    },
    options: {
      title: {
        display: true,
        text: 'Recall Resource Chart'
      }
    }
});
