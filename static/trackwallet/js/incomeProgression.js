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
              fill: true,
              label: 'Received',
              backgroundColor: 'transparent',
              borderColor: 'rgb(93, 156, 89)',
              pointBorderColor: 'rgb(93, 156, 89)',
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

const getIncomeLineChartData = () => {
    fetch('/income-progression/get-monthly-income-data')
    .then((response) => response.json())
    .then((results) => {
      const incomeData = results.incomeData;
      const [data, labels] = [Object.values(incomeData), Object.keys(incomeData)];
      const userCurrency = results.userCurrency;
      renderLineChart(data, labels, userCurrency);
    });
  };
  
document.addEventListener('DOMContentLoaded', () => {
    getIncomeLineChartData();
});