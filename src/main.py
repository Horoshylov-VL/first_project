import os
from dotenv import load_dotenv

# Загружаем переменные из файла .env
load_dotenv()

def print_author():
    # Читаем переменную AUTHOR из окружения
    author = os.getenv("AUTHOR")
    
    # Если вдруг переменная не найдена, можно добавить запасной вариант
    if not author:
        author = "Vlad"
        
    print(f"Автор проекта: {author}")

if __name__ == "__main__":
    print_author()

