# === Stage 1: Каркас модуля ===
# Project: BoardGameShelf
from dataclasses import dataclass, field
from typing import List


@dataclass
class Game:
    name: str
    genre: str
    players: int
    duration: int


def make_demo_games() -> List[Game]:
    return [
        Game("Catan", "Strategy", 3, 60),
        Game("Ticket to Ride", "Family", 2, 30),
        Game("Pandemic", "Cooperative", 4, 45),
    ]


def main() -> None:
    for game in make_demo_games():
        print(f"{game.name} — {game.genre}, {game.players} игрока, {game.duration} мин")


if __name__ == "__main__":
    main()
