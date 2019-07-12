import sys

def greet(name):
    print(f"Hello {name}")

print("Arguments:")
print(sys.argv)

try:
    greet(sys.argv[1])
except IndexError:
    print('Usage: python greet.py name')
