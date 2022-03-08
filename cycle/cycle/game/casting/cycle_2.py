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
        self._segments2 = []
        self._prepare_body()

    def get_segments(self):
        return self._segments2

    def move_next(self): 
        for segment2 in self._segments2:
            segment2.move_next() #polymorph
        # update velocities, makes the snake move each segement will follow
        for i in range(len(self._segments2) - 1, 0, -1):
            trailing = self._segments2[i]
            previous = self._segments2[i - 1]
            velocity = previous.get_velocity()
            trailing.set_velocity(velocity)

    def get_head(self):
        return self._segments2[0]

    def grow_tail(self, number_of_segments2):
        for i in range(number_of_segments2):
            tail = self._segments2[-1]
            velocity = tail.get_velocity()
            offset = velocity.reverse()
            position = tail.get_position().add(offset)
            
            segment2 = Actor()
            segment2.set_position(position)
            segment2.set_velocity(velocity)
            segment2.set_text("#")
            segment2.set_color(constants.GREEN)
            self._segments2.append(segment2)
            
            

    def turn_head(self, velocity):
        self._segments2[0].set_velocity(velocity)
    
    def _prepare_body(self):
      
        #Position of 2 cycle 2
        x2 = int(constants.MAX_X / 3) # changed the postition of the cycle
        y2 = int(constants.MAX_Y / 2) # same here
        
      
            #Second snake
        for i in range(constants.SNAKE_LENGTH): # this may be the part we need to copy for another snake
            position2 = Point(x2 - i * constants.CELL_SIZE, y2)
            velocity = Point(1 * constants.CELL_SIZE, 0)
            text = "8" if i == 0 else "#"
            color = constants.RED if i == 0 else constants.RED
            #maybe this is how we make a new snake?
            segment2 = Actor()
            segment2.set_position(position2)
            segment2.set_velocity(velocity)
            segment2.set_text(text)
            segment2.set_color(constants.RED)
            self._segments2.append(segment2)