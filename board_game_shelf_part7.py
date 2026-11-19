# === Stage 7: Генерация идентификаторов ===
# Project: BoardGameShelf
def generate_unique_id(prefix, existing_ids):
    """Генерация уникального идентификатора с префиксом проекта и проверкой коллизий."""
    base = prefix
    counter = 1
    while f"{prefix}_{counter}" in existing_ids:
        counter += 1
    return f"{prefix}_{counter}"


class IdRegistry:
    """Регистр идентификаторов для предотвращения коллизий внутри проекта."""

    def __init__(self):
        self._registry = {}

    def register(self, prefix):
        new_id = generate_unique_id(prefix, self._registry)
        self._registry[new_id] = prefix
        return new_id

    def is_available(self, prefix):
        return generate_unique_id(prefix, self._registry) not in self._registry

    def get_used(self):
        return set(self._registry.keys())


def make_game_id(registry, name):
    return registry.register("game")


def make_session_id(registry, name):
    return registry.register("session")


def make_player_id(registry, name):
    return registry.register("player")


def make_rating_id(registry, value):
    return registry.register("rating")


if __name__ == "__main__":
    reg = IdRegistry()
    print(reg.make_game_id("Chess"))
    print(reg.make_game_id("Chess"))
    print(reg.make_session_id("Party"))
    print(reg.make_player_id("Alice"))
    print(reg.get_used())
