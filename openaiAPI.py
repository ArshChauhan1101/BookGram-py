import openai

openai.api_key = 'API KEY'

def get_book_names(description):
    prompt = f"Given the description '{description}', generate names of 20 books:"
    response = openai.Completion.create(
        engine="text-davinci-003",  # Use the appropriate engine
        prompt=prompt,
        max_tokens=20,
        n=1,
        stop=None,
        temperature=0.7,
    )
    generated_books = response['choices'][0]['text'].split("\n")[:-1]
    return generated_books

if __name__ == "__main__":
    book_description = input("Enter the description of the book: ")

    book_names = get_book_names(book_description)

    print(f"Book names based on the description:\n")
    for i, book in enumerate(book_names, start=1):
        print(f"{i}. {book}")

    print("\nEnd of book names.")
