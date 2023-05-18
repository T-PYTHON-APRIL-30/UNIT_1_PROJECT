import getpass

def validate_input(prompt):
    """Prompts the user and returns it if valid.
    Handles invalid input by displaying an error message
        and re-prompting the user."""
    while True:
        data = input(prompt)
        if data:
            return data
        else:
            print("Input cannot be empty. Please try again.")

def validate_password1(message):
  """
  Prompts user input without showing in the screen and validates that it is not empty.
  and re-prompting the user.
  """

  while True:
    user_input = getpass.getpass(message)
    is_valid_password = lambda message: (
    len(message) >= 8 and
    any(c.isupper() for c in message) and
    any(c.islower() for c in message) and
    any(c.isdigit() for c in message)
)
    if is_valid_password:
      return user_input
    else:
      print("Input cannot be empty. Please try again.")

def validate_password(message):
  """
  Prompts user input without showing in the screen and validates that it is not empty.
  and re-prompting the user.
  """
  while True:
    user_input = getpass.getpass(message)
    if user_input:
      return user_input
    else:
      print("Input cannot be empty. Please try again.")
