# === Stage 11: Поиск по нескольким словам ===
# Project: BoardGameShelf
def find_games(query, games):
    """Поиск игр по нескольким словам с поддержкой исключений через префикс '-'.

    query — строка запроса, например "приключения -карта".
    games — список объектов с полем title (название игры).
    Возвращает список названий игр, соответствующих запросу.
    """
    terms = []
    for token in query.split():
        if token.startswith("-"):
            terms.append(("exclude", token[1:].lower()))
        else:
            terms.append(("include", token.lower()))

    results = []
    for game in games:
        title = game.title.lower()
        include_flags = []
        exclude_flags = []
        for kind, term in terms:
            if term in title:
                if kind == "include":
                    include_flags.append(True)
                else:
                    exclude_flags.append(True)
        if not any(exclude_flags) and any(include_flags):
            results.append(game.title)
    return results

def main():
    sample_games = [
        {"title": "Катапульта: Приключения на острове", "genre": "стратегия", "players": 2, "duration": 60},
        {"title": "Путешествие по карте", "genre": "приключения", "players": 4, "duration": 90},
        {"title": "Карта сокровищ", "genre": "приключения", "players": 2, "duration": 45},
        {"title": "Штурм замка", "genre": "стратегия", "players": 3, "duration": 120},
        {"title": "Остров сокровищ", "genre": "приключения", "players": 5, "duration": 75},
    ]

    print("Поиск 'приключения':")
    for title in find_games("приключения", sample_games):
        print(" -", title)

    print()
    print("Поиск 'приключения -карта':")
    for title in find_games("приключения -карта", sample_games):
        print(" -", title)

    print()
    print("Поиск 'карта':")
    for title in find_games("карта", sample_games):
        print(" -", title)

if __name__ == "__main__":
    main()
