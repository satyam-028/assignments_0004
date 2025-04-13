task 1

try: # Attempt to open the file in read mode with open('sample.txt', 'r') as file: # Read and print each line from the file for line in file: print(line.strip()) # Using strip() to remove any extra newline characters

except FileNotFoundError: # Handle the error if the file doesn't exist print("Error: The file 'sample.txt' does not exist.")


task 2

Take user input
user_input = input("Enter some text: ")

Open the file in write mode ('w') to create it or overwrite it
with open('output.txt', 'w') as file: file.write(user_input + '\n') # Write the user input and add a newline

Append additional data to the file
additional_data = "\nThis is some additional data appended to the file." with open('output.txt', 'a') as file: file.write(additional_data)

Read and display the final content of the file
with open('output.txt', 'r') as file: content = file.read()

print("\nFinal content of the file:") print(content)

