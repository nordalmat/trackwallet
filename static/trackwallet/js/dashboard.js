Chart.defaults.font.family = 'Google Sans'
Chart.defaults.font.size = 16

const renderExpenseChart = (data, labels) => {
  const expensesChart = document.getElementById('expensesChart');

  new Chart(expensesChart, {
    type: 'bar',
    data: {
      labels: labels,
      datasets: [{
        label: 'Spent',
        data: data,
        borderWidth: 1,
        backgroundColor: [
          'rgba(38, 70, 83, 1)',
          'rgba(40, 114, 113, 1)',
          'rgba(42, 157, 143, 1)',
          'rgba(138, 177, 125, 1)',
          'rgba(233, 196, 106, 1)',
          'rgba(244, 162, 97, 1)',
          'rgba(238, 137, 89, 1)'
        ],
        borderColor: [
          'rgba(8, 40, 53, 1)',
          'rgba(10, 84, 83, 1)',
          'rgba(12, 127, 113, 1)',
          'rgba(108, 147, 95, 1)',
          'rgba(203, 166, 76, 1)',
          'rgba(214, 132, 67, 1)',
          'rgba(208, 107, 59, 1)'
        ],
      }]
    },
    options: {
      plugins: {
        legend: {
          display: false
        },
        tooltips: {
          enabled: false
        },
      },
      responsive: true,
      maintainAspectRatio: false,
      scales: {
        y: {
          beginAtZero: true
        }
      }
    }
  });
};

const renderIncomeChart = (data, labels) => {
  const incomeChart = document.getElementById('incomeChart');

  new Chart(incomeChart, {
    type: 'doughnut',
    data: {
      labels: labels,
      datasets: [{
        label: 'Received',
        data: data,
        borderWidth: 1,
        backgroundColor: [
          'rgba(38, 70, 83, 1)',
          'rgba(40, 114, 113, 1)',
          'rgba(42, 157, 143, 1)',
          'rgba(138, 177, 125, 1)',
          'rgba(233, 196, 106, 1)',
          'rgba(244, 162, 97, 1)',
          'rgba(238, 137, 89, 1)'
        ],
      }]
    },
    options: {
      plugins: {
        legend: {
          display: true,
          position: 'right',
        },
        tooltips: {
          enabled: true
        },
      },
      responsive: true,
      maintainAspectRatio: false,
      scales: {
        y: {
          display: false,
          beginAtZero: true,
          grid: {
            display: false
          },
        }
      }
    }
  });
};

const getExpenseChartData = () => {
    fetch('/get-expenses-data')
    .then((response) => response.json())
    .then((results) => {
        const expenseData = results.expenseData;
        const [data, labels] = [Object.values(expenseData), Object.keys(expenseData)];
        renderExpenseChart(data, labels);
    });
};

const getIncomeChartData = () => {
  fetch('/get-income-data')
  .then((response) => response.json())
  .then((results) => {
    const incomeData = results.incomeData;
    const [data, labels] = [Object.values(incomeData), Object.keys(incomeData)];
    renderIncomeChart(data, labels);
  });
};

document.addEventListener('DOMContentLoaded', () => {
    getExpenseChartData();
    getIncomeChartData();
});