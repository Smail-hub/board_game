import file_operations
import random
from faker import Faker

fake = Faker("ru_RU")
fake.last_name_female()
fake.first_name_female()
fake.city()
fake.job()

skills = ["Стремительный прыжок", "Электрический выстрел", "Ледяной удар", 
          "Стремительный удар", "Кислотный взгляд", "Тайный побег", 
          "Ледяной выстрел", "Огненный заряд"]

skills_3 = random.sample(skills, 3)

# Функция для замены обычных символов на похожие из других алфавитов
def stylize_text(text):
    # Словарь замен для создания эффекта "древнего" шрифта
    replacements = {
        'а': 'а̂', 'б': 'б̵', 'в': 'в̌', 'г': 'г̇', 'д': 'д̆',
        'е': 'е͠', 'ё': 'ё̆', 'ж': 'ж̑', 'з': 'з̌', 'и': 'и̂',
        'й': 'й̃', 'к': 'к̇', 'л': 'л̌', 'м': 'м̆', 'н': 'н̂',
        'о': 'о̃', 'п': 'п̌', 'р': 'р̇', 'с': 'с̆', 'т': 'т̂',
        'у': 'у̌', 'ф': 'ф̇', 'х': 'х̂', 'ц': 'ц̆', 'ч': 'ч̌',
        'ш': 'ш̇', 'щ': 'щ̂', 'ъ': 'ъ̆', 'ы': 'ы̌', 'ь': 'ь̇',
        'э': 'э̂', 'ю': 'ю̌', 'я': 'я̆'
    }
    
    result = ''
    for char in text:
        # Заменяем символ, если он есть в словаре, иначе оставляем как есть
        result += replacements.get(char.lower(), char)
    
    return result

# Применяем стилизацию ко всем навыкам
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
    "skill_1": stylize_text(skills_3[0]),
    "skill_2": stylize_text(skills_3[1]),
    "skill_3": stylize_text(skills_3[2]),
}

file_operations.render_template("charsheet.svg", "result_2.0.svg", context)