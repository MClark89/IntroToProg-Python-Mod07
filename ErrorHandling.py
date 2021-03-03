# ---------------------------------------------------------------------------- #
# Title: Assignment 7
# Description: Description of error handling
# ChangeLog (Who,When,What):
# MCLARK, 02.29.2021, created script
# ---------------------------------------------------------------------------- #
# Write a user input prompt
try:
    numValue = int(input("Rate program on a scale from 1 to 10: "))
# Create Question for ValueError
except ValueError:
    print("Answer does not compute! Please enter a value from 1-10.")
except Exception as error:
    print("UNEXPECTED ERROR!")
    print(error)
# Write an else-try statement
else:
    try:
        # Test to see if the number is outside the given range
        if numValue < 1 or numValue > 10:
            raise Exception
    except Exception:
            (print("That is outside the given range."))
    # If no error occured
    else:
        print("Your Value: ", numValue)
finally:
    print("Thank you, Goodbye!")