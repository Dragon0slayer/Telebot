from typing import Dict
import random

from config import GAME_CHOICES, WIN_CONDITIONS


class UserStateManager:
    """
    Менеджер для управління станами користувачів та їх статистикою
    """

    def __init__(self):
        self._states: Dict[int, str] = {}
        self._stats: Dict[int, Dict[str, int]] = {}

    def set_state(self, user_id: int, state: str) -> None:
        self._states[user_id] = state

    def get_state(self, user_id: int) -> str:
        return self._states.get(user_id, 'idle')

    def get_stats(self, user_id: int) -> Dict[str, int]:
        if user_id not in self._stats:
            self._stats[user_id] = {
                'wins': 0,
                'losses': 0,
                'draws': 0
            }
        return self._stats[user_id]

    def increment_wins(self, user_id: int) -> None:
        stats = self.get_stats(user_id)
        stats['wins'] += 1

    def increment_losses(self, user_id: int) -> None:
        stats = self.get_stats(user_id)
        stats['losses'] += 1

    def increment_draws(self, user_id: int) -> None:
        stats = self.get_stats(user_id)
        stats['draws'] += 1

    def reset_stats(self, user_id: int) -> None:
        self._stats[user_id] = {
            'wins': 0,
            'losses': 0,
            'draws': 0
        }


class GameLogic:
    """
    Клас для логіки гри
    """

    @staticmethod
    def determine_winner(user_choice: str, bot_choice: str) -> str:
        if user_choice == bot_choice:
            return 'draw'
        if WIN_CONDITIONS[user_choice] == bot_choice:
            return 'win'
        return 'lose'

    @staticmethod
    def get_bot_choice() -> str:
        return random.choice(GAME_CHOICES)

    @staticmethod
    def map_callback_to_choice(callback_data: str) -> str:
        choice_map = {
            'rock': '🪨 Камінь',
            'scissors': '✂️ Ножиці',
            'paper': '📄 Папір'
        }
        return choice_map.get(callback_data, '')


# Глобальні екземпляри, які будуть імпортуватися в інших модулях
state_manager = UserStateManager()
game_logic = GameLogic()