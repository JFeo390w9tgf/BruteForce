# coded by -> ig : @hackie.techie
import itertools

def generate_passwords():
    # Define the characters to be used for generating passwords
    characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+-=[]{}|;:,.<>?'
    
    # Open a file to write passwords
    with open('passwords.txt', 'w') as file:
        # Generate passwords of lengths from 3 to 12
        for length in range(3, 13):
            # Generate combinations of characters of current length
            for password in itertools.product(characters, repeat=length):
                # Write the generated password to the file
                file.write(''.join(password) + '\n')

if __name__ == "__main__":
    generate_passwords()
    print("Password generation completed. Check 'passwords.txt' file.")
