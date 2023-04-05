import sys
import cv2 as cv
import time
import os
# floor1checkpoint = {"kitchen-1st floor":(138, 23), "bedroom1-1st floor":(48, 24), "empty-1st floor":(59, 41), "bath-1st floor":(31, 44), "stairentry-1st floor":(106, 45), "bath2-1st floor":(58, 50), "room-1st floor":(188, 50),"stairexit-1st floor":(106, 53),"familyroom-1st floor":(63, 67), "formaldinnning-1st floor":(100, 68),"office-1st floor":(139, 71), "exit-1st floor":(79, 76)}
# this is for the second floor
# floor2checkpoint = {"bedroom1-2nd floor":(56,24), "familyroom-2nd floor":(119, 37), "bath-2nd floor":(32, 45), "stairentry-2nd floor":(143, 45), "empty-2nd floor":(73, 51),"stairexit-2nd floor":(142, 51), "bedroom3-2nd floor":(146, 62),"bedroom2-2nd floor":(74, 63),"bathroom-2nd floor":(107, 72)}
# floor1 = floor1checkpoint.values()
# floor2 = floor2checkpoint.values()


class Node():
    def __init__(self, state, parent, action):
        self.state = state
        self.parent = parent
        self.action = action


class StackFrontier():
    def __init__(self):
        self.frontier = []

    def add(self, node):
        self.frontier.append(node)

    def contains_state(self, state):
        return any(node.state == state for node in self.frontier)

    def empty(self):
        return len(self.frontier) == 0

    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            node = self.frontier[-1]
            self.frontier = self.frontier[:-1]
            return node


class QueueFrontier(StackFrontier):

    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            node = self.frontier[0]
            self.frontier = self.frontier[1:]
            return node


class Maze():

    def __init__(self, filename, From_x, From_y, To_x, To_y, imagename):

        # Read file and set height and width of maze
        self.imagename = imagename
        with open(filename) as f:
            contents = f.read()

        # Validate start and goal
        # if contents.count("A") != 1:
        #     raise Exception("maze must have exactly one start point")
        # if contents.count("B") != 1:
        #     raise Exception("maze must have exactly one goal")

        # Determine height and width of maze
        contents = contents.splitlines()
        self.height = len(contents)
        self.width = max(len(line) for line in contents)

        # Keep track of walls
        self.walls = []
        for i in range(self.height):
            row = []
            for j in range(self.width):
                try:
                    # 56 24 143 45
                    if i == From_y and j == From_x:
                        self.start = (i, j)
                        print(self.start)
                        row.append(False)
                    elif i == To_y and j == To_x:
                        self.goal = (i, j)
                        print(self.goal)
                        row.append(False)
                    elif contents[i][j] == " ":
                        row.append(False)
                    elif contents[i][j] == "@":
                        row.append(False)
                    else:
                        row.append(True)
                except IndexError:
                    row.append(False)
            self.walls.append(row)
        self.solution = None

