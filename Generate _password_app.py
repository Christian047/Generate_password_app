    
import random
import string

# Generate the whole set of options to choose from
characters = list(string.ascii_letters + string.digits + " @#$%^&*()")

# Call the function
def generate_password():
    password_length = int(input('How long do you want the password to be?: '))
    
    # Use random.sample to select unique characters
    password = random.sample(characters, password_length)
    
    # Convert the list to a string
    password = ''.join(password)
    
    print(password)

# Example usage
generate_password()
    

while True:
    print('')
    option = input('Do you want to generate password, Y or N: ')
    if option.upper() =='Y':
       generate_password()
    
    elif option.upper() == 'N':
        quit()
        
    else:
        print('Invalid Input')