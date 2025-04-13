# Take user input
user_input = input("Enter some text: ")

# Open the file in write mode ('w') to create it or overwrite it
with open('output.txt', 'w') as file:
    file.write(user_input + '\n')  # Write the user input and add a newline

# Append additional data to the file
additional_data = "\nThis is some additional data appended to the file."
with open('output.txt', 'a') as file:
    file.write(additional_data)

# Read and display the final content of the file
with open('output.txt', 'r') as file:
    content = file.read()

print("\nFinal content of the file:")
print(content)