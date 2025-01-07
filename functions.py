import random

def display_quotes(quotes, count):
    """
    Affiche un nombre spécifique de citations.
    Si count est supérieur ou égal au nombre total de citations,
    toutes les citations sont affichées.
    """
    if count >= len(quotes):
        print("All Quotes:")
        view_quotes(quotes)  # Suppose que view_quotes est une fonction qui affiche toutes les citations
    else:
        print(f"First {count} Quotes:")
        for i in range(count):
            print_quote(quotes[i])  # Suppose que print_quote est une fonction qui affiche une citation

def load_quotes(filename):
    quotes = []
    with open(filename, 'r') as file:
        lines = file.readlines()
    for line in lines:
        line = line.strip()
        if line:
            quotes.append(line)
    return quotes

def random_quote(quotes):
    random_quote = random.choice(quotes)
    return random_quote

def print_quote(quote):
    print(quote)

def view_quotes(quotes):
    for quote in quotes:
        print_quote(quote)
