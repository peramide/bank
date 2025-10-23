# bank
💸 Bank Greeting Program — Inspired by Seinfeld (Season 7, Episode 24). This Python script prompts a user for a greeting and returns a “reward” based on how it starts:  “hello” → $0  starts with “h” → $20  otherwise → $100  Whitespace and case are ignored.



## How It Works

The program prompts you for a greeting.

It normalizes the input (removes spaces, ignores case).

Based on the first few characters, it determines your “reward.”

It prints the result to the console.

## How to Test the Code
_The test file "test_bank.py" handles that!_

Here’s how to test the code manually:

Run the program with python bank.py. Type Hello and press Enter. The program should output:
$0 
Run the program with python bank.py. Type Hello, Newman and press Enter. The program should output:
$0
Run the program with python bank.py. Type How you doing? and press Enter. The program should output
$20
Run the program with python bank.py. Type What's happening? and press Enter. The program should output
$100
