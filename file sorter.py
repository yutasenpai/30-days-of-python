import os

# Get all files in the current directory
files = os.listdir('.')

for filename in files:
    # Look for files that start with 'day ' and end with '.py'
    if filename.startswith('day ') and filename.endswith('.py'):
        # Extract the number part (e.g., '1' from 'day 1.py')
        parts = filename.split(' ')
        num_part = parts[1].replace('.py', '')
        
        # If it's a single digit, pad it with a leading zero
        if len(num_part) == 1:
            new_filename = f"day 0{num_part}.py"
            os.rename(filename, new_filename)
            print(f"🔄 Renamed: {filename} -> {new_filename}")

print("✨ All files sorted numerically!")