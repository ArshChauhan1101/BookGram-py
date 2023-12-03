function searchBooks() {
    var query = document.getElementById('searchInput').value;

    // Make an API request to Google Books API
    var apiUrl = `https://www.googleapis.com/books/v1/volumes?q=${query}`;
    fetch(apiUrl)
        .then(response => response.json())
        .then(data => displayBooks(data.items))
        .catch(error => console.error('Error fetching books:', error));
}

function displayBooks(books) {
    var bookList = document.getElementById('bookList');
    bookList.innerHTML = '';

    if (books && books.length > 0) {
        books.forEach(function(book) {
            var volumeInfo = book.volumeInfo;
            var bookHtml = `<div class="card">
                                <div class="card-body">
                                    <h5 class="card-title">${volumeInfo.title}</h5>
                                    <p class="card-text">Authors: ${volumeInfo.authors ? volumeInfo.authors.join(', ') : 'Unknown'}</p>
                                </div>
                            </div>`;
            bookList.innerHTML += bookHtml;
        });
    } else {
        bookList.innerHTML = '<p>No books found.</p>';
    }
}

document.addEventListener('DOMContentLoaded', function () {
    const navbarTogglerBtn = document.getElementById('navbarTogglerBtn');
    const navbarCollapse = document.getElementById('navbarCollapse');

    navbarTogglerBtn.addEventListener('click', function () {
        navbarCollapse.classList.toggle('show-navbar-collapse');
    });
});
