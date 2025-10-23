def main():
    greeting = input("Greeting: ").lower().strip()
    print(f"${cost(greeting)}")


def cost(greeting):
    # Check if greeting starts with 'hello'
    if greeting.startswith("hello"):
        return 0
    # Check if it starts with 'h' but not 'hello'
    elif greeting.startswith("h"):
        return 20
    # Otherwise
    else:
        return 100


if __name__ == "__main__":
    main()
