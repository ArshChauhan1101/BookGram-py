import requests
import json

def get_books(api_key, query, max_results=20):
    base_url = "https://www.googleapis.com/books/v1/volumes"
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
    query = input("Enter a book title or Author Name: ")

    books = get_books(api_key, query)

    if books:
        output_data = []  # List to store book data

        for book in books:
            volume_info = book['volumeInfo']
            title = volume_info['title']
            authors = volume_info.get('authors', ['Unknown'])
            published_date = volume_info.get('publishedDate', 'Unknown')
            book_category = volume_info.get('categories', ['Unknown'])

            # Create a dictionary for each book
            book_data = {
                "Title": title,
                "Authors": authors,
                "Published Date": published_date,
                "Category": book_category
            }

            output_data.append(book_data)

        # Save the data to a JSON file
        output_file_path = "books_output.json"
        with open(output_file_path, 'w') as json_file:
            json.dump(output_data, json_file, indent=2)

        print(f"Books data has been saved to {output_file_path}")
    else:
        print("No books found.")
