def modify_content(content):
    """
    This python script converts text to uppercase and adds line numbers.
    """
    lines = content.split('\n')
    modified_lines = []
    
    for i, line in enumerate(lines, 1):
        # Add line number and convert to uppercase
        modified_line = f"{i}. {line.upper()}"
        modified_lines.append(modified_line)
    
    return '\n'.join(modified_lines)

def main():
    print("File Read & Write Program")
    
    # Ask user for input filename
    input_filename = input("Enter the name of the file to read: ")
    
    try:
        # Try to open and read the file
        with open(input_filename, 'r', encoding='utf-8') as file:
            content = file.read()
        
        print(f"Successfully read from '{input_filename}'")
        
        
        # Create output filename
        output_filename = input("Enter the name for the new file (or press Enter for 'modified_output.txt'): ")
        if not output_filename:
            output_filename = "modified_output.txt"
        
        # Write modified content to new file (call the earlier function)
        with open(output_filename, 'w', encoding='utf-8') as file:
            file.write(modify_content(content))
        
        print(f"Successfully wrote modified content to '{output_filename}'")
        
    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' does not exist.")
    except PermissionError:
        print(f"Error: Permission denied to read '{input_filename}'.")
    except IsADirectoryError:
        print(f"Error: '{input_filename}' is a directory, not a file.")
    except UnicodeDecodeError:
        print(f"Error: Could not decode the file '{input_filename}'. It may not be a text file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    
if __name__ == "__main__":
    main()