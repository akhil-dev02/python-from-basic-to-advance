def title(text):
    print("\n" + "=" * 60)
    print(text.center(60))
    print("=" * 60)


def pause():
    input("\nPress Enter to continue...")


def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid number.")


def confirm(prompt):
    return input(prompt).strip().lower() == "yes"
