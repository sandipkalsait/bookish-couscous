import re

class Validator:
    @staticmethod
    def validate_adhar(adhar):
        """
        Validate Aadhar Number (12-digit number, no spaces or special characters)
        """
        pattern = r'^\d{12}$'
        if re.match(pattern, adhar):
            return True, "Valid Aadhar Number"
        return False, "Invalid Aadhar Number. Must be 12 digits without spaces or special characters"
    
    @staticmethod
    def validate_pan(pan):
        """
        Validate PAN Card Number (5 letters + 4 digits + 1 letter)
        """
        pattern = r'^[A-Z]{5}\d{4}[A-Z]{1}$'
        if re.match(pattern, pan):
            return True, "Valid PAN Number"
        return False, "Invalid PAN Number. Format: ABCDE1234F (5 letters + 4 digits + 1 letter)"
    
    @staticmethod
    def validate_gst(gst):
        """
        Validate GST Number (15 digits: 2 state code + 10 PAN + 3 entity + 1 check digit)
        """
        pattern = r'^\d{2}[A-Z]{5}\d{4}[A-Z]{1}[A-Z\d]{1}[Z]{1}[A-Z\d]{1}$'
        if re.match(pattern, gst):
            return True, "Valid GST Number"
        return False, "Invalid GST Number. Format: 22ABCDE1234F1Z5"
    
    @staticmethod
    def validate_mobile(mobile):
        """
        Validate Indian Mobile Number (starts with 6,7,8,9 and 10 digits)
        """
        pattern = r'^[6-9]\d{9}$'
        if re.match(pattern, mobile):
            return True, "Valid Indian Mobile Number"
        return False, "Invalid Mobile Number. Must start with 6,7,8,9 and be 10 digits"
    
    @staticmethod
    def validate_email(email):
        """
        Validate Email ID
        """
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if re.match(pattern, email):
            return True, "Valid Email ID"
        return False, "Invalid Email ID"