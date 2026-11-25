# === Stage 10: Текстовый поиск ===
# Project: BoardGameShelf
from difflib import SequenceMatcher


def _highlight(text, query):
    if not query:
        return text
    text = text.lower()
    query = query.lower()
    if query not in text:
        return text
    index = text.find(query)
    before = index
    after = index + len(query)
    return (
        text[:before]
        + f"\033[31m{text[before:after]}\033[0m"
        + text[after:]
    )


def search_games(games, query):
    results = []
    for game in games:
        fields = []
        if game.name:
            fields.append(game.name)
        if game.genre:
            fields.append(game.genre)
        if game.min_players:
            fields.append(str(game.min_players))
        if game.max_players:
            fields.append(str(game.max_players))
        if game.duration:
            fields.append(str(game.duration))
        if any(query.lower() in field.lower() for field in fields):
            line = " | ".join([game.name, game.genre])
            highlighted = _highlight(line, query)
            details = (
                f"Игроки: {game.min_players}-{game.max_players}, "
                f"Длительность: {game.duration} мин"
            )
            results.append(f"{highlighted}\n  {details}")
    return results


class Game:
    def __init__(self, name, genre, min_players, max_players, duration):
        self.name = name
        self.genre = genre
        self.min_players = min_players
        self.max_players = max_players
        self.duration = duration


if __name__ == "__main__":
    collection = [
        Game("Дженга", "Сборник", 1, 6, 30),
        Game("Кодовые имена", "Кооператив", 2, 4, 60),
        Game("Каркассон", "Стратегия", 2, 4, 30),
        Game("Монополия", "Экономическая", 2, 6, 120),
        Game("Экивоки", "Лингвистическая", 2, 8, 45),
    ]
    for result in search_games(collection, "кар"):
        print(result)
