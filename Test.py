from transformers import pipeline
import json

def get_book_info(description):
    # Load the pre-trained GPT-2 model for text generation
    text_generator = pipeline(task='text-generation', model='gpt2')

    # Generate a response based on the book description
    generated_text = text_generator(description, max_length=50, num_return_sequences=1)[0]['generated_text']

    # Extract the generated book name from the response
    sentences = generated_text.split('.')
    book_name = sentences[0].strip()

    # Create a dictionary with book information
    book_info = {
        'book_name': book_name,
        'description': description,
        'generated_text': generated_text
    }

    return book_info

# Example usage
book_description = "It ends with us"
book_info = get_book_info(book_description)

# Save the book information to a JSON file
output_file_path = 'generated_book_info.json'
with open(output_file_path, 'w') as output_file:
    json.dump(book_info, output_file, indent=2)

print("Generated Book Information saved to:", output_file_path)
