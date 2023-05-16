

def validate_string_input(prompt):
    """Prompts the user for a string and returns it if valid.
      Handles invalid input by displaying an error message
        and re-prompting the user."""
    while True:
        data = input(prompt)
        if data:
            return data
        else:
            print("Input cannot be empty. Please try again.")