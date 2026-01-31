import secrets
import re

def roll_damage(text: str) -> str:
    args = text.split()[1:]
    if not args:
        return "Формат: /d XdY [+/-бонус]"

    dice_part = args[0]
    bonus = 0

    if len(args) > 1:
        try:
            bonus = int(args[1])
        except ValueError:
            return "Ошибка: бонус должен быть числом"

    match = re.fullmatch(r"(\d+)d(\d+)", dice_part)
    if not match:
        return "Ошибка: формат костей должен быть XdY (например 2d10)"

    count = int(match.group(1))
    sides = int(match.group(2))

    if count <= 0 or sides <= 0:
        return "Ошибка: количество костей и граней должно быть > 0"

    rolls = [secrets.randbelow(sides) + 1 for _ in range(count)]
    total = sum(rolls) + bonus

    return (
        f"Броски: {rolls}\n"
        f"Бонус: {bonus}\n"
        f"Итоговый урон: {total}"
    )
