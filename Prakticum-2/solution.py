
import sys
import tracemalloc
import dis
import os
import time
from time import process_time

script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
rel_path = "input.txt"
filename = os.path.join(script_dir, rel_path)

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def create_linked_list_from_file(filename):
    try:
        # Создаем фиктивный узел в начале списка
        dummy = ListNode(0)
        current = dummy
        
        # Читаем файл и создаем список
        with open(filename, 'r') as file:
            # Читаем все числа из файла
            numbers = file.read().split()
            for num in numbers:
                try:
                    # Преобразуем строку в число и создаем новый узел
                    current.next = ListNode(int(num))
                    current = current.next
                except ValueError:
                    print(f"Пропущено некорректное значение: {num}")
                    continue
        
        return dummy.next  # Возвращаем голову списка (пропускаем фиктивный узел)
    
    except FileNotFoundError:
        print(f"Файл {filename} не найден")
        return None
    except Exception as e:
        print(f"Произошла ошибка при чтении файла: {str(e)}")
        return None

def print_linked_list(head):
    if head is None:
        print("Список пуст")
        return
    
    current = head
    while current:
        print(current.val, end=" ")
        current = current.next
    print()

def measure_performance(func):
    def wrapper(*args, **kwargs):
        # Начинаем отслеживание памяти
        tracemalloc.start()
        
        # Замеряем разные показатели времени
        wall_start = time.time()  # Реальное время
        cpu_start = process_time()  # Процессорное время
        
        # Выполняем функцию
        result = func(*args, **kwargs)
        
        # Замеряем время окончания
        wall_end = time.time()
        cpu_end = process_time()
        
        # Вычисляем затраченное время
        wall_time = wall_end - wall_start
        cpu_time = cpu_end - cpu_start
        
        # Получаем данные об использовании памяти
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        
        # Подсчитываем количество циклов
        instructions = list(dis.get_instructions(func))
        loop_count = sum(1 for ins in instructions if ins.opname in ['SETUP_LOOP', 'FOR_ITER', 'JUMP_ABSOLUTE'])
        
        # Выводим подробную статистику
        print(f"\nПроизводительность функции {func.__name__}:")
        print(f"Реальное время выполнения: {wall_time:.6f} секунд")
        print(f"Процессорное время выполнения: {cpu_time:.6f} секунд")
        print(f"Текущая память: {current / 1024:.2f} KB")
        print(f"Пиковая память: {peak / 1024:.2f} KB")
        print(f"Количество циклов в коде: {loop_count}")
        
        return result
    return wrapper

# Пример использования:
if __name__ == "__main__":
    # Применяем декоратор к функции создания и печати списка
    @measure_performance
    def test_print_list(filename):
        # Создаем список из файла и печатаем его
        head = create_linked_list_from_file(filename)
        print("Элементы списка:")
        #print_linked_list(head)
    
    # Вызываем функцию с измерением производительности
    test_print_list(filename)
