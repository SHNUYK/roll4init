import secrets

DIVINE_DOUBLES = {
    55: "Император защищает!",
    66: "Слаанеш наслаждается этим…",
    77: "Благословение Нургла разливается гнилью",
    88: "Кхорн требует крови!",
    99: "Тзинч переписывает судьбу"
}

def roll_check(text: str) -> str:
    args = text.split()[1:]
    if not args:
        return "Формат: /r [пул] [+/-модификаторы...]"

    try:
        base_target = int(args[0])
    except ValueError:
        return "Ошибка: базовый пул должен быть числом"

    total_modifier = 0
    for mod in args[1:]:
        if not (mod.startswith("+") or mod.startswith("-")):
            return f"Ошибка: неверный модификатор {mod}"
        try:
            total_modifier += int(mod)
        except ValueError:
            return f"Ошибка: неверный модификатор {mod}"

    target = base_target + total_modifier
    roll = secrets.randbelow(100) + 1

    target_tens = target // 10
    roll_tens = roll // 10

    lines = [
        f"Бросок: {roll}",
        f"Базовый пул: {base_target}",
        f"Модификаторы: {total_modifier:+}",
        f"Итоговый пул: {target}"
    ]

    # Криты
    if roll == 1:
        lines.append("КРИТИЧЕСКИЙ УСПЕХ")
    elif roll == 100:
        lines.append("КРИТИЧЕСКИЙ ПРОВАЛ")

    # Дубли
    if roll % 11 == 0:
        lines.append("ДУБЛЬ!")
        if roll in DIVINE_DOUBLES:
            lines.append(DIVINE_DOUBLES[roll])

    # Степени (RAW DH2)
    if roll <= target:
        degrees = (target_tens - roll_tens) + 1
        lines.append("УСПЕХ")
        lines.append(f"Степени успеха: {degrees}")
    else:
        degrees = (roll_tens - target_tens) + 1
        lines.append("ПРОВАЛ")
        lines.append(f"Степени провала: {degrees}")

    return "\n".join(lines)
