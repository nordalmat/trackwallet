document.addEventListener('DOMContentLoaded', () => {
    const searchField = document.querySelector('#searchField');
    searchField.value = '';

    const baseTable = document.querySelector('.base-table');
    baseTable.style.display = 'block';
    const futureTable = document.querySelector('.future-table');
    futureTable.style.display = 'block';
    const label = document.querySelector('.planned-label');
    label.style.display = 'block';

    const searchTable = document.querySelector('.search-table');
    searchTable.style.display = 'none';
    const searchTableBody = document.querySelector('.search-table-body');
    const noResults = document.querySelector('.no-results');
    $(noResults).removeClass('d-flex').addClass('d-none');
    noResults.style.display = 'none';
    const days7 = document.getElementById('7days');
    const days30 = document.getElementById('30days');

    let debounceTimerId;

    searchField.addEventListener('keyup', () => {
        const searchValue = searchField.value;
        days7.classList.remove('active')
        days30.classList.remove('active')
        if(debounceTimerId) {
            clearTimeout(debounceTimerId);
        };
        debounceTimerId = setTimeout(() => {
            if(searchValue.trim().length > 0) {
                $(noResults).removeClass('d-flex').addClass('d-none');
                noResults.style.display = 'none';
                searchTableBody.innerHTML = '';
                fetch('/search/search-expenses/', {
                    body: JSON.stringify({ searchValue: searchValue}),
                    method: "POST"
                })
                .then((result) => result.json())
                .then((data) => {
                    baseTable.style.display = 'none';
                    futureTable.style.display = 'none';
                    label.style.display = 'none';
                    searchTable.style.display = 'block';
                    if(data.length === 0) {
                        searchTable.style.display = 'none';
                        noResults.style.display = 'block';
                        $(noResults).removeClass('d-none').addClass('d-flex');
                    } else {
                        Promise.all(
                            data.map(element => 
                                fetch('/search/search-category/', {
                                    body: JSON.stringify({category_id: element.category_id}),
                                    method: 'POST'
                                })
                                .then((result) => result.json())
                            )
                        )
                        .then((categories) => {
                            data.forEach((element, index) => {
                                var category = JSON.parse(categories[index]);
                                var categoryName = category.name;
                                var expenseDate = new Date(element.expense_date);
                                var formattedDate = expenseDate.toLocaleDateString('en-US', {
                                    month: 'long',
                                    day: 'numeric',
                                    year: 'numeric'
                                });
                                searchTableBody.innerHTML +=
                                `<tr>
                                    <td>${formattedDate}</td>
                                    <td>${element.amount}</td>
                                    <td>${categoryName}</td>
                                    <td>${element.description}</td>
                                    <td><a href="edit-expense/${element.id}" type="button" class="btn btn-outline-dark btn-sm">Edit</button></td>
                                </tr>`;
                            });
                        });
                    };
                });
            } else {
                label.style.display = 'block';
                baseTable.style.display = 'block';
                futureTable.style.display = 'block';
                searchTable.style.display = 'none';
                $(noResults).removeClass('d-flex').addClass('d-none');
                noResults.style.display = 'none';
            };    
        }, 250);
    });
});