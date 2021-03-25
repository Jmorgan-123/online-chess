# Play online chess with real chess board
Program that enables you to play online chess using real chess board.  Using computer vision it will detect the moves you make on chess board. After that, if it's your turn to move in the online game, it will make the necessary clicks to make the move.

## Setup

1. Turn off all the animations and extra features to keep chess board of online game as simple as possible.

2. Take screenshots of chess board of online game at starting position, one for when you play white and one for when you play black and save them as "white.JPG" and "black.JPG" similar to the images included in the source code.

3. Place your webcam near to your chessboard so that all of the squares and pieces can be clearly seen by it.

4. Remove all pieces from your chess board.

5. Run "board_calibration.py".

6. Check that corners of your chess board are correctly detected by "board_calibration.py" and press key "q" to save detected chess board corners. You don't need to manually select chess board corners, it should be automatically detected by the program. The square covered by points (0,0), (0,1),(1,0) and (1,1) should be a8. Example chess board detection result:

   ![](https://github.com/karayaman/Play-online-chess-with-real-chess-board/blob/main/chessboard_detection_result.jpg?raw=true)

7. Note that "constants.bin" file is created or modified.

## Usage

1. Place pieces of chess board to their starting position.
2. Start the online game.
3. Run "main.py".
4. Switch to the online game so that program detects chess board of online game. You have 5 seconds to do this step.
5.  Wait until program says "game started".
6. Make your move if it's your turn , otherwise make opponent's move.
8. Notice that program actually makes your move on the internet game if it's your turn. Otherwise, wait until program says starting and ending squares of opponent's move. 
9. Go to step 6.

## Frequently Asked Questions

### What is the program doing? How it works? 

It tracks your chess board via webcam. You should place it on top of your chess board. Make sure there
is enough light in the environment and all squares are clearly visible. When you make a move on your chess board, it understands the move you made and transfers it to chess GUI by simulating mouse clicks(It clicks starting and ending squares of your move). This way, using your chess board, you can play chess in any chess program either websites like lichess.org, chess.com or desktop programs like Fritz, Chessmaster etc.

### Placing webcam on top of the chess board sounds difficult. Can I put my laptop aside with the web cam in the laptop display?

Putting a laptop aside and using laptop's webcam won't work well with the latest release because program does not work well with side views. Personally, while using the program I am putting my laptop aside and it gives out moves via chess gui and show clocks. Instead of using laptop's webcam, I disable it
and use my old android phone's camera as webcam using an app called DroidCam. I place my phone
somewhere high enough(bookshelf for instance) so that all of the squares and pieces can be clearly seen by it.

### How well it works?

Using this software I am able to make up to 100 moves in 15+10 rapid online game without getting any errors.

## Required libraries

- opencv
- python-chess
- pyautogui
- mss
- numpy
- pyttsx3