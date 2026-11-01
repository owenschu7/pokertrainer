CSCI 565 Final Project


TODO:
- figure out a way to represent a puzzle as a model
- need to store
  - the difficulty
  - the cards, 2 for the user, and at least 5 for the board
  - the pot size
  - the current bet/ amount to call
  - pot odds/equity calculation
  - the history of who bet before.


--------APPS---------

users
- models: User - username, email, password, first, last, score
- url routing: signup/ login/ logout/
- views:
- templates: signup.html login.html, logout.html

trainer
- models:
- url routing: trainer/trainer_home.html trainer/play.html
- views:
  - startgame
  - 
- templates:
  - trainer_home.html
    - the dashboard for the arena 
      - select difficulty
      - start a puzzle
      - view lessons
      - view stats
  - play.html
    - the actual game

puzzle (not sure if this should be grouped in with trainer app)
- models: holds info about the puzzle
  - the cards (your 2 cards + 0 or 3 or 4 or 5 from the board)
  - the difficulty (preflop, flop, turn, river etc)
  - number of players
  - which players bet.
- urls:
- views:
  - get/set functions
  - card generation (or maybe we just generate 1000 random puzzles)
- templates
  - none

lessons
- models: article title, article date, article body, article number
- url routing:
  - lessons/ - home page for all the lessons
  - lessons/{slug} - article view (slug is the article number of the article being viewed)
- views:

famous
  - this would probably be similar to the trainer apps models
- models:
  - date of game
  - players in the game/their positions (small blind, under the gun etc)
  - cards of the players
  - moves made by the players,

--------- TEMPLATES ------------

templates/
  --base templates--
  index.html
  navigation.html
  footer.html

  -- app templates --
  trainer/
    trainer_home.html
    play.html
  users/
    signup.html
    login.html
  lessons/
    lessons_home.html

--------- STATIC ------------

index.css

********* MODELS ********* 
user model
article model
puzzle model

********* USER MODELS ********* 

********* PUZZLE MODELS ********* 

********* LESSONS MODELS ********* 







CSCI 565 Final Project Proposal
Description: Poker trainer
Our Final Project will be a poker trainer/practice simulation similar to the practice game mode for chess on the chess.com website. The trainer mode will be a puzzle style game where the user gets put into a scenario and that user makes only one action (check, call, raise, or fold), and it will compare your action to a simple pot odds/equity calculator and give you a score depending on if you made a +EV move or a -EV move based on your cards, and what's on the board. +EV moves are moves you make that generate you more money over the long run, -EV is the opposite. Your score will increase if you make +EV moves, and decrease for -EV moves. There will be a leaderboard, and stats to track your score/progress. There will also be lessons/tutorials on the site for users that explain the concepts behind basic poker strategy. There will be another trainer mode where famous poker matches are pulled from a data set (or added from django admin), and you can watch poker pros make moves while pot odds and equity is being calculated, and a clearly labeled AI explanation for why that player made that move.

Feature List:
- Training arena to practice your moves (check, call, raise, all-in, fold), in different scenarios. The training arena is played solo, and the cards will be dealt randomly, along with your position in the round. You never get to see the outcome of the hand or what the opponent has, the user is only trying to make +EV moves. Each puzzle will be stored in the database (sqlite), so you can view your past sessions in your stats page.
- Calculates a ‘score’ that is determined by how well you do in the practice rounds. If you make +EV bets you will score higher, if you put yourself in bad positions by calling/raising bad cards then you make -EV bets, which will lower your score.
- Leaderboard page to track the users' scores.
- Stats page for progression and viewing past puzzles.
- Lessons explaining to beginners what makes a move +EV and how to calculate it, along with examples.
- Famous poker matches recreated to see how the pros play, and an AI explanation of why a pro made that move.

UI Navigation/Page Layout:
- Dashboard/Welcome that explains how the app works/quick links.
- Login Page (similar to midterm project)
- Navigation - website name/logo ← →Dashboard, Training Arena, Famous Hands, Lessons, About, Login/Signup/Signout
- User stats page with graph of score over time. Possible Python library: Plotly
Training arena
- The board is shown in the middle with the setup for the user to make a move, the person will always be on the bottom middle, there will be 4 other bots, who have made moves previously and you have to figure out whether to check, raise, or fold. Future possibilities include adding difficulty by making the scenario more complex. 
- We may use AI for HTML/CSS and maybe JS to create the table design, complex rendering of the chip state (if a player has more chips then their stack is bigger) or for adding animation to the cards, if we feel like it's necessary. All functions/code written with AI will be documented.
Famous matches page:
- Same design as the training area page, except for minor adjustments which include possible AI explanation of why a pro does a certain bet, and buttons like go back, or go forward.
- Lessons page:
- Lessons/tutorials we write to explain basic poker strategy that will help them in the training mode.
- About page describing our project.

