# Email-Validation-Using-Python
This repository contains two Python scripts for validating email addresses using different methods: **string manipulation** and **regular expressions** (regex).

## String Method
This script uses basic string methods to validate email addresses. It checks:
- Length of the email address.
- Presence of exactly one "@" symbol.
- Proper placement of the domain ending (e.g., .com, .net).
- Allowed characters: alphabets, digits, dots, underscores, and "@".

## Regex Method
This script uses a regular expression (regex) to validate email addresses. Regex is a sequence of characters that forms a search pattern, used for pattern matching within strings. The regex pattern in this script ensures:
- The email starts with lowercase letters.
- It may contain dots or underscores.
- It includes an "@" symbol followed by a domain name.
- The domain ends with a valid top-level domain (e.g., .com, .net).
