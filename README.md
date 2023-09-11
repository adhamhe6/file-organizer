# File Organizer

The File Organizer is a script designed to efficiently organize files by moving them to respective folders based on their extensions. It provides a convenient way to declutter your directories and maintain a well-organized file structure.

## Features

- **Flexible Execution**: Run the script from anywhere on your computer, allowing you to organize files in any directory effortlessly.
- **Customizable Organization**: Easily tailor the script's behavior to suit your needs. Edit the main folders and their associated file extensions to create a personalized organization system.
- **Simple Setup**: Clone the repository, execute the script, and provide the path of the directory you want to organize. Let the File Organizer handle the rest.
- **Efficient Sorting**: The script intelligently identifies file extensions and moves them to their respective folders, ensuring a streamlined and tidy file structure.
- **Easy Maintenance**: Simplify file management by keeping your directories organized consistently, making it easier to locate and manage files in the future.

## Usage

1. Clone the repository to your local machine.
2. Open a terminal and navigate to the cloned directory.
3. Run the script using the command `python organize_files.py`.
4. Follow the prompts to enter the path of the directory you want to organize.
5. Sit back and let the File Organizer efficiently arrange your files, providing you with a neatly organized file structure.

**Note**: If you encounter issues with regular paths, here are two options to handle them:

- **Option 1: Use raw string literals**: You can use a raw string literal by prefixing the path string with the letter 'r'. This tells Python to interpret the string as a raw string and not process any escape characters.
```
path = r"path/to/your/folder"
```

- **Option 2: Escape the backslashes**: Alternatively, you can escape the backslashes in the path string by using double backslashes. This tells Python to interpret the backslash as a literal character.
```
path = "path\\to\\your\\folder"
```

## Contribution

Contributions to the File Organizer project are welcome! If you have any ideas, suggestions, or bug reports, please feel free to open an issue or submit a pull request on the GitHub repository.

## License

This project is licensed under the [MIT License](LICENSE). Feel free to use, modify, and distribute the script in accordance with the terms of the license.