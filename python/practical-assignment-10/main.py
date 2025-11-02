# 10. RE Module 
# Accept following information from user. 
# 1. Aadhar Number 
# 2. PAN 
# 3. GST 
# 4. Mobile Number(Indian only) 
# 5. Email ID 
# Validate the values as per their standard formats. Display errors otherwise. 
# Display all valid values.  suing separate files

import re
from validation import Validator

def get_user_input():
    """
    Get input from user for all required fields
    """
    print("=== User Information Validation System ===")
    print("Please enter the following information:\n")
    
    data = {}
    
    data['adhar'] = input("1. Aadhar Number (12 digits): ").strip()
    data['pan'] = input("2. PAN Number (e.g., ABCDE1234F): ").strip().upper()
    data['gst'] = input("3. GST Number (15 characters): ").strip().upper()
    data['mobile'] = input("4. Mobile Number (10 digits): ").strip()
    data['email'] = input("5. Email ID: ").strip()
    
    return data

def validate_all_data(data):
    """
    Validate all user data and return results
    """
    validation_results = {}
    
    # Validate each field
    validation_results['adhar'] = Validator.validate_adhar(data['adhar'])
    validation_results['pan'] = Validator.validate_pan(data['pan'])
    validation_results['gst'] = Validator.validate_gst(data['gst'])
    validation_results['mobile'] = Validator.validate_mobile(data['mobile'])
    validation_results['email'] = Validator.validate_email(data['email'])
    
    return validation_results

def display_results(data, validation_results):
    """
    Display validation results and valid values
    """
    print("\n" + "="*50)
    print("VALIDATION RESULTS")
    print("="*50)
    
    valid_count = 0
    valid_data = {}
    
    fields = [
        ('Aadhar Number', 'adhar'),
        ('PAN Number', 'pan'),
        ('GST Number', 'gst'),
        ('Mobile Number', 'mobile'),
        ('Email ID', 'email')
    ]
    
    for field_name, field_key in fields:
        is_valid, message = validation_results[field_key]
        status = "✓ VALID" if is_valid else "✗ INVALID"
        print(f"\n{field_name}: {status}")
        print(f"  Input: {data[field_key]}")
        print(f"  Message: {message}")
        
        if is_valid:
            valid_count += 1
            valid_data[field_name] = data[field_key]
    
    # Display summary
    print("\n" + "="*50)
    print("SUMMARY")
    print("="*50)
    print(f"Total Fields: 5")
    print(f"Valid Fields: {valid_count}")
    print(f"Invalid Fields: {5 - valid_count}")
    
    if valid_count > 0:
        print("\nVALID VALUES:")
        print("-" * 30)
        for field_name, value in valid_data.items():
            print(f"{field_name}: {value}")
    else:
        print("\nNo valid values to display.")

def main():
    """
    Main function to run the validation system
    """
    try:
        # Get user input
        user_data = get_user_input()
        
        # Validate all data
        results = validate_all_data(user_data)
        
        # Display results
        display_results(user_data, results)
        
    except KeyboardInterrupt:
        print("\n\nProgram interrupted by user. Exiting...")
    except Exception as e:
        print(f"\nAn error occurred: {str(e)}")

if __name__ == "__main__":
    main()
