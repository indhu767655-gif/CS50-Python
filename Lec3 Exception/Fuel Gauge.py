def main():
    while True:
        try:
            fraction = input("fraction:")
            x,y = fraction.split("/")
            x = int(x)
            y = int(y)

            if y == 0:
                continue
            if x>y:
                continue

            percentage = round((x/y)*100)

            if percentage <= 1:
                print("E")
            elif percentage >= 99:
                print("F")
            else:
                print(f"{percentage}%")

            break

        except (ValueError, zeroDivisionError):
            continue


if __name__ == "__main__":
    main()