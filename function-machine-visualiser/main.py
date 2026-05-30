# Week 1

def f(x):
    return 2 * x + 3


def g(x):
    return x ** 2 - 4


def h(x):
    return 3 * x - 1


def show_menu():
    print("Welcome to Function Machine Visualiser")
    print()
    print("Choose a function:")
    print("1. f(x) = 2x + 3")
    print("2. g(x) = x^2 - 4")
    print("3. h(x) = 3x - 1")
    print("4. g(f(x))")
    print("5. f(g(x))")
    print()

def show_machine_diagram(input_value, rule_name, output_value):
    print("[ input:", input_value, "] ---> [", rule_name, "] ---> [ output:",
    output_value, "]")

def main():
    x = None
    show_menu()

    choice = input("Enter your choice: ")
    while choice != "1" and choice != "2" and choice != "3" and choice != "4" and choice != "5": 
        print("Invalid choice pick a number from 1 to 5.")
        print()
        choice = input("Enter your choice: ")

    while x is None:
        try:
            x = float(input("Enter a number: "))
        except ValueError:
            print("Invalid input. Please enter a number.")

    print()
    print("Input:", x)

    if choice == "1":
        print("Selected machine: f(x) = 2x + 3")
        print("Final output:", f(x))
        result = f(x)
        show_machine_diagram(x, "f(x) = 2x + 3", result)

    elif choice == "2":
        print("Selected machine: g(x) = x^2 - 4")
        result = g(x)
        print("Final output:", result)
        show_machine_diagram(x, "g(x) = x^2 - 4", result)

    elif choice == "3":
        print("Selected machine: h(x) = 3x - 1")
        result = h(x)
        print("Final output:", result)
        show_machine_diagram(x, "h(x) = 3x - 1", result)

    elif choice == "4":
        middle = f(x)
        final = g(middle)

        print("Composition: g(f(x)) means f first, then g")
        print("First machine: f(x) = 2x + 3")
        print("Middle output:", middle)
        print("Second machine: g(x) = x^2 - 4")
        print("Final output:", final)
        print("Path:", x, "-> f(x) ->", middle, "-> g(x) ->", final)

    else:
        middle = g(x)
        final = f(middle)

        print("Composition: f(g(x)) means g first, then f")
        print("First machine: g(x) = x^2 - 4")
        print("Middle output:", middle)
        print("Second machine: f(x) = 2x + 3")
        print("Final output:", final)
        print("Path:", x, "-> g(x) ->", middle, "-> f(x) ->", final)

main()
