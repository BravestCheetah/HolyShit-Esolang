# HolyShit | Random EsoLang

*An Esolang inspired by brainfuck*  
*350+ lines of code, brace yourself if you're diving into the source*

## Installation

Install the compiler using pip:
```bash/terminal
pip install holyshit-eso
```

Or clone the Git repository and install it locally:
```bash/terminal
git clone https://github.com/bravestcheetah/HolyShit-esolang
cd HolyShit-esolang
pip install .
```

## Executing Code
**Note, all code files must end in .crap**

To execute code, first change the file extension (e.g., .py) to .geist. Then, use the HolyShit command to run the compiler:
``` Bash/terminal
HolyShit script.crap [-v | --verbal] [-d | --debug]
```
/ Run the script with optional verbosity

Alternatively:
``` Bash/terminal
hsEso script.crap [-v | --verbal] [-d | --debug]
```

This reads the code character by character and executes it. To learn how to write code, check out the next section.


## Coding

HolyShit esolang is inspired by brainf**k and has a similar structure. Here's a list of all functions/features:

| Character    | Functionality | Required Mode |
|--------------|---------------|---------------|
| `c`          | Change mode to cursor mode | Cell mode |
| `s`          | Change mode to cell mode | Cursor mode |
| `>`          | Move the cursor one cell to the right | Cursor mode |
| `<`          | Move the cursor one cell to the left | Cursor mode |
| `?`          | Add one to cursor value | Cursor mode |
| `r`          | Reset the cursor value (set to 0) | Cursor mode |
| `!`          | Subtract one from cursor value | Cursor mode |
| `%`          | Store the cursor value inside the selected cell | Cell mode |
| `~<number>`  | Loop condition: specifies the value the cell beneath should have to end the loop | Both |
| `[`          | Start of a loop; ends when the cursor hovers over a cell with the loop condition value | Both |
| `]`          | Close loop; code after executes when loop finishes | Both |
| `-`          | If statement condition: runs if the cell value matches the cursor value | Both |
| `(`          | Code block for an if statement | Both |
| `)`          | Close an if statement | Both |
| `@`          | Print the value in the cell under the cursor | Cell mode |
| `#`          | Take input from the user and store it in the cursor | Cursor mode |
| `/Text`      | Comment: ignores everything after this character on the line during compilation | Both |

## Examples

Examples can be found in the `/example-code` folder.

---
### Printing "Hello, World!"

To print "Hello, World!", store the ASCII values of each character. Below are the values:

| Character | ASCII Value |
|-----------|-------------|
| H         | 72          |
| e         | 101         |
| l         | 108         |
| l         | 108         |
| o         | 111         |
| ,         | 44          |
| (space)   | 32          |
| W         | 87          |
| o         | 111         |
| r         | 114         |
| l         | 108         |
| d         | 100         |
| !         | 33          |

### Step-by-Step Explanation

For each character:
1. Enter **cursor mode** (`c`) to edit the cursor value.
2. Use a **loop** (`~<value>[...]`) to increment the cursor value until it matches the ASCII value.
3. Switch to **cell mode** (`s`) and store the cursor value (`%`).
4. Switch to **cell mode** again to **print** (`@`) the stored value.
5. Reset the cursor (`r`) after printing and repeat for the next character.

Example for **'H'** (ASCII 72):
``` HolyShit
c  / Enter cursor mode
~72[?s%c] / Increment cursor to 72, switch to cell mode and store the value
s@ / Switch to cell mode and print 'H'
```

Combine all characters:
``` HolyShit
c~72[?s%c]s@cr~101[?s%c]s@cr~108[?s%c]s@@cr~111[?s%c]s@cr~44[?s%c]s@cr~32[?s%c]s@cr~87[?s%c]s@cr~111[?s%c]s@cr~114[?s%c]s@cr~108[?s%c]s@cr~100[?s%c]s@cr~33[?s%c]s@cr~10[?s%c]s@
/ Prints each character of "Hello, World!" by incrementing values and switching modes
```

Note: The "l" character is printed twice instead of looping multiple times.

---

### Taking Inputs

Take the ASCII value of one character using `#`:
``` HolyShit
c#s% / Enter cursor mode, take user input, and store it in a cell
```

To print the input:
``` HolyShit
c# / Take input (ASCII value of one character)
s% / Store input in cell
@ / Print value inside the cell
```

Shortened to:
``` HolyShit
c#s%@ / Take input, store it in a cell, and print it
```

For multiple inputs, use cursor movement:
```HolyShit
c#s% / Take input and store it in the cell
c> / Move to the next cell
c#s% / Next input
c> / Move to the next cell
c#s% / Last input
<< / Go back to the first cell
s@c>s@c>s@ / Print each character and move to the next cell
```
