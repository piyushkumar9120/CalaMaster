"""
╔══════════════════════════════════════════════════════╗
║       Advanced Calculator with History               ║
║       Built by: Piyush Kumar                         ║
║       Project for: CodeStorm 2026 #2                 ║
╚══════════════════════════════════════════════════════╝
"""

import math
import datetime
import os

# ─── History Storage ────────────────────────────────────
history = []

def add_to_history(expression, result):
    timestamp = datetime.datetime.now().strftime("%H:%M:%S")
    history.append({"time": timestamp, "expr": expression, "result": result})

# ─── Basic Operations ────────────────────────────────────
def add(a, b):        return a + b
def subtract(a, b):   return a - b
def multiply(a, b):   return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero!"
    return a / b

def modulus(a, b):
    if b == 0:
        return "Error: Division by zero!"
    return a % b

def power(a, b):      return a ** b

# ─── Advanced Operations ─────────────────────────────────
def square_root(a):
    if a < 0:
        return "Error: Cannot take sqrt of negative number!"
    return math.sqrt(a)

def logarithm(a):
    if a <= 0:
        return "Error: Log undefined for zero or negative!"
    return math.log10(a)

def natural_log(a):
    if a <= 0:
        return "Error: ln undefined for zero or negative!"
    return math.log(a)

def factorial(a):
    if a < 0:
        return "Error: Factorial not defined for negative numbers!"
    if not float(a).is_integer():
        return "Error: Factorial only for whole numbers!"
    return math.factorial(int(a))

def sin_deg(a):   return math.sin(math.radians(a))
def cos_deg(a):   return math.cos(math.radians(a))
def tan_deg(a):   return math.tan(math.radians(a))

# ─── Display Functions ───────────────────────────────────
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_header():
    print("\n" + "═" * 52)
    print("   🔢  Advanced Calculator with History")
    print("   Built by Piyush Kumar | CodeStorm 2026")
    print("═" * 52)

def print_menu():
    print("""
  ┌─── BASIC ─────────────────────────────────┐
  │  1. Addition          2. Subtraction       │
  │  3. Multiplication    4. Division          │
  │  5. Modulus           6. Power (x^y)       │
  ├─── ADVANCED ──────────────────────────────┤
  │  7. Square Root       8. Log (base 10)     │
  │  9. Natural Log      10. Factorial         │
  │ 11. Sin (degrees)    12. Cos (degrees)     │
  │ 13. Tan (degrees)                          │
  ├─── EXTRAS ────────────────────────────────┤
  │ 14. View History     15. Save History      │
  │ 16. Clear History    17. Clear Screen      │
  │  0. Exit                                   │
  └───────────────────────────────────────────┘""")

def get_number(prompt):
    while True:
        try:
            return float(input(f"  👉 {prompt}: "))
        except ValueError:
            print("  ❌ Invalid input! Please enter a number.")

def show_result(expr, result):
    if isinstance(result, str) and result.startswith("Error"):
        print(f"\n  ❌ {result}")
    else:
        if isinstance(result, float) and result.is_integer():
            result_display = int(result)
        else:
            result_display = round(result, 6) if isinstance(result, float) else result
        print(f"\n  ✅ {expr} = {result_display}")
        add_to_history(expr, result_display)
    input("\n  Press Enter to continue...")

def view_history():
    print("\n" + "═" * 52)
    print("   📋  Calculation History")
    print("═" * 52)
    if not history:
        print("  No calculations yet!")
    else:
        for i, item in enumerate(history, 1):
            print(f"  [{i}] {item['time']}  |  {item['expr']} = {item['result']}")
    print("═" * 52)
    input("\n  Press Enter to continue...")

def save_history():
    if not history:
        print("\n  ❌ No history to save!")
        input("  Press Enter to continue...")
        return
    filename = f"calc_history_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    with open(filename, "w") as f:
        f.write("Advanced Calculator - History Log\n")
        f.write(f"Generated: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write("=" * 40 + "\n")
        for i, item in enumerate(history, 1):
            f.write(f"[{i}] {item['time']} | {item['expr']} = {item['result']}\n")
    print(f"\n  ✅ History saved to '{filename}'")
    input("  Press Enter to continue...")

def clear_history():
    history.clear()
    print("\n  ✅ History cleared!")
    input("  Press Enter to continue...")

# ─── Main Program ────────────────────────────────────────
def main():
    clear_screen()
    print_header()
    print("\n  Welcome, Piyush! Let's calculate! 🚀")
    input("  Press Enter to start...")

    while True:
        clear_screen()
        print_header()
        print_menu()

        choice = input("\n  Enter your choice (0-17): ").strip()

        # ── Two-number operations ──
        if choice in ['1', '2', '3', '4', '5', '6']:
            a = get_number("Enter first number")
            b = get_number("Enter second number")

            if choice == '1':
                show_result(f"{a} + {b}", add(a, b))
            elif choice == '2':
                show_result(f"{a} - {b}", subtract(a, b))
            elif choice == '3':
                show_result(f"{a} × {b}", multiply(a, b))
            elif choice == '4':
                show_result(f"{a} ÷ {b}", divide(a, b))
            elif choice == '5':
                show_result(f"{a} % {b}", modulus(a, b))
            elif choice == '6':
                show_result(f"{a} ^ {b}", power(a, b))

        # ── Single-number operations ──
        elif choice in ['7', '8', '9', '10', '11', '12', '13']:
            a = get_number("Enter number")

            if choice == '7':
                show_result(f"√{a}", square_root(a))
            elif choice == '8':
                show_result(f"log({a})", logarithm(a))
            elif choice == '9':
                show_result(f"ln({a})", natural_log(a))
            elif choice == '10':
                show_result(f"{int(a)}!", factorial(a))
            elif choice == '11':
                show_result(f"sin({a}°)", sin_deg(a))
            elif choice == '12':
                show_result(f"cos({a}°)", cos_deg(a))
            elif choice == '13':
                show_result(f"tan({a}°)", tan_deg(a))

        # ── Extras ──
        elif choice == '14':
            view_history()
        elif choice == '15':
            save_history()
        elif choice == '16':
            clear_history()
        elif choice == '17':
            clear_screen()
        elif choice == '0':
            print("\n  👋 Thanks for using Advanced Calculator!")
            print("  Good luck at CodeStorm 2026, Piyush! 🏆\n")
            break
        else:
            print("\n  ❌ Invalid choice! Please enter 0-17.")
            input("  Press Enter to continue...")

if __name__ == "__main__":
    main()
