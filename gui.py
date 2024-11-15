import tkinter as tk
import openai

# Set your OpenAI API key
openai.api_key = "API key Here"  # Replace with your actual API key

# Function to handle the submission of the question and request an answer from GPT
def submit_question():
    question = question_entry.get().strip()
    if question:
        try:
            # Request to OpenAI API
            response = openai.chat.completions.create(
                model="gpt-4",  # Use GPT-4 model
                messages=[{"role": "user", "content": question}],
                max_tokens=150
            )
            # Extract the answer
            answer = response.choices[0].message.content.strip()
            print(f"Question: {question}")
            print(f"Answer: {answer}\n")
        except Exception as e:
            print(f"Error: {e}")
    else:
        print("Please enter a question.")

# Set up the tkinter window
root = tk.Tk()
root.title("ChatGPT Question Interface")

# Label above the text box
label = tk.Label(root, text="Ask a Question Here", font=("Arial", 14))
label.pack(pady=10)

# Text box for user input
question_entry = tk.Entry(root, width=50, font=("Arial", 12))
question_entry.pack(pady=10)

# Submit button
submit_button = tk.Button(root, text="Submit", font=("Arial", 12), command=submit_question)
submit_button.pack(pady=10)

# Start the tkinter event loop
root.mainloop()
