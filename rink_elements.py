# rink_elements.py - FULLY RESTORED (CREASES REMOVED)
import pygame
import math
from config import *
from faceoff_circles import draw_all_faceoff_circles

def draw_rink(surface, screen_width, screen_height, pens_win=False):
    """Draws complete NHL rink WITHOUT creases"""
    rink_rect = get_scaled_rink_rect(screen_width, screen_height)

    # 1. Ice surface
    pygame.draw.rect(surface, PALE_ICE_COLOR, rink_rect, border_radius=feet_to_pixels(28, 'y', rink_rect))

    # 2. Boards
    pygame.draw.rect(surface, BOARD_COLOR, rink_rect, width=feet_to_pixels(0.5, 'y', rink_rect), border_radius=feet_to_pixels(28, 'y', rink_rect))

    # 3. Goal lines (thick red)
    goal_line_x_left = rink_rect.left + feet_to_pixels(11, 'x', rink_rect)
    goal_line_x_right = rink_rect.right - feet_to_pixels(11, 'x', rink_rect)
    pygame.draw.line(surface, LINE_COLOR, (goal_line_x_left, rink_rect.top), (goal_line_x_left, rink_rect.bottom), feet_to_pixels(0.33, 'y', rink_rect))
    pygame.draw.line(surface, LINE_COLOR, (goal_line_x_right, rink_rect.top), (goal_line_x_right, rink_rect.bottom), feet_to_pixels(0.33, 'y', rink_rect))

    # 4. Blue lines
    blue_line_left = rink_rect.left + feet_to_pixels(75, 'x', rink_rect)
    blue_line_right = rink_rect.right - feet_to_pixels(75, 'x', rink_rect)
    pygame.draw.rect(surface, BLUE_LINE_COLOR, (blue_line_left, rink_rect.top, feet_to_pixels(1, 'y', rink_rect), rink_rect.height))
    pygame.draw.rect(surface, BLUE_LINE_COLOR, (blue_line_right - feet_to_pixels(1, 'y', rink_rect), rink_rect.top, feet_to_pixels(1, 'y', rink_rect), rink_rect.height))

    # 5. Center line (red)
    current_y = rink_rect.top
    while current_y < rink_rect.bottom:
        pygame.draw.line(surface, LINE_COLOR, (rink_rect.centerx, current_y), (rink_rect.centerx, min(current_y + feet_to_pixels(2, 'y', rink_rect), rink_rect.bottom)), 12)
        current_y += feet_to_pixels(3, 'y', rink_rect)  # 2ft stripe + 1ft gap

    # 6. Faceoff circles (no creases)
    draw_all_faceoff_circles(surface, rink_rect, pens_win)

    return rink_rect

def get_scaled_rink_rect(screen_width, screen_height):
    """Returns properly scaled rink rectangle"""
    scale = min(screen_width / BASE_RINK_WIDTH, screen_height / (BASE_RINK_WIDTH * (85 / 200)))
    return pygame.Rect(
        (screen_width - (BASE_RINK_WIDTH * scale)) // 2,
        (screen_height - (BASE_RINK_WIDTH * (85 / 200) * scale)) // 2,
        BASE_RINK_WIDTH * scale,
        BASE_RINK_WIDTH * (85 / 200) * scale
    )