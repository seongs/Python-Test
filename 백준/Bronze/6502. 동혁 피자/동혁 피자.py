import math

count = 0

while True:
    try:
        r, w, l = map(int, input().split())

        if r == 0:
            break

        if 2*r >= math.sqrt(w**2+l**2):
            count += 1
            print(f"Pizza {count} fits on the table.")
        else:
            count += 1
            print(f"Pizza {count} does not fit on the table.")

    except ValueError:
        break
