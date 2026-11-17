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

    #INFO:
    # this is where we generate a random puzzle based on the difficulty
    # the difficulties will have a lot in common except for the complexity of the hand
    # we dont determine the other players hand (their cards) nor do we increase/decrease the bet sizes they make because they have good hands.
    # instead we focus on something called 'breakeven equity'
    #   breakeven equity: a simple equation that returns a percentage
    #   - this percentage tells us how much probability of getting another card to improve our hand is needed to make +EV calling decisions
    #   - ex: breakeven equity = 8%
    #         - if we have a 20% chance of getting a card to make a flush
    #         > then we should call because 8 < 20
    #         - if we have a 4% chance of getting a card to make a three of a kind
    #         > then we should fold because 8 > 4
    #
    #  this is a good skill to have in poker; to figure out these numbers fast. This is what we are 'training'
    #  we are not training to read the opponents range, nor figure out complex psycological 'reads' on the players.

    if request.method == 'POST':
        # create a deck with 52 cards
        deck = []
        for r in '23456789TJQKA':
            for s in 'hdcs':
                card = f"{r}{s}"
                deck.append(card)
        # we only take 7 random cards. 2 for user, 5 for the board (some difficulties wont use all 7)
        dealt = random.sample(deck, 7) # randomly select 7 cards from the deck

        # give 2 cards to the user
        hole_cards = sorted(dealt[0:2]) 

        # TODO: we need to generate the hand history, this part is tricky
        # bets shall be chosen randomly (within reason)
        # in the difficulties easy will give simple numbers, hard will have more bets the user needs to account for

        #JSON representation for hand history.
        # we store everything we need to represent who bet, how much, what position they are in, and when.
        # it is stored as a python array of dictionaries
        # each item in the array (dictionary) in the array will hold an action for a player.
        # if a player is out (folded), we should not store any actions after the player
        # preflop will have 8 or more items associated with it
        # flop, turn, river will have a variable amount of items associated with it, depending on complexity of the actions
        # our app will use 6 players in every game because of position naming and simplicity
        # ex:
        # two players (SB, BB) must put in a blind before starting. SB puts 0.5, BB puts 1    (SB always puts half the BB)
        # the 'amount' is stored as 'big blinds' and converted to chips, 1 BB-> 10$ on the front end
        # we store the amounts in 'big blinds', and we can convert to whichever denomination the user chooses on the front end

        # positions explained:
        # SB - small blind
        # BB - big blind
        # UTG - under the gun
        # HJ - high jack
        # CO - cut off
        # BTN - button/dealer
        # after the round is over the positions rotate, if you were the SB you are now the BTN.
        # there are more names for positions with more than 6 people. we can later add more, or less

        # streets explained:
        # streets are the betting rounds; in each 'street' each player has a chance to check, raise, call, fold
        # pf - preflop    each player decides to bet after getting their two cards,
        #                 each player must call the BB, who automatically has to put up 1 BB
        #                 the first to make a decision is the 'UTG' as no decisons were made if you are SB, or BB, because those bets are automatically required
        # f - flop        3 cards get dealt on the board. each player gets to bet/call/check/raise
        #                 SB is the first to act
        # t - turn        +1 card gets dealt to the board, action starts with the SB
        # r - river       +1 card gets dealt to the board, action starts with the SB
        #                 after everyone bets, who ever is still in shows their cards and the highest hand wins

        # example of what we need to generate for each puzzle

        # player  position  street  action  amount  potsize
        # 6       SB        pf      blind   0.5     0.5
        # 1       BB        pf      blind   1       1.5
        # 2       UTG       pf      fold    0       1.5
        # 3       HJ        pf      raise   5       6.5
        # 4       CO        pf      call    5       11.5
        # 5       BTN       pf      call    5       16.5
        # 6       SB        pf      call    5       21
        # 1       SB        pf      fold    0       21
        # 6       SB        f       check   0       21
        # 1       BB        f       check   0       21
        # 2       UTG       f       check   0       21
        # 3       HJ        f       bet     2       23
        # 4       CO        f       (decision will be made here if the user is playing as player 4 and difficulty is medium)

        # we just need to generate a random senario (like the one above) up until the a spot where the user should make a decision
        # in easy/hard difficulty this will look the same but different in when we decide the player acts. hard -> later in the game. easy -> early in the game
        # side note: easy difficulty can just be training for deciding to go in with good starting cards, and different equations can be used to measure success

        # after we do that we can run an algorithm to check how many 'outs' we have
        # we then can calculate the equity we have in the game. (using thoes 'outs')
        # we also must calculate the breakeven equity of the last bet

        # after the user makes a decision, (this should be in a different function)
        # we then see if the breakeven equity is right to call.
        # we apply a score out of 100 to the decision.
        # if the decision was bad it gets 0/100
        # if the decision was good it gets 100/100
        # we need to figure out how to rank a good call, this part can be tricky
        # we also can make an algorithm that ranks users. bad users will hover around 0, good users will have a higher score
        # bad users score should increase by more when they 'win'. but go down a little when they 'lose'
        # good users score should increase by a little when they 'win' and go down by a lot if they 'lose'
        # theres a better explaination for that somewhere else


        if chosen_difficulty == 'E':
            # Easy - Preflop, no cards on the board
            board_cards = []
            # TODO: create a random senario for bets players have made in hand_history
            # we can do this later
        elif chosen_difficulty == 'M':
            # medium - Flop, 3 cards on the board
            board_cards = sorted(dealt[2:5])
            # TODO: create a random senario for bets players have made in hand_history




        else:
            # Hard - All 5 cards on the board
            board_cards = sorted(dealt[2:7])
            # TODO: create a random senario for bets players have made in hand_history
            # we can do this later
            


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









