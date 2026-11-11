from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
import random # for generating random cards to save to puzzle
from decimal import Decimal # to use correct python decimals for floating point math
from .models import Puzzle

# Create your views here.

# HOME VIEW of the trainer home page
# displays a dashboard for the users
# button to play a puzzle (calls generate_and_play_puzzle())
@login_required(login_url='/login/')
def trainer_home_view(request):
    return render(request, 'trainer/trainer_home.html')


# builds a new instance of a puzzle, and redirects the to the game
def generate_and_play_puzzle(request, chosen_difficulty='E'):
    if request.method == 'POST':
        deck = []
        for r in '23456789TJQKA':
            for s in 'hdcs':
                card = f"{r}{s}"
                deck.append(card)
        dealt = random.sample(deck, 7) # randomly select 7 cards from the deck
        hole_cards = sorted(dealt[0:2]) # give 2 cards to the user

        if chosen_difficulty == 'E':
            # Easy - Preflop, no cards on the board
            board_cards = []
        elif chosen_difficulty == 'M':
            # medium - Flop, 3 cards on the board
            board_cards = sorted(dealt[2:5])
        else:
            # Hard - All 5 cards on the board
            board_cards = sorted(dealt[2:7])

        # generate pot odds, equity here
        # for now use these as placeholders
        pot_size = Decimal('100.00')
        equity = Decimal('0.00')
        call_amount = Decimal('50.00')
        calculated_action = 'C' # F - fold, C - call, R - raise
        raise_amount = Decimal('0.00')

        new_puzzle = Puzzle.objects.create(
            hole_card_1 = hole_cards[0],
            hole_card_2 = hole_cards[1],
            board_cards = board_cards,
            pot_size = pot_size,
            equity = equity,
            amount_to_call = call_amount,
            correct_action = calculated_action,
            difficulty = chosen_difficulty,
        )

        # redirect the users browser url to /trainer/{id} in urls.py
        # each puzzle is unique, and can be played by other users
        return redirect('view_puzzle', puzzle_id=new_puzzle.id)
    else:
        return redirect('trainer')


def view_puzzle(request, puzzle_id):
    puzzle = Puzzle.objects.get(id=puzzle_id)

    context = {'puzzle': puzzle}
    return render(request, 'trainer/play_puzzle.html', context)









