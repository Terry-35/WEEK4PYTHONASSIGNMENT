# Step 1: Open the original file and read the content
with open("myfile.txt", "r") as file:
    content = file.read()

# Step 2: Modify the content (for demonstration, we are just changing it to uppercase)
modified_content = content.upper()

# Step 3: Write the modified content to a new file
with open("modified_file.txt", "w") as new_file:
    new_file.write(modified_content)

print("File read and modified successfully!")
