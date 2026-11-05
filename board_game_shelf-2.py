# === Stage 2: Проверка полей ===
# Project: BoardGameShelf
import re


def normalize_game_title(title):
    title = title.strip()
    if not title:
        raise ValueError("Название игры не может быть пустым.")
    title = title.replace("™", "").replace("®", "").replace("©", "").strip()
    title = re.sub(r"\s+", " ", title).strip()
    title = title.strip(".,;:!?")
    if not title:
        raise ValueError("После очистки название игры пустое.")
    return title


def normalize_game_genre(genre):
    genre = (genre or "").strip()
    if not genre:
        raise ValueError("Жанр игры не может быть пустым.")
    genre = genre.replace("™", "").replace("®", "").replace("©", "").strip()
    genre = re.sub(r"\s+", " ", genre).strip()
    genre = genre.strip(".,;:!?")
    if not genre:
        raise ValueError("После очистки жанр игры пустой.")
    return genre


def normalize_players(players):
    players = players.strip()
    if not players:
        raise ValueError("Число игроков не может быть пустым.")
    try:
        value = int(players)
    except ValueError:
        raise ValueError(f"Число игроков должно быть целым: '{players}'.")
    if value < 1:
        raise ValueError("Число игроков должно быть не меньше 1.")
    if value > 4:
        raise ValueError("Число игроков не может превышать 4.")
    return value


def normalize_duration(duration):
    duration = duration.strip()
    if not duration:
        raise ValueError("Длительность партии не может быть пустой.")
    match = re.fullmatch(r"(\d+)\s*мин", duration)
    if not match:
        raise ValueError(f"Длительность должна быть в формате 'N мин': '{duration}'.")
    minutes = int(match.group(1))
    if minutes < 1:
        raise ValueError("Длительность партии должна быть не меньше 1 минуты.")
    if minutes > 1440:
        raise ValueError("Длительность партии не может превышать 1440 минут.")
    return minutes


def validate_game(game):
    errors = []
    title = normalize_game_title(game["title"])
    if not title:
        errors.append("Название игры не может быть пустым.")
    genre = normalize_game_genre(game["genre"])
    if not genre:
        errors.append("Жанр игры не может быть пустым.")
    players = normalize_players(game["players"])
    if players < 1:
        errors.append("Число игроков должно быть не меньше 1.")
    if players > 4:
        errors.append("Число игроков не может превышать 4.")
    duration = normalize_duration(game["duration"])
    if duration < 1:
        errors.append("Длительность партии должна быть не меньше 1 минуты.")
    if duration > 1440:
        errors.append("Длительность партии не может превышать 1440 минут.")
    return {
        "title": title,
        "genre": genre,
        "players": players,
        "duration": duration,
        "errors": errors,
    }
