import os, subprocess

# Settings
TEST_DIR = "."                 # Directory with our program
CODE_FILE = "main.c"                # our C code
COMPILER_TIMEOUT = 10.0             # Compiler timeout (seconds)
RUN_TIMEOUT = 10.0                  # Run timeout (seconds)

# Create absolute paths
code_path = os.path.join(TEST_DIR, CODE_FILE)
app_path = os.path.join(TEST_DIR, "app")

# Compile the program
print("Building...")
try:
    ret = subprocess.run(["gcc", code_path, "-o", app_path],
                         stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE,
                         timeout=COMPILER_TIMEOUT)
except Exception as e:
    print("ERROR: Compilation failed.", str(e))
    exit(1)

# Parse the output and print
output = ret.stdout.decode('utf-8')
print(output)
output = ret.stderr.decode('utf-8')
print(output)

# Check to see if the program compiled successfully
if ret.returncode != 0:
    print("Compilation failed.")
    exit(1)
    
# Run the compiled program
print("Running...")
try:
    ret = subprocess.run([app_path],
                         stdout=subprocess.PIPE,
                         timeout=RUN_TIMEOUT)

except Exception as e:
    print("ERROR: Runtime failed.", str(e))
    exit(1)
    
# Parse the output and print
output = ret.stdout.decode('utf-8')
print("OUTPUT:", output)

# All test passed! Exit gracefuly
print("All test passed!")
exit(0)