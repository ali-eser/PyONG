# PyONG
#### Video Demo:  <https://youtu.be/lYvpLr0jfc0>
#### Description:
Harvard CS50x Final Project

PyONG is a remake and a reimplementation of the classic PONG in Python 3.11 using pygame 2.3.0 libraries.

PyONG is a two player game, where left paddle is controlled by "W" and "S" for up and down movement, respectively, while right paddle is controlled by "UP ARROW" and "DOWN ARROW". When opened, the game greets players with a splash screen constituted by the text "PyONG!" and below that a smaller text that prompts the player to start the game by pressing "SPACE". The board is colored greyish blue, accompanied with a orangered ball. The board also houses scores for Player 1 (left) and Player 2 (right). Every text in the game uses default SysFont (in the video it is Segoe UI, as I use Windows).

Each time the ball touches the upper or lower bound of the screen, the program inverts the y velocity of it. Similarly, when the ball collides with the left or right paddle, its x velocity is inverted. Now, I have -- somewhat -- realistic physics implemented, contrary to the original game where the bounce angle was determined by the collision coordinate on the paddle. I was about to implement this, but while I was researching the math behind it, I realized that I actually learned the solution to this problem. I hesitated to implement it, as I believed it would violate the academic honesty policy. And eventually decided to keep the realistic bounce mechanics. So it is different from classic PONG on this aspect.

Whenever a ball touches one side of the screen, the player on the other side of the screen is awarded a point. Each time a player scores the game, there is a 150ms of wait introduced in order to keep the gameplay from becoming overwhelming. The winning condition in this game is simple: the first to reach 10 wins. When a player wins the game, the game stops rendering everything including physics, player controls, and score calculation, and reads on the screen "Player 1 Won!" for example. The game prompts below the player with the text "Press SPACE to play again". When "SPACE" is pressed, the game resets everything to the initital state, and the game starts again.

There is a sound played whenever a collision is detected. I recorded a key press sound of my mechanical keyboard with iPhone, and denoised the sound file using Audacity. I also created a title bar icon for the game in MS Paint and added transparency to it with GIMP.

The reason I used Python and pygame is that I found Python to be quite light on syntax and easier to build somewhat more complex programs like games from the get go compared to C throughout CS50x. I opted to import pygame as it offers a fairly complete game development environment especially for someone like me who was about to develop his first game. I see PyONG as my introduction to game development and it teached me many different use cases of lists, dicts, tuples, functions and so on.