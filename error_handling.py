def read_file():
    while True:
        try:
            filename = input("Enter a filename: ")
            with open(filename, "r") as file:
                content = file.read()
                print(f"File content:\n{content}")
            break
        except FileNotFoundError:
            print(f"Error: The file '{filename}' was not found.")
        except IOError:
            print(f"Error: Unable to read the file '{filename}'.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

# Call the function to execute the file reading operation
read_file()
