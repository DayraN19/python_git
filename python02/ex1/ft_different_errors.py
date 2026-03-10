def garden_operations(arg: str) -> None:
    try:
        if arg == "value":
            open("file.txt", "invalid")      # ValueError

        elif arg == "zero":
            10 / 0                           # ZeroDivisionError

        elif arg == "file":
            open("missing.txt", "r")         # FileNotFoundError

        elif arg == "key":
            plants = {"rose": 10}
            plants["missing_plant"]          # KeyError

        else:
            print("No error triggered")

    except ValueError:
        print("ValueError detected")

    except ZeroDivisionError:
        print("ZeroDivisionError detected")

    except FileNotFoundError:
        print("FileNotFoundError detected")

    except KeyError:
        print("KeyError detected")


def test_error_types() -> None:
    print("=== Garden Error Types Demo ===")

    for test in ["value", "zero", "file", "key", "unknown"]:
        print(f"Testing: {test}")
        garden_operations(test)

    print("All error types tested successfully!")


def main() -> None:
    test_error_types()


if __name__ == "__main__":
    main()
