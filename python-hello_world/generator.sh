#!/bin/bash

# Create 2-print.py
cat << 'EOF' > 2-print.py
#!/usr/bin/python3
print("\"Programming is like building a multilingual puzzle")
EOF

# Create 3-print_number.py (3 lines, uses f-string, no cast)
cat << 'EOF' > 3-print_number.py
#!/usr/bin/python3
number = 98
print(f"{number} Battery street")
EOF

# Create 4-print_float.py (Float: 3.14 format, 2 digits)
cat << 'EOF' > 4-print_float.py
#!/usr/bin/python3
number = 3.14159
print(f"Float: {number:.2f}")
EOF

# Create 5-print_string.py (3x string, then first 9 chars)
cat << 'EOF' > 5-print_string.py
#!/usr/bin/python3
str = "Holberton School"
print(str * 3)
print(str[:9])
EOF

# Create 6-concat.py (5 lines, concat str1 and str2)
cat << 'EOF' > 6-concat.py
#!/usr/bin/python3
str1 = "Welcome to"
str2 = "Holberton School!"
str1 = str1 + " " + str2
print(str1)
EOF

# Create 7-edges.py (8 lines, no loop, slicing)
cat << 'EOF' > 7-edges.py
#!/usr/bin/python3
word = "Holberton"
word_first_3 = word[:3]
word_last_2 = word[-2:]
middle_word = word[1:-1]
print("First 3 letters:", word_first_3)
print("Last 2 letters:", word_last_2)
print("Middle word:", middle_word)
EOF

# Create 8-concat_edges.py (5 lines, slicing only)
cat << 'EOF' > 8-concat_edges.py
#!/usr/bin/python3
str = "Python is an interpreted, interactive, object-oriented programming language"
print(str[39:66] + str[6:7] + str[:6])
EOF

# Create 9-easter_egg.py (max 98 chars)
cat << 'EOF' > 9-easter_egg.py
#!/usr/bin/python3
import this
EOF

# Add README.md to project folder
cat << 'EOF' > README.md
# Python - Hello, World

This project introduces Python scripting. It covers:
- Basic syntax and printing
- Using environment variables
- String manipulation
- Simple shell scripting
EOF

# Add README.md to root folder
cd ../../
cat << 'EOF' > README.md
# alu-higher_level_programming

This repository contains introductory Python scripts and projects done as part of the ALU curriculum. Each subfolder contains exercises focusing on specific language features and problem-solving skills.
EOF

# Return to project directory
cd "$PROJECT_DIR" || exit

# Make all Python and shell files executable
chmod +x *.py 0-run 1-run_inline

echo "✅ Project setup complete in: $PROJECT_DIR"
