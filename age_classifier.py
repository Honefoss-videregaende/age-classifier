# Age classifier
def classify_age(age):
    if age < 6:
        return "Kindergarten"
    elif 6 <= age < 13:
        return "Primary School"
    elif 13 <= age < 16:
        return "Lower Secondary School"
    elif 16 <= age < 19:
        return "Upper Secondary School"
    elif 19 <= age < 23:
        return "University"
    else:
        return "Work"

age = int(input("Enter your age: "))
print(f"You should be in: {classify_age(age)}")
