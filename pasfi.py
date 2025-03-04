import re
import sys
import argparse

def extract_custom_strings(input_file, length, num_caps, num_digits, num_specials):
    try:
        with open(input_file, 'r', encoding='utf-8', errors='ignore') as file:
            lines = file.readlines()

        valid_strings = []
        special_chars = r"!@#$%^&*()_+[]{}|;:',.<>?/`~"

        # Process each line
        for line in lines:
            # Find all words of the specified length
            words = re.findall(rf'\b[a-zA-Z0-9{re.escape(special_chars)}]{{{length}}}\b', line)
            for word in words:
                # Count capital letters, digits, and special characters
                num_upper = sum(1 for c in word if c.isupper())
                num_digit = sum(1 for c in word if c.isdigit())
                num_special = sum(1 for c in word if c in special_chars)

                # Check if the word matches the criteria
                if num_upper == num_caps and num_digit == num_digits and num_special == num_specials:
                    valid_strings.append(word)

        # Print valid strings
        for string in valid_strings:
            print(string)

    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found!")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Extract strings from a file based on custom criteria.")
    parser.add_argument("input_file", help="Path to the input file")
    parser.add_argument("--length", type=int, required=True, help="Length of the string")
    parser.add_argument("--caps", type=int, required=True, help="Number of capital letters")
    parser.add_argument("--digits", type=int, required=True, help="Number of digits")
    parser.add_argument("--specials", type=int, required=True, help="Number of special characters")

    # Parse arguments
    args = parser.parse_args()

    # Extract and print valid strings
    extract_custom_strings(args.input_file, args.length, args.caps, args.digits, args.specials)
