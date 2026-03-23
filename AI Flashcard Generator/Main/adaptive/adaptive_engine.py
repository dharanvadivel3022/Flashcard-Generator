"""
Adaptive Learning Module
------------------------
Adjusts flashcard difficulty using user performance
"""

import time

class AdaptiveEngine:
    def __init__(self):
        self.stats = {}  # {card_id: {correct, attempts, next_review}}

    def record_attempt(self, card_id, is_correct):
        """
        Records user attempt and updates review schedule
        """
        if card_id not in self.stats:
            self.stats[card_id] = {
                "correct": 0,
                "attempts": 0,
                "next_review": time.time()
            }

        self.stats[card_id]["attempts"] += 1
        if is_correct:
            self.stats[card_id]["correct"] += 1
            self.stats[card_id]["next_review"] = time.time() + 86400  # 1 day
        else:
            self.stats[card_id]["next_review"] = time.time() + 300  # 5 minutes

    def get_due_cards(self):
        """
        Returns cards that are due for review
        """
        now = time.time()
        return [cid for cid, data in self.stats.items()
                if data["next_review"] <= now]
