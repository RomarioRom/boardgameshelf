# === Stage 4: Редактирование записей ===
# Project: BoardGameShelf
import uuid


def is_editable_field(field_name):
    editable_fields = ("title", "genre", "num_players", "duration")
    return field_name in editable_fields


def validate_game_data(changes):
    if not isinstance(changes, dict):
        raise ValueError("Изменения должны быть словарём")

    for field_name, value in changes.items():
        if not is_editable_field(field_name):
            raise ValueError(f"Недопустимое поле для редактирования: {field_name}")

        if field_name == "title":
            if not isinstance(value, str) or not value.strip():
                raise ValueError("Название должно быть непустой строкой")
        elif field_name == "genre":
            if not isinstance(value, str) or not value.strip():
                raise ValueError("Жанр должен быть непустой строкой")
        elif field_name == "num_players":
            if not isinstance(value, int) or value < 1 or value > 8:
                raise ValueError("Число игроков должно быть целым от 1 до 8")
        elif field_name == "duration":
            if not isinstance(value, int) or value <= 0:
                raise ValueError("Длительность должна быть положительным числом")

    return changes


def edit_game(game, changes):
    changes = validate_game_data(changes)

    new_game = dict(game)
    for field_name, value in changes.items():
        new_game[field_name] = value

    new_game["id"] = str(uuid.uuid4())

    return new_game


def apply_game_edit(game_id, changes, games_by_id):
    if game_id not in games_by_id:
        raise KeyError(f"Игра с идентификатором {game_id} не найдена")

    updated_game = edit_game(games_by_id[game_id], changes)
    games_by_id[game_id] = updated_game
    return updated_game
