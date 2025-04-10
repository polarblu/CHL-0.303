# puck.py - FULLY RESTORED + HORIZONTAL MOVEMENT FIX
import pygame
import random
import math
from config import *


class Puck:
    def __init__(self, rink_rect):
        self.speed_decay = 0.99  # Slower decay (was 0.98)
        self.radius = feet_to_pixels(1.0, 'y', rink_rect)
        self.color = (0, 0, 0)
        self.reset(rink_rect)

    def reset(self, rink_rect):
        self.x = rink_rect.centerx
        self.y = rink_rect.centery
        self.vx = 0  # Horizontal movement (left/right)
        self.vy = 0  # Vertical movement (up/down in HORIZONTAL RINK)

    def draw(self, surface):
        """Draw the puck on the given surface."""
        pygame.draw.circle(
            surface,
            self.color,
            (int(self.x), int(self.y)),
            self.radius
        )

    def update(self, rink_rect, current_time):
        # Movement
        self.x += self.vx
        self.y += self.vy

        # Boundary collisions (horizontal rink: top = right side)
        if self.x <= rink_rect.left + self.radius:
            self.x = rink_rect.left + self.radius
            self.vx *= -0.8  # Bounce off left wall
        elif self.x >= rink_rect.right - self.radius:
            self.x = rink_rect.right - self.radius
            self.vx *= -0.8  # Bounce off right wall

        if self.y <= rink_rect.top + self.radius:
            self.y = rink_rect.top + self.radius
            self.vy *= -0.8  # Bounce off top wall
        elif self.y >= rink_rect.bottom - self.radius:
            self.y = rink_rect.bottom - self.radius
            self.vy *= -0.8  # Bounce off bottom wall

    def _take_action(self, rink_rect):
        if random.random() < 0.25:  # Pass
            self._make_pass(rink_rect)
        else:  # Shot
            self._take_shot(rink_rect)

    def _make_pass(self, rink_rect):
        # Gentle pass (25% chance) - Less erratic
        target_x = rink_rect.centerx + random.uniform(-rink_rect.width * 0.2, rink_rect.width * 0.2)
        target_y = rink_rect.centery + random.uniform(-rink_rect.height * 0.2, rink_rect.height * 0.2)
        angle = math.atan2(target_y - self.y, target_x - self.x)
        speed = feet_to_pixels(10, 'y', rink_rect)  # Reduced speed for passes
        self.vx = math.cos(angle) * speed
        self.vy = math.sin(angle) * speed

    def _take_shot(self, rink_rect):
        # Violent shot (75% chance) - Aim for top-right (horizontal rink: "up" = negative vy)
        target_x = rink_rect.right
        target_y = rink_rect.centery + random.uniform(-rink_rect.height * 0.1, rink_rect.height * 0.1)
        angle = math.atan2(target_y - self.y, target_x - self.x)
        speed = feet_to_pixels(40, 'y', rink_rect)  # Higher speed for shots
        self.vx = math.cos(angle) * speed
        self.vy = math.sin(angle) * speed

    # In puck.py - Complete the _take_shot method (cutoff in your file)
    def _take_shot(self, rink_rect):
        # Shoot toward right side (TOP in horizontal rink: negative vy)
        target_x = rink_rect.right
        target_y = rink_rect.centery + random.uniform(-50, 50)
        angle = math.atan2(target_y - self.y, target_x - self.x)
        speed = feet_to_pixels(30, 'y', rink_rect)  # Violent shot (75% chance)
        self.vx = math.cos(angle) * speed
        self.vy = math.sin(angle) * speed