# not updating since it is not using
    def print(self):
        solution = self.solution[1] if self.solution is not None else None
        print()
        for i, row in enumerate(self.walls):
            for j, col in enumerate(row):
                if col:
                    print("█", end="")
                elif (i, j) == self.start:
                    print("A", end="")
                elif (i, j) == self.goal:
                    print("B", end="")
                elif solution is not None and (i, j) in solution:
                    print("*", end="")
                else:
                    print(" ", end="")
            print()
        print()

    def neighbors(self, state):
        row, col = state
        candidates = [
            ("up", (row - 1, col)),
            ("down", (row + 1, col)),
            ("left", (row, col - 1)),
            ("right", (row, col + 1))
        ]

        result = []
        for action, (r, c) in candidates:
            if 0 <= r < self.height and 0 <= c < self.width and not self.walls[r][c]:
                result.append((action, (r, c)))
        return result

    def solve(self):
        """Finds a solution to maze, if one exists."""

        # Keep track of number of states explored
        self.num_explored = 0
        # Initialize frontier to just the starting position
        start = Node(state=self.start, parent=None, action=None)
        """ Selector for Stack or Queue """
        # frontier = StackFrontier()
        frontier = QueueFrontier()
        frontier.add(start)

        # Initialize an empty explored set
        self.explored = set()

        # Keep looping until solution found
        while True:

            # If nothing left in frontier, then no path
            if frontier.empty():
                raise Exception("no solution")

            # Choose a node from the frontier
            node = frontier.remove()

            self.num_explored += 1

            # If node is the goal, then we have a solution
            if node.state == self.goal:
                actions = []
                cells = []
                while node.parent is not None:
                    actions.append(node.action)
                    cells.append(node.state)
                    node = node.parent
                # print(actions)
                actions.reverse()
                cells.reverse()
                # print(cells)
                self.solution = (actions, cells)
                return

            # Mark node as explored
            self.explored.add(node.state)

            # Add neighbors to frontier
            for action, state in self.neighbors(node.state):
                if not frontier.contains_state(state) and state not in self.explored:
                    child = Node(state=state, parent=node, action=action)
                    # print("""""""""""""")
                    # print(child.state)
                    # print(child.action)
                    frontier.add(child)

    def output_image(self, show_solution=True, show_explored=False):
        base_img = cv.imread(os.path.abspath(
            f'inmapapp/static/inmapapp/{self.imagename}'))

        base_img = cv.resize(base_img, (826, 465))
        # from PIL import Image, ImageDraw
        # cell_size = 100
        # cell_border = 2

        # # Create a blank canvas
        # img = Image.new(
        #     "RGBA",
        #     (self.width * cell_size, self.height * cell_size),
        #     "black"
        # )
        # img = Image.open("indoor_map.png")
        # draw = ImageDraw.Draw(img)
        checkpointlist = []
        solution = self.solution[1] if self.solution is not None else None
        for i, row in enumerate(self.walls):
            for j, col in enumerate(row):

                # Walls
                if col:
                    # fill = (40, 40, 40)
                    continue

                # Start
                elif (i, j) == self.start:
                    cv.circle(base_img, (round(j*4.2), round(i*4.7)),
                              1, (0, 255, 0), 20)
                    cv.putText(base_img, 'You are here!', (round(j*4.2)+5, round(i*4.7)+5),
                               cv.FONT_HERSHEY_SIMPLEX, 0.5, (124, 35, 134), 1, cv.LINE_AA)
                    continue

                # Goal
                elif (i, j) == self.goal:
                    cv.circle(base_img, (round(j*4.2), round(i*4.7)),
                              1, (243, 215, 124), 20)
                    cv.putText(base_img, 'Your destination', (round(
                        j*4.2)+5, round(i*4.7)+5), cv.FONT_HERSHEY_SIMPLEX, 0.5, (159, 71, 49), 1, cv.LINE_AA)

                    continue

                # Solution
                elif solution is not None and show_solution and (i, j) in solution:
                    # print(i,j,f'{self.imagename}')
                    checkpointlist.append((i, j))
                    fill = (0, 225, 50)

                # Explored
                elif solution is not None and show_explored and (i, j) in self.explored:
                    # fill = (212, 97, 85)
                    continue

                # Empty cell
                else:
                    # fill = (237, 240, 252)
                    continue

                # Draw cell
                # draw.rectangle(
                #     ([(j * cell_size + cell_border, i * cell_size + cell_border),
                #       ((j + 1) * cell_size - cell_border, (i + 1) * cell_size - cell_border)]),
                #     fill=fill
                # )
                # /home/sooraj/Documents/PROJECTS/INMAPWEBV2.0/inmapproject/inmapapp/templates/inmapapp/index.html

                cv.circle(base_img, (round(j*4.2), round(i*4.7)), 1, fill, 5)

        # print(f"for image{self.imagename}")
        # print(checkpointlist)
        # for checkpoints in checkpointlist:
        #     for points in floor1:
        #         x_distance = abs(checkpoints[1]-points[0])
        #         y_distance = abs(checkpoints[0]-points[1])
        #         if x_distance<=2 and y_distance<=2:
        #             print(f"checkpoint{checkpoints} is near to point{points} of floor1")
        #             cv.circle(base_img,(round(checkpoints[1]*4.2),round(checkpoints[0]*4.7)),1,(0,0,255),5)
        #     for points in floor2:
        #         x_distance = abs(checkpoints[1]-points[0])
        #         y_distance = abs(checkpoints[0]-points[1])
        #         if x_distance<=2 and y_distance<=2:
        #             print(f"checkpoint{checkpoints} is near to point{points} of floor2")
        #             cv.circle(base_img,(round(checkpoints[1]*4.2),round(checkpoints[0]*4.7)),1,(0,0,255),5)
        # print(self.solution)

        cv.imwrite(os.path.abspath(
            f'inmapapp/static/inmapapp/mod{self.imagename}'), base_img)
        return len(self.solution[1])
        # img.save(filename)


# if len(sys.argv) != 2:
#     sys.exit("Usage: python maze.py maze.txt")

# m = Maze(sys.argv[1])

# then = time.time()
# m = Maze('floor2.txt')
# print("Maze:")
# # m.print()
# print("Solving...")
# m.solve()
# print("States Explored:", m.num_explored)
# print("Solution:")
# # m.print()
# now = time.time()
# m.output_image()
# print("time",now-then)
