"""
Problem 3: Number Analysis
Analyze a list of numbers provided by the user.
"""

# 1️⃣ Fonction pour demander les nombres à l'utilisateur
def get_numbers_from_user():
    numbers = []
    while True:
        value = input("Enter a number (or 'done' to finish): ").strip().lower()
        if value == "done":
            break
        try:
            numbers.append(float(value))
        except ValueError:
            print("Invalid input. Please enter a number or 'done'.")
    return numbers


# 2️⃣ Fonction d’analyse des nombres
def analyze_numbers(numbers):
    """
    Analyze the list and return a dictionary with:
    - count
    - sum
    - average
    - minimum
    - maximum
    - even_count
    - odd_count
    """
    if not numbers:
        return None

    count = len(numbers)
    total = sum(numbers)
    average = total / count
    minimum = min(numbers)
    maximum = max(numbers)
    even_count = sum(1 for n in numbers if int(n) % 2 == 0)
    odd_count = sum(1 for n in numbers if int(n) % 2 != 0)

    return {
        "count": count,
        "sum": total,
        "average": average,
        "min": minimum,
        "max": maximum,
        "even_count": even_count,
        "odd_count": odd_count,
    }


# 3️⃣ Fonction d’affichage
def display_analysis(analysis):
    if not analysis:
        return
    print("\nAnalysis Results:")
    print("-" * 20)
    for key, value in analysis.items():
        if isinstance(value, float):
            print(f"{key.capitalize()}: {value:.2f}")
        else:
            print(f"{key.capitalize()}: {value}")


# 4️⃣ Fonction principale
def main():
    print("Number Analyzer")
    print("Enter numbers one at a time. Type 'done' when finished.")
    print()

    numbers = get_numbers_from_user()
    if not numbers:
        print("No numbers entered!")
        return

    analysis = analyze_numbers(numbers)
    display_analysis(analysis)


if __name__ == "__main__":
    main()
