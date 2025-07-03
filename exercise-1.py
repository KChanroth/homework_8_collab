def replace_last(numbers) -> list:
    if not isinstance(numbers, list):
        return "Invalid input"

    if len(numbers) < 2:
        print("⚠️ List must contain at least two numbers to swap.")
        return numbers

    swap = numbers[:]
    swap[0], swap[-1] = swap[-1], swap[0]
    return swap

print(""" 
================================================
            🔄 Number Swapper 🔄
================================================""")

while True:
    print("➡ Enter a list of numbers separated by spaces")
    number = input(">> ")

    try:
        new_list = []
        for x in number.strip().split():
            new_list.append(int(x))
    except ValueError:
        print("⚠️ Please enter valid numbers only.")
        continue

    print("-" * 48)
    result = replace_last(new_list)
    print("✅ Swapped List:", result)
    print("-" * 48)

    yn = input("🔁 Do you want to try again? (y/n): ")
    print("-" * 48)

    if yn.lower() != "y":
        print("=" * 48)
        print("👋 Goodbye! Thanks for using Number Swapper!")
        print("=" * 48)
        break
