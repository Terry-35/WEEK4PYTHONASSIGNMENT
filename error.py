filename = input("Please enter the filename: ")

try:
    # Step 1: Open the file in read mode
    with open(filename, "r") as file:
        content = file.read()
    print("File content successfully read:")
    print(content)

except FileNotFoundError:
    # Step 2: Handle the case where the file does not exist
    print(f"Error: The file '{filename}' was not found. Please check the filename.")

except IOError:
    # Step 3: Handle general input/output errors (e.g., file can't be read)
    print(f"Error: Could not read the file '{filename}'. Please check if it is accessible.")

finally:
    print("File operation complete.")
