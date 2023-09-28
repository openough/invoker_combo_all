def generate_strings(q, w, e):
    def generate_helper(current_string, remaining_q, remaining_w, remaining_e):
        # Если все символы использованы, добавляем текущую строку в результат
        if not remaining_q and not remaining_w and not remaining_e:
            result.append(current_string)
            return

        # Если есть доступные символы q, добавляем их к текущей строке и рекурсивно вызываем функцию
        if remaining_q:
            generate_helper(current_string + 'q', remaining_q - 1, remaining_w, remaining_e)

        # То же самое для символов w и e
        if remaining_w:
            generate_helper(current_string + 'w', remaining_q, remaining_w - 1, remaining_e)

        if remaining_e:
            generate_helper(current_string + 'e', remaining_q, remaining_w, remaining_e - 1)

    result = []
    generate_helper('', q, w, e)
    return result

# Пример использования
q = 1
w = 1
e = 1
generated_strings = generate_strings(q, w, e)
print(generated_strings)