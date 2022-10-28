# This is the main file!
import random
from classes.fallingitem import falling_item
from classes.player import player

from classes.director import Director

from services.keyboard_service import KeyboardService
from services.video_service import VideoService

from shared.color import Color
from shared.point import Point


FRAME_RATE = 12
MAX_X = 900
MAX_Y = 600
CELL_SIZE = 15
FONT_SIZE = 15
COLS = 60
ROWS = 40
WHITE = Color(255, 255, 255)
DEFAULT_ARTIFACTS = 40


def main():
    
    # create the cast
    player = player()
    
    # create the banner
    banner = player()
    banner.set_text("")
    banner.set_font_size(FONT_SIZE)
    banner.set_color(WHITE)
    banner.set_position(Point(CELL_SIZE, 0))
    player.add_actor("banners", banner)
    
    # create the robot
    x = int(MAX_X / 2)
    y = int(MAX_Y / 2)
    position = Point(x, y)

    robot = player()
    robot.set_text("#")
    robot.set_font_size(FONT_SIZE)
    robot.set_color(WHITE)
    robot.set_position(position)
    player.add_actor("robots", robot)
    
    # create the artifacts
   

    for n in range(DEFAULT_ARTIFACTS):
        text = chr(random.randint(33, 126))

        x = random.randint(1, COLS - 1)
        y = random.randint(1, ROWS - 1)
        position = Point(x, y)
        position = position.scale(CELL_SIZE)

        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        color = Color(r, g, b)
        
        item = falling_item()
        falling_item.set_text(text)
        falling_item.set_font_size(FONT_SIZE)
        falling_item.set_color(color)
        falling_item.set_position(position)
        falling_item.set_message()
        player.add_actor("Items", falling_item)
    
    # start the game
    keyboard_service = KeyboardService(CELL_SIZE)
    video_service = VideoService(MAX_X, MAX_Y, CELL_SIZE, FRAME_RATE)
    director = Director(keyboard_service, video_service)
    director.start_game(player)


if __name__ == "__main__":
    main()