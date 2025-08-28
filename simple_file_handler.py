def simple_file_handler():
    """Simple file read/write with basic error handling"""
    
    try:
        # Get input filename
        input_file = input("Enter input filename: ")
        
        # Read file
        with open(input_file, 'r') as file:
            content = file.read()
        
        # Modify content (simple example)
        modified_content = content.upper()
        
        # Get output filename
        output_file = input("Enter output filename: ")
        
        # Write to new file
        with open(output_file, 'w') as file:
            file.write(modified_content)
            
        print(f"Success! Modified content written to {output_file}")
        
    except FileNotFoundError:
        print("Error: File not found!")
    except PermissionError:
        print("Error: Permission denied!")
    except Exception as e:
        print(f"An error occurred: {e}")
