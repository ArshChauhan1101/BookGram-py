# Working code
import openai
import json

YOUR_API_KEY = "API KEY"

def chat_with_bot(book_description):
    messages = [
        {
            "role": "system",
            "content": (
                "You are an artificial intelligence assistant designed to "
                "suggest book names based on a given book description."
            ),
        },
        {
            "role": "user",
            "content": f"{book_description}",
        },
    ]

    # Send a message to the bot
    response = openai.ChatCompletion.create(
        model="mistral-7b-instruct",
        messages=messages,
        api_base="https://api.perplexity.ai",
        api_key=YOUR_API_KEY,
    )

    # Extract book names from the bot's response
    book_names = response['choices'][0]['message']['content']

    # Save book names to a JSON file
    output_json = {"book_names": book_names}
    with open("book_names_output.json", "w") as json_file:
        json.dump(output_json, json_file, indent=2)

    # Print the bot's response
    print(f"Bot: {book_names}")
    print("Book names saved to 'book_names_output.json'.")

if __name__ == "__main__":
    # Ask the user for a book description
    user_input = input("Write a book description: ")

    # Have a conversation with the bot based on the book description
    chat_with_bot(user_input)


