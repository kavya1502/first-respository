# Function to calculate dot product
def dot_product(vector1, vector2):
    return sum(v1 * v2 for v1, v2 in zip(vector1, vector2))

# Input vectors
vector1 = list(map(int, input("Enter the elements of the first vector, separated by spaces: ").split()))
vector2 = list(map(int, input("Enter the elements of the second vector, separated by spaces: ").split()))

# Ensure both vectors have the same length
if len(vector1) != len(vector2):
    print("Error: Vectors must be of the same length.")
else:
    # Print the dot product
    print("Dot product:", dot_product(vector1, vector2))
print("hello hello")

