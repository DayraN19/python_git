import sys


def main() -> None:
    print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===\n")

    ID = input("Input Stream active. Enter archivist ID: ")
    Status = input("Input Stream active. Enter status report: ")

    print(f'[STANDARD] Archive status from {ID} : {Status}')
    print(
        "[ALERT] System diagnostic: Communication channels verified",
        file=sys. stderr
        )
    print("[STANDARD] Data transmission complete\n")
    print("Three-channel communication test successful.")


if __name__ == "__main__":
    main()
