# === Stage 9: Сортировка записей ===
# Project: BoardGameShelf
import datetime


def create_game(name, genre, players, duration, created=None):
    game = {
        "name": name,
        "genre": genre,
        "players": players,
        "duration": duration,
        "created": created or datetime.datetime.now(),
    }
    return game


def sort_games_by_name(games, reverse=False):
    return sorted(games, key=lambda g: g["name"], reverse=reverse)


def sort_games_by_created(games, reverse=False):
    return sorted(games, key=lambda g: g["created"], reverse=reverse)


def sort_games(games, by="name", reverse=False):
    if by == "name":
        return sort_games_by_name(games, reverse=reverse)
    if by == "created":
        return sort_games_by_created(games, reverse=reverse)
    raise ValueError("Неизвестное поле для сортировки")


if __name__ == "__main__":
    demo = [
        create_game("Кодовые имена", "Тактика", 2, 60),
        create_game("Каркассон", "Стратегия", 3, 30),
        create_game("Дженга", "Сборник", 4, 15),
    ]
    print(sort_games(demo, "name"))
    print(sort_games(demo, "created"))
    print(sort_games(demo, "name", reverse=True))
