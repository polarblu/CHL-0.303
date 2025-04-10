# config.py - FULLY RESTORED
import pygame

RINK_PADDING_PX = 20  # Padding between rink and window edges

# NHL Standard Dimensions (in feet)
RINK_LENGTH_FT = 200
RINK_WIDTH_FT = 85
CORNER_RADIUS_FT = 28
BLUE_LINE_TO_GOAL_FT = 50
GOAL_LINE_TO_BOARDS_FT = 11
FACE_OFF_CIRCLE_RADIUS_FT = 15
FACE_OFF_DOT_TO_GOAL_FT = 20

# Colors
PALE_ICE_COLOR = (240, 248, 255)  # Ice surface
BOARD_COLOR = (0, 50, 150)  # In config.py
LINE_COLOR = (200, 0, 0)  # Red lines
BLUE_LINE_COLOR = (0, 0, 200)  # Blue lines
CREASE_COLOR = (180, 220, 255)  # Goal crease (even though we're hiding it)
GOLD_COLOR = (255, 215, 0)

# Screen dimensions (200:85 aspect ratio)
BASE_RINK_WIDTH = 1000
SCREEN_WIDTH = BASE_RINK_WIDTH
SCREEN_HEIGHT = int(BASE_RINK_WIDTH * (85 / 200))  # 425

def feet_to_pixels(feet, axis='x', rink_rect=None):
    """Convert feet to pixels based on current rink dimensions."""
    if rink_rect:
        if axis == 'x':
            return int(feet * (rink_rect.width / RINK_LENGTH_FT))
        else:  # 'y'
            return int(feet * (rink_rect.height / RINK_WIDTH_FT))
    else:
        if axis == 'x':
            return int(feet * (BASE_RINK_WIDTH / RINK_LENGTH_FT))
        else:
            return int(feet * ((BASE_RINK_WIDTH * (85/200)) / RINK_WIDTH_FT))