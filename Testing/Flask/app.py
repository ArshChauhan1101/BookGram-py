from flask import Flask, render_template, request
import requests

app = Flask(__name__)

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

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        api_key = "AIzaSyBPasAv979guuK3JTztaleOTdQfrjfhsvg"
        query = request.form['query']

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

            return render_template('index.html', books=output_data)
        else:
            return render_template('index.html', message="No books found.")

    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
