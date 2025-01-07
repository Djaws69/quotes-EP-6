from functions import *

def menu():
    print("\n==== Programming Quotes ====")
    print("1. Random quote")
    print("2. All quotes")
    print("3. Exit")

# main.py

def main():
    quotes = load_quotes()  # Suppose que load_quotes charge les citations
    
    while True:
        choice = menu()  # Affiche le menu et obtient le choix de l'utilisateur
        
        if choice == 1:  # Afficher toutes les citations
            view_quotes(quotes)
        elif choice == 2:  # Afficher un nombre spécifique de citations
            count = int(input("Enter the number of quotes to display: "))
            display_quotes(quotes, count)
        elif choice == 3:  # Quitter le programme
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")



if __name__ == "__main__":
    main()
