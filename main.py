# main.py - FULLY RESTORED + RESIZE FIX
import pygame
import sys
import math
from config import *
from rink_elements import draw_rink
from puck import Puck


def main():
    pygame.init()
    current_width, current_height = SCREEN_WIDTH, SCREEN_HEIGHT
    screen = pygame.display.set_mode((current_width, current_height), pygame.RESIZABLE)
    pygame.display.set_caption("Puck Physics Test")
    clock = pygame.time.Clock()

    # Initialize rink and puck
    rink_rect = draw_rink(screen, current_width, current_height)
    puck = Puck(rink_rect)
    game_start_time = pygame.time.get_ticks() // 1000

    # Debug font
    font = pygame.font.SysFont('Arial', 16)

    while True:
        current_time = pygame.time.get_ticks() // 1000 - game_start_time

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.VIDEORESIZE:
                current_width, current_height = event.w, event.h
                screen = pygame.display.set_mode((current_width, current_height), pygame.RESIZABLE)
                rink_rect = draw_rink(screen, current_width, current_height)  # Update rink_rect on resize
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    puck._take_shot(rink_rect)
                elif event.key == pygame.K_r:
                    puck.reset(rink_rect)

        # Update
        puck.update(rink_rect, current_time)

        # Draw
        screen.fill((50, 50, 50))
        draw_rink(screen, current_width, current_height)
        puck.draw(screen)

        # Debug info
        debug_text = [
            f"Position: ({int(puck.x)}, {int(puck.y)})",
            f"Velocity: {math.hypot(puck.vx, puck.vy):.1f} px/s",
            f"Time: {current_time}s",
            "[R] Reset Puck | [SPACE] Shoot"
        ]
        for i, text in enumerate(debug_text):
            text_surface = font.render(text, True, (255, 255, 255))
            screen.blit(text_surface, (10, 10 + i * 20))

        pygame.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    main()