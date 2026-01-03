def echo(data):
    if not data:
        raise ValueError("Please provide input")
    return f"Echoed: {data}"

def main():
    user_input = input("Hello how are you?\n")
    result = echo(user_input)
    print(result)


if __name__ == "__main__":
    main()



