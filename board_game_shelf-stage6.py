# === Stage 6: Связи между сущностями ===
# Project: BoardGameShelf
import collections


class Game:
    def __init__(self, title, genre, players, duration):
        self.title = title
        self.genre = genre
        self.players = players
        self.duration = duration


class Session:
    def __init__(self, game, players, rounds):
        self.game = game
        self.players = players
        self.rounds = rounds


def get_sessions_for_game(game, sessions):
    result = []
    for session in sessions:
        if session.game is not None and session.game.title == game.title:
            result.append(session)
    return result


def check_integrity(game, sessions):
    problems = collections.deque()
    for session in get_sessions_for_game(game, sessions):
        if session.game is None:
            problems.append(("null-game", session))
        if session.players is None:
            problems.append(("null-players", session))
        if session.rounds is None:
            problems.append(("null-rounds", session))
    return problems


def main():
    carcassonne = Game("Carcassonne", "strategy", 2, 60)
    sessions = [
        Session(carcassonne, ["Alice", "Bob"], 3),
        Session(None, ["Carol"], 1),
        Session(carcassonne, None, 2),
        Session(carcassonne, ["Dave", "Eve"], None),
        Session(Game("Azul", "strategy", 2, 30), ["Frank", "Grace"], 2),
        Session(carcassonne, ["Heidi", "Ivan"], 5),
    ]

    print("Партии для игры:", carcassonne.title)
    sessions = get_sessions_for_game(carcassonne, sessions)
    print("Найдено партий:", len(sessions))
    for session in sessions:
        print("  Игроки:", session.players, "Раундов:", session.rounds)

    problems = check_integrity(carcassonne, sessions)
    if problems:
        print("\nПроблемы целостности:")
        for issue, session in problems:
            print("  ", issue, session.players, session.rounds)
    else:
        print("\nЦелостность проверена успешно")


if __name__ == "__main__":
    main()
