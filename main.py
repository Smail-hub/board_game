import file_operations
import random
from faker import Faker

fake = Faker("ru_RU")
fake.last_name_female()
fake.first_name_female()
fake.city()
fake.job()

skills = ["Стремительный прыжок", "Электрический выстрел", "Ледяной удар", "Стремительный удар", "Кислотный взгляд", "Тайный побег", "Ледяной выстрел", "Огненный заряд"]

skills_3 = random.sample(skills, 3)

context = {
  "first_name": fake.first_name_female(),
  "last_name": fake.last_name_female(),
  "town": fake.city(),
  "job": fake.job(),
  "strength": random.randint(3, 18),
  "agility": random.randint(3, 18),
  "endurance": random.randint(3, 18),
  "intelligence": random.randint(3, 18),
  "luck": random.randint(3, 18),
  "skill_1": skills_3[0].replace("е", "е͠"),
  "skill_2": skills_3[1].replace("е", "е͠"),
  "skill_3": skills_3[2].replace("е", "е͠"),
}

print(context)

file_operations.render_template("charsheet.svg", "result.svg", context)