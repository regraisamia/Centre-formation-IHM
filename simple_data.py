import json
import random

# Simple Moroccan data
students = []
for i in range(20):
    student = {
        "matricule": f"ST2024{i+1:04d}",
        "first_name": random.choice(["Mohammed", "Ahmed", "Youssef", "Fatima", "Aicha", "Khadija"]),
        "last_name": random.choice(["Alami", "Bennani", "Tazi", "Fassi", "Idrissi"]),
        "city": random.choice(["Casablanca", "Rabat", "Fes", "Marrakech", "Agadir"]),
        "formation": random.choice(["Dev Web", "Marketing", "Gestion", "Design"])
    }
    students.append(student)

data = {"students": students}

with open('moroccan_data.json', 'w') as f:
    json.dump(data, f, indent=2)

print("Data generated successfully!")
print(f"Students: {len(students)}")