from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    api_key = "AIzaSyBPasAv979guuK3JTztaleOTdQfrjfhsvg"  # Replace with your actual API key
    query = request.form.get('query')
    max_results = 20

    # Call the function to get books using Google Books API
    books = get_books(api_key, query, max_results)

    # Check if books were found
    if books:
        # Process the data and send it to the HTML template
        book_data = []

        for book in books:
            volume_info = book['volumeInfo']
            title = volume_info['title']
            authors = volume_info.get('authors', ['Unknown'])
            published_date = volume_info.get('publishedDate', 'Unknown')
            book_category = volume_info.get('categories', ['Unknown'])

            book_data.append({
                "Title": title,
                "Authors": authors,
                "Published Date": published_date,
                "Category": book_category
            })

        return jsonify(book_data)

    else:
        return jsonify({"error": "No books found."})

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
    app.run(debug=True)
