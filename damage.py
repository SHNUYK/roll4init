import secrets
import re

def roll_damage(text: str) -> str:
    args = text.split()[1:]
    if not args:
        return "Формат: /d XdY [+/-модификаторы...]"

    dice_part = args[0]
    total_modifier = 0
    for mod in args[1:]:
        if not (mod.startswith("+") or mod.startswith("-")):
            return f"Ошибка: неверный модификатор {mod}"
        try:
            total_modifier += int(mod)
        except ValueError:
            return f"Ошибка: неверный модификатор {mod}"

    match = re.fullmatch(r"(\d+)d(\d+)", dice_part)
    if not match:
        return "Ошибка: формат костей должен быть XdY (например 2d10)"

    count = int(match.group(1))
    sides = int(match.group(2))

    if count <= 0 or sides <= 0:
        return "Ошибка: количество костей и граней должно быть > 0"

    rolls = [secrets.randbelow(sides) + 1 for _ in range(count)]
    total = sum(rolls) + total_modifier

    total = max(0, total)
    
    return (
        f"Броски: {rolls}\n"
        f"Модификаторы: {total_modifier:+}\n"
        f"Итоговый урон: {total}"
    )
