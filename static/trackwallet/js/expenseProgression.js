Chart.defaults.font.family = 'Google Sans'
Chart.defaults.font.size = 16

const renderLineChart = (data, labels, userCurrency) => {
    const lineChart = document.getElementById('lineChart');
  
    new Chart(lineChart, {
        type: 'line',
        data: {
            labels: labels,
            datasets: [{
              data: data,
              label: 'Spent',
              backgroundColor: 'transparent',
              borderColor: 'rgb(223, 46, 56)',
              pointBorderColor: 'rgb(223, 46, 56)',
              pointBorderWidth: 4,
              tension: 0.5,
              spanGaps: false
            }],
        },
        options: {
          responsive: true,
          maintainAspectRatio: false,
          plugins: {
            legend: {
              display: false
            },
            tooltip: {
              callbacks: {
                  label: (item) =>
                      `${item.dataset.label}: ${item.formattedValue} ${userCurrency}`,
              }
            }
          },
          scales: {
            x: {
              grid: {
                display: false
              }
            },
            y: {
              border: {
                dash: [10]
              },
              ticks: {
                callback: (value) => `${value} ${userCurrency}`,
              }
            }
          }
        },
    });
};

const getExpenseLineChartData = () => {
    fetch('/expenses-progression/get-monthly-expense-data')
    .then((response) => response.json())
    .then((results) => {
      const expenseData = results.expenseData;
      const [data, labels] = [Object.values(expenseData), Object.keys(expenseData)];
      const userCurrency = results.userCurrency;
      renderLineChart(data, labels, userCurrency);
    });
  };
  
document.addEventListener('DOMContentLoaded', () => {
    getExpenseLineChartData();
});