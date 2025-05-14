def read_and_write_file():
    try:
        # Open the input file for reading
        with open("input.txt", "r") as input_file:
            # Read the contents of the input file
            content = input_file.read()

        # Modify the content (e.g., convert to uppercase)
        modified_content = content.upper()

        # Open the output file for writing
        with open("output.txt", "w") as output_file:
            # Write the modified content to the output file
            output_file.write(modified_content)

        print("File processing completed successfully!")
    except FileNotFoundError:
        print("Error: Input file not found.")
    except IOError:
        print("Error: Unable to read or write the file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Call the function to execute the file read and write operation
read_and_write_file()
