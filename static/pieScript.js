/*Created by Kayla L. Patterson on 07/27/20
Description: Creates the Provision and Recall 
Pie Charts, and populates them from data on the backend*/

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
