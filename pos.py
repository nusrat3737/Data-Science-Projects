import nltk
from nltk.tokenize import word_tokenize
import tkinter as tk
from tkinter import ttk, scrolledtext


# Download the necessary resources
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')


# Function to perform POS tagging
def pos_tag_text():
    # Get the input text
    input_text = text_input.get("1.0", tk.END).strip()

    # Tokenize the input text
    tokens = word_tokenize(input_text)

    # Perform POS tagging
    pos_tags = nltk.pos_tag(tokens)

    # Display the POS tags
    output_text = "\n".join([f"{word}: {tag}" for word, tag in pos_tags])
    text_output.delete("1.0", tk.END)
    text_output.insert(tk.END, output_text)


# Create the main application window
root = tk.Tk()
root.title("POS Tagger")

# Create a frame for the input text
input_frame = ttk.Frame(root, padding="10")
input_frame.grid(row=0, column=0, padx=10, pady=10)

# Create and place the input text widget
ttk.Label(input_frame, text="Enter Text:").grid(row=0, column=0, sticky="W")
text_input = scrolledtext.ScrolledText(input_frame, wrap=tk.WORD, width=50, height=10)
text_input.grid(row=1, column=0, padx=5, pady=5)

# Create a button to perform POS tagging
pos_tag_button = ttk.Button(input_frame, text="Tag POS", command=pos_tag_text)
pos_tag_button.grid(row=2, column=0, pady=5)

# Create a frame for the output text
output_frame = ttk.Frame(root, padding="10")
output_frame.grid(row=1, column=0, padx=10, pady=10)

# Create and place the output text widget
ttk.Label(output_frame, text="POS Tags:").grid(row=0, column=0, sticky="W")
text_output = scrolledtext.ScrolledText(output_frame, wrap=tk.WORD, width=50, height=10)
text_output.grid(row=1, column=0, padx=5, pady=5)

# Start the Tkinter event loop
root.mainloop()
