import math

def classify_roots(discriminant):

    if discriminant > 0:
        return "real_distinct", "Two distinct real roots"
    elif discriminant == 0:
        return "real_repeated", "One repeated real root"
    else:
        return "complex", "Two complex roots"

def calculate_roots(a, b, discriminant):
    root_calculations = [
        ((-b + math.sqrt(discriminant)) / (2 * a), "first"),  # Root 1 
        ((-b - math.sqrt(discriminant)) / (2 * a), "second")  # Root 2
    ] 

    if discriminant < 0:
        root_calculations = [
            (complex(-b / (2 * a), math.sqrt(-discriminant) / (2 * a)), "first"),
            (complex(-b / (2 * a), -math.sqrt(-discriminant) / (2 * a)), "second")
        ]

    return root_calculations

a = float(input("Enter the coefficient a: "))
b = float(input("Enter the coefficient b: "))
c = float(input("Enter the coefficient c: "))

discriminant = b ** 2 - 4 * a * c

root_type, description = classify_roots(discriminant)

roots = calculate_roots(a, b, discriminant)

print(f"\nThe quadratic equation has {description}:")
for root, label in roots:
    print(f"Root {label}: {root}") 
