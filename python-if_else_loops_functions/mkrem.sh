#!/bin/bash

DIR="./"

# 100-print_tebahpla.py
cat > "$DIR/100-print_tebahpla.py" << 'EOF'
#!/usr/bin/python3
for i in range(122, 96, -1):
    if (122 - i) % 2 == 0:
        print("{}".format(chr(i)), end="")
    else:
        print("{}".format(chr(i - 32)), end="")
EOF

# 101-remove_char_at.py
cat > "$DIR/101-remove_char_at.py" << 'EOF'
#!/usr/bin/python3
def remove_char_at(str, n):
    if n < 0 or n >= len(str):
        return str
    return str[:n] + str[n+1:]
EOF

# 102-magic_calculation.py
cat > "$DIR/102-magic_calculation.py" << 'EOF'
#!/usr/bin/python3
def magic_calculation(a, b, c):
    if a < b:
        return c
    elif c > b:
        return a + b
    else:
        return a * b - c
EOF

# Make all files executable
chmod +x $DIR/100-print_tebahpla.py
chmod +x $DIR/101-remove_char_at.py
chmod +x $DIR/102-magic_calculation.py

echo "✅ Advanced Python files created and made executable in '$DIR'."
