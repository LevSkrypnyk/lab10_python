# Автор: Петренко Іван
# Коментар: створення та запис запитання до файлу, з обробкою помилок

filename = "questions_answers.txt"

try:
    with open(filename, "w", encoding="utf-8") as file:
        file.write("Петренко Іван\n")
        file.write("Питання: Що таке списки у Python та як з ними працювати?\n")
    print(f"Файл '{filename}' успішно створено.")
except IOError as e:
    print(f"Помилка при створенні файлу: {e}")
