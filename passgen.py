import argparse
import string
import random


class PasswordGenerator:
    def __init__(
        self,
        length=12,
        use_lower=True,
        use_upper=True,
        use_digits=False,
        use_symbols=False,
    ):
        self.length = length
        self.lowercase_flag = use_lower
        self.uppercase_flag = use_upper
        self.integer_flag = use_digits
        self.symbol_flag = use_symbols

    def generate(self):
        charset = ""
        if self.lowercase_flag:
            charset += string.ascii_lowercase
        if self.uppercase_flag:
            charset += string.ascii_uppercase
        if self.integer_flag:
            charset += string.digits
        if self.symbol_flag:
            charset += "!@#$%^&*()-_=+[]{};:,.?/\\|~"

        if not charset:
            raise ValueError("No character sets selected. Enable at least one option.")

        return "".join(random.choice(charset) for _ in range(self.length))


def main():
    parser = argparse.ArgumentParser(description="Simple CLI Password Generator")
    parser.add_argument(
        "-l", "--length", type=int, default=12, help="Length of the password"
    )
    parser.add_argument("-s", "--symbols", action="store_true", help="Include symbols")
    parser.add_argument(
        "-i", "--integers", action="store_true", help="Include integers"
    )
    parser.add_argument(
        "-u", "--no-upper", action="store_true", help="Exclude uppercase letters"
    )
    parser.add_argument(
        "-n", "--no-lower", action="store_true", help="Exclude lowercase letters"
    )
    parser.add_argument(
        "-c", "--count", type=int, default=1, help="Number of passwords to generate"
    )

    args = parser.parse_args()

    generator = PasswordGenerator(
        length=args.length,
        use_lower=not args.no_lower,
        use_upper=not args.no_upper,
        use_digits=args.integers,
        use_symbols=args.symbols,
    )

    for _ in range(args.count):
        print(generator.generate())


if __name__ == "__main__":
    main()
