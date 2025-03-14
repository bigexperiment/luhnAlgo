from flask import Flask, render_template, request, jsonify
from flask_wtf.csrf import CSRFProtect
import re
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-here'  # Required for CSRF protection
csrf = CSRFProtect(app)

def luhn_algorithm(card_number):
    # Remove any spaces or hyphens
    card_number = ''.join(filter(str.isdigit, card_number))
    
    if not card_number.isdigit():
        return {'valid': False, 'steps': []}
    
    # Convert to list of integers
    digits = [int(d) for d in card_number]
    original_digits = digits.copy()
    
    steps = []
    steps.append({
        'description': 'Original number',
        'digits': ' '.join(str(d) for d in digits)
    })
    
    # Double every second digit from right to left
    doubled_digits = digits.copy()
    for i in range(len(digits) - 2, -1, -2):
        doubled_digits[i] *= 2
        if doubled_digits[i] > 9:
            doubled_digits[i] -= 9
    
    doubled_display = []
    for i, digit in enumerate(doubled_digits):
        if i < len(digits) - 1 and (len(digits) - i - 1) % 2 == 1:
            doubled_display.append(f"({original_digits[i]}×2={digit})")
        else:
            doubled_display.append(str(digit))
    
    steps.append({
        'description': 'Double every second digit from right to left (subtract 9 if > 9)',
        'digits': ' '.join(doubled_display)
    })
    
    # Sum all digits
    total = sum(doubled_digits)
    steps.append({
        'description': 'Sum all digits',
        'digits': f"{' + '.join(str(d) for d in doubled_digits)} = {total}"
    })
    
    # Check if total is divisible by 10
    is_valid = total % 10 == 0
    steps.append({
        'description': 'Check if sum is divisible by 10',
        'digits': f"{total} ÷ 10 = {total // 10} remainder {total % 10}"
    })
    
    return {
        'valid': is_valid,
        'steps': steps
    }

def validate_expiry_date(exp_date):
    # Check format
    if not re.match(r'^\d{2}/\d{2}$', exp_date):
        return False
    
    # Extract month and year
    month, year = exp_date.split('/')
    current_year = datetime.now().year % 100  # Get last two digits of current year
    current_month = datetime.now().month
    
    try:
        month = int(month)
        year = int(year)
        
        # Check if month is valid
        if month < 1 or month > 12:
            return False
        
        # Check if card is expired
        if year < current_year or (year == current_year and month < current_month):
            return False
            
        return True
    except ValueError:
        return False

def validate_cvc(cvc):
    # CVC should be 3 or 4 digits
    if not re.match(r'^\d{3,4}$', cvc):
        return False
    return True

def get_card_type(card_number):
    # Remove spaces and hyphens
    card_number = ''.join(filter(str.isdigit, card_number))
    
    # Visa
    if re.match(r'^4[0-9]{12}(?:[0-9]{3})?$', card_number):
        return "Visa"
    # Mastercard
    elif re.match(r'^5[1-5][0-9]{14}$', card_number):
        return "Mastercard"
    # American Express
    elif re.match(r'^3[47][0-9]{13}$', card_number):
        return "American Express"
    # Discover
    elif re.match(r'^6(?:011|5[0-9]{2})[0-9]{12}$', card_number):
        return "Discover"
    # Unknown
    else:
        return "Unknown"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/validate', methods=['POST'])
def validate():
    card_number = request.form.get('card_number', '')
    exp_date = request.form.get('exp_date', '')
    cvc = request.form.get('cvc', '')
    
    # Validate card number using Luhn algorithm
    result = luhn_algorithm(card_number)
    
    # Additional validations
    exp_date_valid = validate_expiry_date(exp_date) if exp_date else None
    cvc_valid = validate_cvc(cvc) if cvc else None
    card_type = get_card_type(card_number)
    
    return jsonify({
        'is_valid': result['valid'],
        'card_number': card_number,
        'steps': result['steps'],
        'card_type': card_type,
        'exp_date_valid': exp_date_valid,
        'cvc_valid': cvc_valid
    })

if __name__ == '__main__':
    app.run(debug=True) 