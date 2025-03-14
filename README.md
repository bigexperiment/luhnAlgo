# Credit Card Validator - Luhn Algorithm

A web application that demonstrates the Luhn algorithm for credit card number validation with a modern, interactive UI.

## Features

- Modern, responsive UI using Tailwind CSS
- Real-time credit card number formatting
- Instant validation using the Luhn algorithm
- Visual feedback for valid/invalid card numbers
- Detailed step-by-step explanation of the Luhn algorithm calculation
- Card type detection (Visa, Mastercard, American Express, Discover)
- Expiration date and CVC validation
- Example valid and invalid card numbers
- Educational information about the Luhn algorithm

## Local Setup

1. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
python api/index.py
```

4. Open your browser and navigate to `http://localhost:5000`

## Deploying to Vercel

This application is configured for easy deployment to Vercel. Follow these steps:

1. Install the Vercel CLI:
```bash
npm install -g vercel
```

2. Login to Vercel:
```bash
vercel login
```

3. Deploy the application:
```bash
vercel
```

4. For production deployment:
```bash
vercel --prod
```

You can also deploy directly from the Vercel dashboard:

1. Push your code to a GitHub repository
2. Go to [vercel.com](https://vercel.com) and sign in
3. Click "New Project" and import your repository
4. Keep the default settings and click "Deploy"

## How to Use

1. Enter a credit card number in the input field
2. Optionally enter an expiration date (MM/YY) and CVC
3. The number will be automatically formatted for better readability
4. Click "Validate Card" or press Enter
5. The result will be displayed with:
   - Color-coded feedback (green for valid, red for invalid)
   - Card type detection
   - Detailed step-by-step calculation
   - Validation results for expiration date and CVC

## About the Luhn Algorithm

The Luhn algorithm, also known as the "modulus 10" or "mod 10" algorithm, is a checksum formula used to validate various identification numbers, including credit card numbers. The algorithm detects accidental errors such as single digit mistakes or transposition of adjacent digits.

## Test Numbers

You can test the validator with these example numbers:
- Valid: 4532 7153 3790 1241 (Visa)
- Valid: 5555 5555 5555 4444 (Mastercard)
- Valid: 3782 8224 6310 005 (American Express)
- Invalid: 4532 7153 3790 1242
- Invalid: 5555 5555 5555 5555
- Invalid: 3782 8224 6310 006 