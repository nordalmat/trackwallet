document.addEventListener('DOMContentLoaded', () => {
    const days7 = document.getElementById('7days');
    const days30 = document.getElementById('30days');
    days7.classList.remove('active');
    days30.classList.remove('active');

    const searchField = document.querySelector('#searchField');
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

    days7.addEventListener('click', () => {
        searchTableBody.innerHTML = '';
        searchField.value = '';
        if(days7.classList.contains('active')) {
            days7.classList.remove('active');
            label.style.display = 'block';
            baseTable.style.display = 'block';
            futureTable.style.display = 'block';
            searchTable.style.display = 'none';
            $(noResults).removeClass('d-flex').addClass('d-none');
            noResults.style.display = 'none';
        } else {
            days7.classList.add('active');
            days30.classList.remove('active');
            fetch('/toolbar/income-days/', {
                body: JSON.stringify({days: 7}),
                method: 'POST'
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
                            fetch('/search/search-source/', {
                                body: JSON.stringify({source_id: element.source_id}),
                                method: 'POST'
                            })
                            .then((result) => result.json())
                        )
                    )
                    .then((sources) => {
                        data.forEach((element, index) => {
                            var source = JSON.parse(sources[index]);
                            var sourceName = source.name;
                            var incomeDate = new Date(element.income_date);
                            var formattedDate = incomeDate.toLocaleDateString('en-US', {
                                month: 'long',
                                day: 'numeric',
                                year: 'numeric'
                            });
                            searchTableBody.innerHTML +=
                            `<tr>
                                <td>${formattedDate}</td>
                                <td>${element.amount}</td>
                                <td>${sourceName}</td>
                                <td>${element.description}</td>
                                <td><a href="edit-income/${element.id}" type="button" class="btn btn-outline-dark btn-sm">Edit</button></td>
                            </tr>`;
                        });
                    });
                };
            });
        };
    });
    days30.addEventListener('click', () => {
        searchTableBody.innerHTML = '';
        searchField.value = '';
        if(days30.classList.contains('active')) {
            days30.classList.remove('active');
            days7.classList.remove('active');
            label.style.display = 'block';
            baseTable.style.display = 'block';
            futureTable.style.display = 'block';
            searchTable.style.display = 'none';
            $(noResults).removeClass('d-flex').addClass('d-none');
            noResults.style.display = 'none';
        } else {
            days30.classList.add('active');
            days7.classList.remove('active');
            fetch('/toolbar/income-days/', {
                body: JSON.stringify({days: 30}),
                method: 'POST'
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
                            fetch('/search/search-source/', {
                                body: JSON.stringify({source_id: element.source_id}),
                                method: 'POST'
                            })
                            .then((result) => result.json())
                        )
                    )
                    .then((sources) => {
                        data.forEach((element, index) => {
                            var source = JSON.parse(sources[index]);
                            var sourceName = source.name;
                            var incomeDate = new Date(element.income_date);
                            var formattedDate = incomeDate.toLocaleDateString('en-US', {
                                month: 'long',
                                day: 'numeric',
                                year: 'numeric'
                            });
                            searchTableBody.innerHTML +=
                            `<tr>
                                <td>${formattedDate}</td>
                                <td>${element.amount}</td>
                                <td>${sourceName}</td>
                                <td>${element.description}</td>
                                <td><a href="edit-income/${element.id}" type="button" class="btn btn-outline-dark btn-sm">Edit</button></td>
                            </tr>`;
                        });
                    });
                };
            });
        };
    });
});