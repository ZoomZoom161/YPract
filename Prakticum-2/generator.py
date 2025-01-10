
import random
import os

script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
rel_path = "input.txt"
filename = os.path.join(script_dir, rel_path)

def generate_numbers_file(filename, count, min_value=1, max_value=100):
    """
    Генерирует список случайных целых чисел и записывает их в файл
    
    Параметры:
    filename (str): имя файла для записи
    count (int): количество генерируемых чисел
    min_value (int): минимальное значение числа (по умолчанию 1)
    max_value (int): максимальное значение числа (по умолчанию 100)
    """
    try:
        with open(filename, 'w') as file:
            numbers = [str(random.randint(min_value, max_value)) for _ in range(count)]
            file.write(' '.join(numbers))
        print(f"Успешно сгенерировано и записано {count} чисел в файл {filename}")
    except Exception as e:
        print(f"Ошибка при записи в файл: {str(e)}")

# Более подробная версия с дополнительными опциями
def generate_numbers_file_extended(filename, count, min_value=1, max_value=100, 
                                 separator=' ', numbers_per_line=10):
    """
    Генерирует список случайных целых чисел и записывает их в файл
    с дополнительными опциями форматирования
    
    Параметры:
    filename (str): имя файла для записи
    count (int): количество генерируемых чисел
    min_value (int): минимальное значение числа
    max_value (int): максимальное значение числа
    separator (str): разделитель между числами
    numbers_per_line (int): количество чисел в одной строке
    """
    try:
        with open(filename, 'w') as file:
            for i in range(0, count):
                number = random.randint(min_value, max_value)
                # Добавляем число и разделитель
                file.write(str(number))
                
                # Добавляем разделитель или переход на новую строку
                if i < count - 1:  # Если это не последнее число
                    if (i + 1) % numbers_per_line == 0:
                        file.write('\n')  # Новая строка после каждых numbers_per_line чисел
                    else:
                        file.write(separator)
                        
        print(f"Успешно сгенерировано и записано {count} чисел в файл {filename}")
        print(f"Диапазон чисел: от {min_value} до {max_value}")
    except Exception as e:
        print(f"Ошибка при записи в файл: {str(e)}")

# Пример использования:
if __name__ == "__main__":
    # Использование простой версии
    #generate_numbers_file(filename, 20)
    
    # Использование расширенной версии с дополнительными параметрами
    generate_numbers_file_extended(filename, 
                                 count=1000000, 
                                 min_value=0, 
                                 max_value=1000, 
                                 separator=' ', 
                                 numbers_per_line=1)

