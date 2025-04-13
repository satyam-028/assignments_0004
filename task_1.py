try:
    # Attempt to open the file in read mode
    with open('sample.txt', 'r') as file:
        # Read and print each line from the file
        for line in file:
            print(line.strip())  # Using strip() to remove any extra newline characters

except FileNotFoundError:
    # Handle the error if the file doesn't exist
    print("Error: The file 'sample.txt' does not exist.")