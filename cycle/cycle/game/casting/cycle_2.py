import constants
from game.casting.actor import Actor
from game.shared.point import Point


class Cycle2(Actor):
    """
    A long limbless reptile.
    
    The responsibility of Snake is to move itself.

    Attributes:
        _points (int): The number of points the food is worth.
    """
    def __init__(self):
        super().__init__()
        self._segments = []
        self._prepare_body()

    def get_segments(self):
        return self._segments

    def move_next(self): 
        for segment in self._segments:
            segment.move_next() #polymorph
        # update velocities, makes the snake move each segement will follow
        for i in range(len(self._segments) - 1, 0, -1):
            trailing = self._segments[i]
            previous = self._segments[i - 1]
            velocity = previous.get_velocity()
            trailing.set_velocity(velocity)

    def get_head(self):
        return self._segments[0]

    def grow_tail(self, number_of_segments):
        for i in range(number_of_segments):
            tail = self._segments[-1]
            velocity = tail.get_velocity()
            offset = velocity.reverse()
            position = tail.get_position().add(offset)
            
            segment = Actor()
            segment.set_position(position)
            segment.set_velocity(velocity)
            segment.set_text("#")
            segment.set_color(constants.RED)
            self._segments.append(segment)
            
            

    def turn_head(self, velocity):
        self._segments[0].set_velocity(velocity)
    
    def _prepare_body(self):      
        
        x = int((constants.MAX_X / 4) * 3)
        y = int(constants.MAX_Y / 2)
      
            
        for i in range(constants.SNAKE_LENGTH): 
            position = Point(x, y + i * constants.CELL_SIZE)
            velocity = Point(0, -1*constants.CELL_SIZE)
            text = "8" if i == 0 else "#"
            color = constants.RED if i == 0 else constants.RED
            
            segment = Actor()
            segment.set_position(position)
            segment.set_velocity(velocity)
            segment.set_text(text)
            segment.set_color(color)
            self._segments.append(segment)
