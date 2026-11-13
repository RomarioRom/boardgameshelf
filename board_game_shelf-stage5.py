# === Stage 5: Связанная сущность ===
# Project: BoardGameShelf
from dataclasses import dataclass, field
from datetime import date


@dataclass
class Game:
    """Настольная игра: название, жанр, число игроков, длительность."""

    title: str
    genre: str
    players: int
    duration: int


class GameCollection:
    def __init__(self):
        self._games = {}

    def add_game(self, game: Game) -> Game:
        if game.title in self._games:
            raise ValueError(f"Игра '{game.title}' уже есть в коллекции")
        self._games[game.title] = game
        return game

    def get_game(self, title: str) -> Game | None:
        return self._games.get(title)

    def titles(self) -> list[str]:
        return list(self._games)


@dataclass
class Session:
    """Отыгранный или запланированный матч по конкретной игре."""

    game_title: str
    played_on: date
    players: list[str] = field(default_factory=list)

    def add_player(self, name: str) -> None:
        if name not in self.players:
            self.players.append(name)

    @property
    def game(self) -> Game | None:
        return GameCollection().get_game(self.game_title)


class SessionBook:
    def __init__(self, collection: GameCollection):
        self.collection = collection
        self._sessions: dict[str, list[Session]] = {}

    def add_session(self, game_title: str, played_on: date, players: list[str]) -> Session:
        if not self.collection.get_game(game_title):
            raise ValueError(f"Игры '{game_title}' нет в коллекции")
        session = Session(game_title, played_on, list(players))
        self._sessions.setdefault(game_title, []).append(session)
        return session

    def sessions_for(self, game_title: str) -> list[Session]:
        return list(self._sessions.get(game_title, []))

    def all_sessions(self) -> list[Session]:
        result: list[Session] = []
        for sessions in self._sessions.values():
            result.extend(sessions)
        return result
