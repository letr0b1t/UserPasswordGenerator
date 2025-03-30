# UPG - UserPasswordGenerator

**UPG - UserPasswordGenerator** is a powerful tool designed to generate personalized password dictionaries based on user-provided information. Inspired by tools like CUPP, UPG takes it a step further with enhanced features like extended Leet-speak, separators, common password patterns, and flexible date handling. Perfect for security researchers, penetration testers, and anyone interested in understanding password creation patterns.

## Features

- **Interactive Mode**: Answer simple questions about the target to create a tailored wordlist.
- **Advanced Leet-Speak**: Automatically generates variations like `4nn4`, `R1c0`, `7e57`.
- **Separators**: Adds `-`, `.`, `_` between words (e.g., `John-Fluffy`, `John.Fluffy`).
- **Common Patterns**: Includes popular suffixes like `1234`, `qwerty`, `!@#`.
- **Date Handling**: Supports `DD/MM/YYYY` input with multiple formats (e.g., `15031995`, `15-03-1995`).
- **Minimum Length Filter**: Customize the minimum password length (default: 6).
- **Output**: Saves the generated passwords to a timestamped file (e.g., `passwords_20250330_123456.txt`).

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/letr0b1t/UserPasswordGenerator.git
   cd UserPasswordGenerator
   
2. **Requirements**:
   - Python3.x (no additional dependencies required).

3. **Run the Tool**:
   ```bash
   python3 upg.py


## Example Output

For inputs `First Name: John`, `Surname: Doe`, `Pet's name: Fluffy`, `Birthdate: 15/03/1995`, and `Minimum length: 8`:
- `JohnFluffy`
- `John-Fluffy`
- `JohnFluffy1234`
- `J0hnF1uffy!1`
- `JohnMarch`
- `15031995`
- `15-03-1995`

## Contributing

Contributions are welcome! Feel free to:
- Submit bug reports or feature requests via [Issues](https://github.com/letr0b1t/UserPasswordGenerator/issues).
- Fork the repository and create a pull request with your improvements.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Inspired by [CUPP](https://github.com/Mebus/cupp) – a great starting point for password generation tools.
- Built with ❤️ by [Letr0b1t].

Happy password hunting! 🦇
