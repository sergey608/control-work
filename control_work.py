def filter_strings(strings):
    return [s for s in strings if len(s) <= 3]

# Пример использования:
strings = ["Hello", "2", "world", ":-)"]
filtered = filter_strings(strings)
print(filtered)  # Вывод: ['2', ':-)']