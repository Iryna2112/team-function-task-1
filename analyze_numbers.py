def analyze_numbers(numbers: list) -> dict:
    """
    Аналізує список цілих чисел і повертає статистичну інформацію.

    Args:
        numbers: список цілих чисел (може бути порожнім або містити від'ємні числа)

    Returns:
        dict з ключами: count, min, max, average, even_count, odd_count
    """
    if not numbers:
        return {
            "count": 0,
            "min": None,
            "max": None,
            "average": None,
            "even_count": 0,
            "odd_count": 0,
        }

    count = len(numbers)
    even_count = sum(1 for n in numbers if n % 2 == 0)
    odd_count = count - even_count

    return {
        "count": count,
        "min": min(numbers),
        "max": max(numbers),
        "average": sum(numbers) / count,
        "even_count": even_count,
        "odd_count": odd_count,
    }


if __name__ == "__main__":
    # Приклад з умови задачі
    test_input = [2, 5, 8, -3, 10]
    result = analyze_numbers(test_input)

    print("Вхідні дані:", test_input)
    print("Результат:")
    for key, value in result.items():
        print(f'  "{key}": {value}')

    # Перевірка порожнього списку
    print("\nПорожній список:")
    empty_result = analyze_numbers([])
    for key, value in empty_result.items():
        print(f'  "{key}": {value}')