
import re


# Check if the phone number is valid
def validate_phone(phone):
    pattern = r"^\d{3}-\d{3}-\d{4}$"
    return bool(re.fullmatch(pattern, phone))


# Check if the Social Security number is valid
def validate_ssn(ssn):
    pattern = r"^\d{3}-\d{2}-\d{4}$"
    return bool(re.fullmatch(pattern, ssn))


# Check if the ZIP code is valid
def validate_zip(zip_code):
    pattern = r"^\d{5}(-\d{4})?$"
    return bool(re.fullmatch(pattern, zip_code))


# Test each function using valid and invalid inputs
def run_tests():
    print("\n--- Validation Tests ---")

    print("Phone valid:", validate_phone("941-555-1234"))
    print("Phone invalid:", validate_phone("9415551234"))

    print("SSN valid:", validate_ssn("123-45-6789"))
    print("SSN invalid:", validate_ssn("123456789"))

    print("ZIP valid:", validate_zip("34286"))
    print("ZIP+4 valid:", validate_zip("34286-1234"))
    print("ZIP invalid:", validate_zip("3428"))


# Get user input and display validation results
def main():
    phone = input("Enter a phone number (XXX-XXX-XXXX): ")
    ssn = input("Enter a Social Security number (XXX-XX-XXXX): ")
    zip_code = input("Enter a ZIP code (XXXXX or XXXXX-XXXX): ")

    print("\n--- Validation Results ---")

    if validate_phone(phone):
        print("Phone number is valid.")
    else:
        print("Phone number is invalid.")

    if validate_ssn(ssn):
        print("Social Security number is valid.")
    else:
        print("Social Security number is invalid.")

    if validate_zip(zip_code):
        print("ZIP code is valid.")
    else:
        print("ZIP code is invalid.")

    run_tests()


# Start the program
if __name__ == "__main__":
    main()
