document.addEventListener('DOMContentLoaded', () => {
    const href = window.location.pathname.split('/')[1]
    const dashboard = document.querySelector('.dashboard')
    const expenses = document.querySelector('.expenses')
    const income = document.querySelector('.income')
    const preferences = document.querySelector('.preferences')
    const expensesProgression = document.querySelector('.expenses-progression')
    const incomeProgression = document.querySelector('.income-progression')


    switch(href) {
        case '':
          dashboard.classList.add('active');
          break;
        case 'expenses':
          expenses.classList.add('active');
          break;
        case 'income':
          income.classList.add('active');
          break;
        case 'preferences':
          preferences.classList.add('active');
          break;
        case 'expenses-progression':
          expensesProgression.classList.add('active');
          break;
        case 'income-progression':
          incomeProgression.classList.add('active');
          break;
        default:
          break;
      }
});