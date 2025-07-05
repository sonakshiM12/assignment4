# Step 1: Write user input to output.txt
text1 = input("Enter text to write to the file: ")
with open("output.txt", "w") as file:
    file.write(text1 + "\n")
print("Data successfully written to output.txt.\n")

# Step 2: Append additional user input to the same file
text2 = input("Enter additional text to append: ")
with open("output.txt", "a") as file:
    file.write(text2 + "\n")
print("Data successfully appended.\n")

# Step 3: Read and display the final content of the file
print("Final content of output.txt:")
with open("output.txt", "r") as file:
    print(file.read())
