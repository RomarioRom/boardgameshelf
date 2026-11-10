# === Stage 3: Хранилище в памяти ===
# Project: BoardGameShelf
from dataclasses import dataclass, field
from typing import List, Dict, Optional


@dataclass
class Game:
    name: str
    genre: str
    num_players: int
    duration: int


class InMemoryGameStore:
    def __init__(self):
        self._games: Dict[int, Game] = {}
        self._counter = 0

    def add(self, game: Game) -> int:
        self._counter += 1
        game_id = self._counter
        self._games[game_id] = game
        return game_id

    def get(self, game_id: int) -> Optional[Game]:
        return self._games.get(game_id)

    def list_all(self) -> List[Game]:
        return list(self._games.values())

    def __len__(self) -> int:
        return len(self._games)


def create_sample_store() -> InMemoryGameStore:
    store = InMemoryGameStore()
    store.add(Game("Terraforming Mars", "Strategy", 1, 120))
    store.add(Game("Catan", "Strategy", 3, 60))
    store.add(Game("Codenames", "Party", 4, 15))
    return store


def demo() -> None:
    store = create_sample_store()
    print(f"Всего игр: {len(store)}")

    for game in store.list_all():
        print(f"  #{game_id} {game.name} ({game.genre}, {game.num_players} игрока, {game.duration} мин)")

    selected = store.get(2)
    if selected:
        print(f"Партия №2: {selected.name}")
    else:
        print("Игра не найдена")


if __name__ == "__main__":
    demo()
