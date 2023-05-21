from pathlib import Path

# Absolute path

p = Path()
print(p)
p1 = Path("ecommerce")
print(p1.exists())
p2 = Path("emoji")
# no path, will create path
print(p2.rmdir())
print(p2.mkdir())
p3 = Path()
# THIS WILL give all the .py files
print(p3.glob("*.PY"))

for file in p3.glob("*.py"):
    print(file)

# Relative path
