import constants
from game.scripting.action import Action
from game.shared.point import Point


class ControlActorsAction(Action):
    """
    An input action that controls the snake.
    
    The responsibility of ControlActorsAction is to get the direction and move the snake's head.

    Attributes:
        _keyboard_service (KeyboardService): An instance of KeyboardService.
    """

    def __init__(self, keyboard_service):
        """Constructs a new ControlActorsAction using the specified KeyboardService.
        
        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
        """
        self._keyboard_service = keyboard_service
        self._direction = Point(0,-constants.CELL_SIZE)# changed to make the cycles vertical
        #second cycle control
        self._keyboard_service2 = keyboard_service
        self._direction2 = Point(0,-constants.CELL_SIZE) # same here

    def execute(self, cast, script):
        """Executes the control actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        #we used this part to make the tail grow.
        cycle1 = cast.get_first_actor("cycle1")
        segments = cycle1.get_segments()[1:]
         # second cycle
        cycle2 = cast.get_first_actor("cycle2")
        segments2 = cycle2.get_segments()[1:]
        segments = 1    #We are going to add a new segment to the tail.
        segments2 = 1
        
        # left
        if self._keyboard_service.is_key_down('a'):
            self._direction = Point(-constants.CELL_SIZE, 0)
            cycle1.grow_tail(segments) #if the Cycle move left, is going to add a segment
        
        # right
        if self._keyboard_service.is_key_down('d'):
            self._direction = Point(constants.CELL_SIZE, 0)
            cycle1.grow_tail(segments)#if  the Cycle move right, is going to add a segment the same with the other keys
        # up
        if self._keyboard_service.is_key_down('w'):
            self._direction = Point(0, -constants.CELL_SIZE)
            cycle1.grow_tail(segments)
        # down
        if self._keyboard_service.is_key_down('s'):
            self._direction = Point(0, constants.CELL_SIZE)
            cycle1.grow_tail(segments)
        snake = cast.get_first_actor("cycle1")
        snake.turn_head(self._direction)
        
        # add the jkli movement for the second snake
        
        # left
        if self._keyboard_service2.is_key_down('j'):
            self._direction2 = Point(-constants.CELL_SIZE, 0)
            cycle2.grow_tail(segments2)
        # right
        if self._keyboard_service2.is_key_down('l'):
            self._direction2 = Point(constants.CELL_SIZE, 0)
            cycle2.grow_tail(segments2)
        # up
        if self._keyboard_service2.is_key_down('i'):
            self._direction2 = Point(0, -constants.CELL_SIZE)
            cycle2.grow_tail(segments2)

        # down
        if self._keyboard_service2.is_key_down('k'):
            self._direction2 = Point(0, constants.CELL_SIZE)
            cycle2.grow_tail(segments2)
        # Made the keyboard service for cycle2
        cycle2 = cast.get_first_actor("cycle2")
        cycle2.turn_head(self._direction2)
