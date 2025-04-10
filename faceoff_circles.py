# faceoff_circles.py
import pygame
from config import *

class FaceOffCircle:
    def __init__(self, surface, position, include_marks=True,
                 outline_color=LINE_COLOR, fill_color=PALE_ICE_COLOR, rink_rect=None):  # **FIXED COLORS**
        """
        Args:
            surface: Pygame surface to draw on
            position: (x,y) center position in pixels
            include_marks: Whether to draw L-shaped markings
            outline_color: Defaults to LINE_COLOR (RED)
            fill_color: Defaults to PALE_ICE_COLOR
            rink_rect: Pygame Rect representing the rink boundaries
        """
        self.surface = surface
        self.position = position
        self.include_marks = include_marks
        self.outline_color = outline_color
        self.fill_color = fill_color
        self.rink_rect = rink_rect

        # Calculate radius using rink_rect if available, otherwise use surface size
        if rink_rect:
            self.radius = feet_to_pixels(15, 'y', rink_rect)
        else:
            # Fallback to screen dimensions (less ideal)
            screen_width, screen_height = surface.get_size()
            temp_rect = pygame.Rect(0, 0,
                                  feet_to_pixels(200, 'x'),
                                  feet_to_pixels(85, 'y'))
            self.radius = feet_to_pixels(15, 'y', temp_rect)

        # Dynamic padding
        self.padding = feet_to_pixels(2, 'y', rink_rect) if rink_rect else feet_to_pixels(2, 'y')
        self.size = self.radius * 2 + self.padding * 2
        self.temp_surface = pygame.Surface((self.size, self.size), pygame.SRCALPHA)
        self.circle_center = (self.size // 2, self.size // 2)

    def draw(self):
        """Draws circle with configured colors"""
        self.temp_surface.fill((0, 0, 0, 0))  # Clear surface

        # 1. Main circle
        pygame.draw.circle(self.temp_surface, self.fill_color, self.circle_center, self.radius)
        pygame.draw.circle(self.temp_surface, self.outline_color, self.circle_center, self.radius, 2)

        # 2. Center dot (1ft diameter)
        center_dot_radius = feet_to_pixels(0.5, 'y', self.rink_rect) if self.rink_rect else feet_to_pixels(0.5, 'y')
        pygame.draw.circle(self.temp_surface, self.outline_color, self.circle_center, center_dot_radius)

        # 3. L-shaped markings (if enabled)
        if self.include_marks:
            self._draw_straight_l_shapes()

        # Final blit
        blit_pos = (self.position[0] - self.size // 2, self.position[1] - self.size // 2)
        self.surface.blit(self.temp_surface, blit_pos)

    def _draw_straight_l_shapes(self):
        """Draw L-shaped markings"""
        l_gap = feet_to_pixels(0.5, 'y', self.rink_rect) if self.rink_rect else feet_to_pixels(0.5, 'y')
        h_length = feet_to_pixels(3, 'x', self.rink_rect) if self.rink_rect else feet_to_pixels(3, 'x')
        v_length = feet_to_pixels(2, 'y', self.rink_rect) if self.rink_rect else feet_to_pixels(2, 'y')
        dot_radius = feet_to_pixels(1.5, 'y', self.rink_rect) if self.rink_rect else feet_to_pixels(1.5, 'y')

        # Reference points
        top = self.size // 2 - dot_radius
        bottom = self.size // 2 + dot_radius
        left = self.size // 2 - dot_radius
        right = self.size // 2 + dot_radius

        # Draw all L-shapes
        shapes = [
            # Top-right
            [(right + l_gap, top), (right + l_gap + h_length, top)],
            [(right + l_gap, top), (right + l_gap, top - v_length)],
            # Top-left
            [(left - l_gap, top), (left - l_gap - h_length, top)],
            [(left - l_gap, top), (left - l_gap, top - v_length)],
            # Bottom-right
            [(right + l_gap, bottom), (right + l_gap + h_length, bottom)],
            [(right + l_gap, bottom), (right + l_gap, bottom + v_length)],
            # Bottom-left
            [(left - l_gap, bottom), (left - l_gap - h_length, bottom)],
            [(left - l_gap, bottom), (left - l_gap, bottom + v_length)]
        ]

        for start, end in shapes:
            pygame.draw.line(self.temp_surface, self.outline_color, start, end, 2)

def draw_all_faceoff_circles(surface, rink_rect, pens_win=False):
    """Create and draw all circles using rink_rect for positioning"""
    dot_offset_x = feet_to_pixels(FACE_OFF_DOT_TO_GOAL_FT, 'x', rink_rect)
    dot_offset_y = feet_to_pixels(22, 'y', rink_rect)
    goal_line_x = feet_to_pixels(GOAL_LINE_TO_BOARDS_FT, 'x', rink_rect)

    circles = (
        # Center circle
        FaceOffCircle(surface, rink_rect.center, include_marks=False,
                     outline_color=BLUE_LINE_COLOR, rink_rect=rink_rect),  # **FIXED: WAS COLOR_BLUE**
        # Other circles
        FaceOffCircle(surface,
                     (rink_rect.left + goal_line_x + dot_offset_x,
                      rink_rect.centery - dot_offset_y),
                     rink_rect=rink_rect),
        FaceOffCircle(surface,
                     (rink_rect.left + goal_line_x + dot_offset_x,
                      rink_rect.centery + dot_offset_y),
                     rink_rect=rink_rect),
        FaceOffCircle(surface,
                     (rink_rect.right - goal_line_x - dot_offset_x,
                      rink_rect.centery - dot_offset_y),
                     rink_rect=rink_rect),
        FaceOffCircle(surface,
                     (rink_rect.right - goal_line_x - dot_offset_x,
                      rink_rect.centery + dot_offset_y),
                     rink_rect=rink_rect),
    )

    # Draw all circles
    for circle in circles:
        circle.draw()