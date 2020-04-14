import pandas as pd

class Solver:
    LAYOUT = ''
    START = (0,0)
    LAST = (0,0)
    CURRENT = (0,0)
    VISITED = []

    def __init__(self, layout, starting_point=(0,0), last_position=(0,0), current_position=(0,0), visited=[]):
        self.LAYOUT = layout
        self.START = starting_point
        self.LAST = last_position
        self.CURRENT = current_position
        self.VISITED = visited


    def findStartingPoint(self, layout):
        start = (0,0)
        for v_index, row in layout.iterrows():          # Row = top to bottom
            for index, col in enumerate(row):           # Col = left to right
                if col == 's':
                    start = ((index * 32) + 16, (v_index * 32) + 16)
                    break

        print("Found start at: %s" % str(start))
        return start


    def checkEnvironment(self, old, layout, robot):
        index = (int((old[0] - 16) / 32), int((old[1] - 16) / 32))

        print('old index: ', index)
        left_block, above_block, right_block, below_block = 'b', 'b', 'b', 'b'

        if (index[0] >= 1):
            left_block = layout[index[0]-1][index[1]]
            print('left: %s' % left_block)
        if (index[1] >= 1):
            above_block = layout[index[0]][index[1]-1]
            print('above: %s' % above_block)
        if (index[0] < robot.DIMENSIONS['x']-1):
            right_block = layout[index[0]+1][index[1]]
            print('right: %s' % right_block)
        if (index[1] < robot.DIMENSIONS['y']-1):
            below_block = layout[index[0]][index[1]+1]
            print('below: %s' % below_block)

        return (left_block, above_block, right_block, below_block)

    
    # Maybe count how many options are available! Count also how often a point was visited! Special cases for the direction if already visited (only after the other if was wrong)!
    def findNextPosition(self, old, layout, robot, visited):
        index = (int((old[0] - 16) / 32), int((old[1] - 16) / 32))

        # environment = ('left', 'above', 'right', 'below')   # always check
        # environment = ('b', 'b', 'b', 'w')
        environment = self.checkEnvironment(old, layout, robot)        # returns stuff of line above
        current_direction = robot.DIRECTION
        left_is_free = environment[0] == 'w'
        above_is_free = environment[1] == 'w'
        right_is_free = environment[2] == 'w'
        below_is_free = environment[3] == 'w'
        # need to also check if point already visited!


        if current_direction == 'below':
            print('BELOW IS FREE: ', below_is_free)
            if below_is_free and (old[0], old[1] + 32) not in visited:
                robot.DIRECTION = 'below'
                return (old[0], old[1] + 32)
            if left_is_free and (old[0] - 32, old[1]) not in visited:
                robot.DIRECTION = 'left'
                return (old[0] - 32, old[1])
            if right_is_free and (old[0] + 32, old[1]) not in visited:
                robot.DIRECTION = 'right'
                return (old[0] + 32, old[1])
            if above_is_free:
                robot.DIRECTION = 'above'
                return (old[0], old[1] - 32)    
        elif current_direction == 'right':
            print('RIGHT IS FREE: ', right_is_free)
            if right_is_free and (old[0] + 32, old[1]) not in visited:
                robot.DIRECTION = 'right'
                return (old[0] + 32, old[1])
            if below_is_free and (old[0], old[1] + 32) not in visited:
                robot.DIRECTION = 'below'
                return (old[0], old[1] + 32)
            if above_is_free:
                robot.DIRECTION = 'above'
                return (old[0], old[1] - 32)
            if left_is_free:
                robot.DIRECTION = 'left'
                return (old[0] - 32, old[1])
        elif current_direction == 'left':
            print('LEFT IS FREE: ', left_is_free)
            if left_is_free and (old[0] - 32, old[1]) not in visited:
                robot.DIRECTION = 'left'
                return (old[0] - 32, old[1])
            if below_is_free and (old[0], old[1] + 32) not in visited:
                robot.DIRECTION = 'below'
                return (old[0], old[1] + 32)
            if above_is_free:
                robot.DIRECTION = 'above'
                return (old[0], old[1] - 32)
            if right_is_free:
                robot.DIRECTION = 'right'
                return (old[0] + 32, old[1])
        elif current_direction == 'above':
            print('ABOVE IS FREE: ', above_is_free)
            if above_is_free and (old[0], old[1] - 32) not in visited:
                robot.DIRECTION = 'above'
                return (old[0], old[1] - 32)
            if right_is_free and (old[0] + 32, old[1]) not in visited:
                robot.DIRECTION = 'right'
                return (old[0] + 32, old[1])
            if left_is_free and (old[0] - 32, old[1]) not in visited:
                robot.DIRECTION = 'left'
                return (old[0] - 32, old[1])
            if below_is_free:
                robot.DIRECTION = 'below'
                return (old[0], old[1] + 32)
                

        return old # - one field in the opposite direction