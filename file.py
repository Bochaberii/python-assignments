with open("input.txt", "r") as file:
    content = file.read()
    uppercase_content = content.upper()
   
  
    with open("output.txt", "w") as output_file:
        output_file.write(f"Original content: {content}\n")
        output_file.write(f"Uppercase content: {uppercase_content}\n")
       
        output_file.write("Trying something new")


new = input("What file do you want to open?")

try:
     with open(new, "r") as file:
         content= file.read()
         print(content)

except FileNotFoundError:
    print(f"File '{new}' not found. Please check file name and try again. ")

finally:
    print("File operation completed.")