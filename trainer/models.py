from django.db import models

# Create your models here.
class Puzzle(models.Model):
    DIFFICULTY = {
        "E": "EASY - Preflop",
        "M": "MEDIUM - Flop",
        "H": "HARD - River",
    }
    difficulty = models.CharField(max_length=1, choices=DIFFICULTY, default="E")
    # >> d = Puzzle(..., difficulty="E", ...)
    # >> d.save()
    # >> d.difficulty
    # 'E'
    # >> d.get_difficulty_display()
    # 'Easy - Preflop'
    #

    hole_card_1 = models.CharField(max_length=2, help_text="Ts for 10 of spades")
    hole_card_2 = models.CharField(max_length=2, help_text="Kd for King of Diamonds")

    board_cards = models.JSONField(
        default=list,
        help_text="Enter as a list of strings -> '2s', 'Jd', 'Tc' "
    )

    pot_size = models.DecimalField(max_digits=10, decimal_places=2)
    amount_to_call = models.DecimalField(max_digits=10, decimal_places=2)
    equity = models.DecimalField(max_digits=5, decimal_places=2)
    #pot_odds

    class ActionChoices(models.TextChoices):
        FOLD = 'F', 'Fold'
        CALL = 'C', 'Call'
        RAISE = 'R', 'Raise'

    correct_action = models.CharField(
        max_length=1,
        choices=ActionChoices.choices,
        default=ActionChoices.FOLD
    )

    # TODO: hand_history JSON Field to store the generated predetermined poker game


    # TODO: add a many to many field to link users to completed puzzles
    # completed_by = ...


    


    def __str__(self):
        return f"Puzzle {self.id}: {self.hole_card_1}, {self.hole_card_2} on board {self.board_cards}"


