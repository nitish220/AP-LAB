def generate_pascals_triangle(n):
    triangle = []

    for i in range(n):
        row = [1 if j == 0 or j == i else row[j - 1] + row[j] for j in range(i + 1)]
        triangle.append(row)

    return triangle

def print_pascals_triangle(triangle):
    for row in triangle:
        print(" ".join(map(str, row)))

n = int(input("Enter the number of rows for Pascal's Triangle: "))
pascals_triangle = generate_pascals_triangle(n)
print("Pascal's Triangle:")
print_pascals_triangle(pascals_triangle)