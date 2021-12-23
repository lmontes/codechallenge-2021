import sys

n = int(sys.stdin.readline())

for i in range(0, n):
    d1, d2 = sys.stdin.readline().split(":")
    
    result = int(d1) + int(d2)
    
    if result >= 12:
        print(f"Case #{i+1}: -")
    else:
    	print(f"Case #{i+1}: {result + 1}")
