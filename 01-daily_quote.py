#!/usr/bin/env python3

import random
from datetime import date


quotes = [
    "Life is what happens when you're busy making other plans. – John Lennon",
    "Do not dwell in the past, do not dream of the future, concentrate the mind on the present moment. – Buddha",
    "The purpose of life is to live it, to taste experience to the utmost, to reach out eagerly and without fear for newer and richer experience. – Eleanor Roosevelt",
    "In the end, we only regret the chances we didn’t take. – Lewis Carroll",
    "Life is 10% what happens to us and 90% how we react to it. – Charles R. Swindoll",
    "The only impossible journey is the one you never begin. – Tony Robbins",
    "Life is really simple, but we insist on making it complicated. – Confucius"
]

def get_quote_of_the_day(quotes):
    todays_quote = None
    today = date.today()
    todays_quote = random.choice(quotes)
    return todays_quote

if __name__ == "__main__":
    print(get_quote_of_the_day(quotes))
