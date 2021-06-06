from awarrior import Warrior


def main() -> int:
    w = Warrior('http://127.0.0.1:8000')
    w.get_boss()
    return 0


if __name__ == '__main__':
    main()