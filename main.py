import requests # imported requests from after installing googleAPI

def get_books(api_key, query, max_results=20): #defining the function name getting books
    base_url = "https://www.googleapis.com/books/v1/volumes" #Base URL of the google books which will find all the books from API
    # Parameters which are used to get the data q - string which will check, key - it is the api_key which is being used to autheticate and maxResults which will give us max books we want
    params = { 
        'q': query,
        'key': api_key,
        'maxResults': max_results
    }

    response = requests.get(base_url, params=params) 
    data = response.json()

    if 'items' in data:
        return data['items']
    else:
        return None

if __name__ == "__main__":
    api_key = "API_KEY"
    query = input("Enter a book title: ")

    books = get_books(api_key, query)

    if books:
        for book in books:
            volume_info = book['volumeInfo']
            title = volume_info['title']
            authors = volume_info.get('authors', ['Unknown'])
            published_date = volume_info.get('publishedDate', 'Unknown')
            book_category = volume_info.get('categories', ['Unknown'])
            print(f"Title: {title}, Authors: {', '.join(authors)}, Published Date: {published_date}, Category: {', '.join(book_category)}")
    else:
        print("No books found.")
