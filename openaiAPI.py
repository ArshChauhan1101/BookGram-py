import openai
import json

openai.api_key = 'API_KEY'

def get_book_name(description):
    prompt = f"{description}. Suggest a name for a book:"
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=10,
        n=5,  # Increase the number of book names to generate
        stop=None,
        temperature=0.7,
    )
    generated_books = [choice['text'].strip() for choice in response['choices']]
    return generated_books

if __name__ == "__main__":
    book_description = input("Enter the description of the book: ")

    book_names = get_book_name(book_description)

    # Save the generated book names to a JSON file
    with open('generated_books.json', 'w') as file:
        json.dump(book_names, file)

    print(f"Book names based on the description have been saved to 'generated_books.json'.")
