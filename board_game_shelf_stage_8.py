# === Stage 8: Фильтрация записей ===
# Project: BoardGameShelf
from datetime import date


def filter_games_by_genre(games, genre):
    return [game for game in games if game["жанр"] == genre]


def filter_games_by_date_range(games, start, end):
    return [game for game in games if start <= game["дата"] <= end]


def filter_games(games, genre=None, start=None, end=None):
    filtered = games
    if genre is not None:
        filtered = filter_games_by_genre(filtered, genre)
    if start is not None:
        filtered = filter_games_by_date_range(filtered, start, end)
    return filtered
