import numpy
from pwn import *
import datetime
import logging
from heapq import *
import math
logging.basicConfig(filename=datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S") + '.log', encoding='utf-8', level=logging.DEBUG)

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

opposite_letters = {"w": "s", "a": "d", "s": "w", "d": "a"}
letter_directions = {
    "a": (0, -1),
    "w": (-1, 0),
    "s": (1, 0),
    "d": (0, 1),
}

class remote_maze:
    conn = None
    flag = None
    current_location = None
    safe_squares = numpy.full((2034, 2034), '1')
    num_bombs = numpy.full((2034, 2034), '?')
    min_x = 0
    max_y = 2034
    visited_v2 = []
    leniency = 3
    manhattan = 4066


    def __init__(self):
        self.conn = remote('pwn.chall.pwnoh.io', 13380)
        self.flag = tuple([int(i) for i in self.conn.recvline().decode().strip().split(' ')])
        self.min_x = (max(math.floor(self.flag[0]/3)-1, 0))*3
        self.max_y = min((math.ceil(self.flag[1]/3)+1)*3, 2033)
        self.visited_v2 = []
        self.leniency = 3
        self.manhattan = 4066
        self.tick()
        self.mov('a')

    # Returns number of nearby "bombs"
    def mov(self, letter):
        if letter not in letter_directions.keys():
            raise "Invalid key"
        logging.debug("Moving " + letter)
        self.conn.sendline(letter.encode())
        return self.tick()

    def get_flag_location(self):
        return self.flag

    def tick(self):
        location_str = self.conn.recvline().decode()
        logging.debug(location_str)
        self.current_location = tuple([int(i) for i in location_str.strip("[]\n ").split(' ') if i.isnumeric()])
        self.safe_squares[self.current_location[0]][self.current_location[1]] = '0'
        other = self.conn.clean(0.3).decode()
        logging.debug(other)
        numBombs = 0
        if not other == '':
            if "try again!" in other:
                print("Game ended")
                exit(1)
            else:
                numBombs = len([i for i in other.split('\n') if i != ''])
        self.num_bombs[self.current_location[0]][self.current_location[1]] = numBombs;
        return numBombs

    def get_current_location(self):
        return self.current_location

    def get_safe_squares(self):
        return self.safe_squares

    def pretty_print_safe(self):
        for i in range(max(self.current_location[0] - 5, 0), min(self.current_location[0] + 5, 2034)):
            for j in range(max(self.current_location[1] - 5, 0), min(self.current_location[1] + 5, 2034)):
                if i == self.current_location[0] and j == self.current_location[1]:
                    print('*', end="")
                else:
                    print(self.safe_squares[i][j], end="")
            print()
        print(self.safe_squares[self.current_location[0]][self.current_location[1]])

    def pretty_print_bombs(self):
        for i in range(max(self.current_location[0] - 5, 0), min(self.current_location[0] + 5, 2034)):
            for j in range(max(self.current_location[1] - 5, 0), min(self.current_location[1] + 5, 2034)):
                if i == self.current_location[0] and j == self.current_location[1]:
                    print('*', end="")
                else:
                    out = str(self.num_bombs[i][j])
                    color = bcolors.ENDC
                    if out == "0":
                        color = bcolors.OKGREEN
                    elif out == "1" or out == "2" or out == "3":
                        color = bcolors.WARNING
                    elif out == 'b':
                        color = bcolors.FAIL
                    elif out == "?":
                        color = bcolors.OKCYAN

                    print(color, out, bcolors.ENDC, end="", sep='')
            print()
        print(self.num_bombs[self.current_location[0]][self.current_location[1]])
        print("(" + str(self.current_location[0]) + ", " + str(self.current_location[1]) + ")")


    def three_print_bombs(self):
        three_pos = [self.current_location[0] % 3, self.current_location[1] % 3]
        for i in range(self.current_location[0] - three_pos[0], self.current_location[0] - three_pos[0] + 3):
            for j in range(self.current_location[1] - three_pos[1], self.current_location[1] - three_pos[1] + 3):
                if i == self.current_location[0] and j == self.current_location[1]:
                    print('*', end="")
                else:
                    print(self.num_bombs[i][j], end="")
            print()





    def start_find_zero_area(self):

        bombs = int(self.num_bombs[self.current_location[0]][self.current_location[1]])
        if bombs != 0:
            return

        for letter in letter_directions.keys():
            self.find_zero_area(letter)

    def find_zero_area(self, mov_letter):

        # check if already done
        try:
            if self.safe_squares[self.current_location[0] + letter_directions[mov_letter][0]][self.current_location[1] + letter_directions[mov_letter][1]] == '0':
                return
        except:
            return;

        # check for edges
        current_loc = self.current_location

        # check that it's not moving into a guaranteed bomb
        next_loc = (current_loc[0] + letter_directions[mov_letter][0], current_loc[1] + letter_directions[mov_letter][1])
        if not self.is_valid_coords(next_loc):
            return
        if self.num_bombs[next_loc[0]][next_loc[1]] == 'b':
            return

        bombs = self.mov(mov_letter)

        if bombs > 0:
            # Check surrounding for known bombs ('b'), if we know all the bombs we can go in all the other directions
            known_bombs = 0
            unknown_bombs = []
            directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
            for dir in directions:
                check_loc = (self.current_location[0] + dir[0], self.current_location[1] + dir[1])
                if self.is_valid_coords(check_loc) and self.num_bombs[check_loc[0]][check_loc[1]] == 'b':
                    known_bombs += 1
                elif self.is_valid_coords(check_loc) and self.num_bombs[check_loc[0]][check_loc[1]] == '?':
                    unknown_bombs.append(check_loc)
            if known_bombs + len(unknown_bombs) == bombs:
                for bomb_loc in unknown_bombs:
                    self.num_bombs[bomb_loc[0]][bomb_loc[1]] = 'b'
                for letter in letter_directions.keys():
                    self.find_zero_area(letter)
            else:
                self.mov(opposite_letters[mov_letter])
                return
        if current_loc == self.current_location:
            return
        for letter in letter_directions.keys():
            self.find_zero_area(letter)
        self.mov(opposite_letters[mov_letter])

    def start_find_zero_area_v2(self):
        self.visited_v2 = [self.current_location]
        self.manhattan = abs(self.current_location[0] - self.flag[0]) + abs(self.current_location[1] - self.flag[1])
        bombs = int(self.num_bombs[self.current_location[0]][self.current_location[1]])

        if bombs == 0:
            for letter in letter_directions.keys():
                check_loc = (self.current_location[0] + letter_directions[letter][0], self.current_location[1] + letter_directions[letter][1])
                if self.is_valid_coords(check_loc):
                    self.find_zero_area_v2(letter)
        else:
            known_bombs = 0
            possible_bombs = []
            directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
            for dir in directions:
                check_loc = (self.current_location[0] + dir[0], self.current_location[1] + dir[1])
                if self.is_valid_coords(check_loc) and self.num_bombs[check_loc[0]][check_loc[1]] == 'b':
                    known_bombs += 1
                elif self.is_valid_coords(check_loc) and self.num_bombs[check_loc[0]][check_loc[1]] == '?':
                    possible_bombs.append(check_loc)
            if known_bombs + len(possible_bombs) == bombs:
                known_bombs = bombs
                for bomb_loc in possible_bombs:
                    self.num_bombs[bomb_loc[0]][bomb_loc[1]] = 'b'
            if known_bombs == bombs:
                for letter in letter_directions.keys():
                    check_loc = (self.current_location[0] + letter_directions[letter][0], self.current_location[1] + letter_directions[letter][1])
                    if not check_loc in self.visited_v2 and self.is_close_coords(check_loc, self.manhattan, self.leniency) and self.num_bombs[check_loc[0]][check_loc[1]] != 'b':
                        self.find_zero_area_v2(letter)
            else:
                for letter in letter_directions.keys():
                    check_loc = (self.current_location[0] + letter_directions[letter][0], self.current_location[1] + letter_directions[letter][1])
                    if not check_loc in self.visited_v2 and self.is_close_coords(check_loc, self.manhattan, self.leniency) and self.safe_squares[check_loc[0]][check_loc[1]] == '0':
                        self.find_zero_area_v2(letter)

    def find_zero_area_v2(self, mov_letter):
        bombs = self.mov(mov_letter)
        #prospect_loc = (self.current_location[0] + letter_directions[mov_letter][0], self.current_location[1] + letter_directions[mov_letter][1])

        cur_manhattan = abs(self.current_location[0] - self.flag[0]) + abs(self.current_location[1] - self.flag[1])
        self.manhattan = min(self.manhattan, cur_manhattan)

        self.visited_v2.append(self.current_location)

        if bombs == 0:
            for letter in letter_directions.keys():
                check_loc = (self.current_location[0] + letter_directions[letter][0], self.current_location[1] + letter_directions[letter][1])
                if not check_loc in self.visited_v2 and self.is_close_coords(check_loc, self.manhattan, self.leniency):
                    self.find_zero_area_v2(letter)
        else:
            known_bombs = 0
            possible_bombs = []
            directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
            for dir in directions:
                check_loc = (self.current_location[0] + dir[0], self.current_location[1] + dir[1])
                if self.is_valid_coords(check_loc) and self.num_bombs[check_loc[0]][check_loc[1]] == 'b':
                    known_bombs += 1
                elif self.is_valid_coords(check_loc) and self.num_bombs[check_loc[0]][check_loc[1]] == '?':
                    possible_bombs.append(check_loc)
            if known_bombs + len(possible_bombs) == bombs:
                known_bombs = bombs
                for bomb_loc in possible_bombs:
                    self.num_bombs[bomb_loc[0]][bomb_loc[1]] = 'b'
            if known_bombs == bombs:
                for letter in letter_directions.keys():
                    check_loc = (self.current_location[0] + letter_directions[letter][0], self.current_location[1] + letter_directions[letter][1])
                    if not check_loc in self.visited_v2 and self.is_close_coords(check_loc, self.manhattan, self.leniency) and self.num_bombs[check_loc[0]][check_loc[1]] != 'b':
                        self.find_zero_area_v2(letter)
            else:
                for letter in letter_directions.keys():
                    check_loc = (self.current_location[0] + letter_directions[letter][0], self.current_location[1] + letter_directions[letter][1])
                    if not check_loc in self.visited_v2 and self.is_close_coords(check_loc, self.manhattan, self.leniency) and self.safe_squares[check_loc[0]][check_loc[1]] == '0':
                        self.find_zero_area_v2(letter)

        self.mov(opposite_letters[mov_letter])



    def sudoku_bombs(self):
        for i in range(2031, self.min_x-1, -3):
            for j in range(0, self.max_y+1, 3):
                visited_squares = 0
                already_found_bomb = False
                for x in range(3):
                    for y in range(3):
                        if self.safe_squares[i + x][j + y] == '0':
                            visited_squares += 1
                        if self.num_bombs[i + x][j + y] == 'b':
                            already_found_bomb = True
                if visited_squares == 8 and not already_found_bomb:
                    the_bomb_x, the_bomb_y = 0, 0
                    for x in range(3):
                        for y in range(3):
                            if self.safe_squares[i + x][j + y] == '1':
                                the_bomb_x, the_bomb_y = i+x, j+y
                    self.num_bombs[the_bomb_x][the_bomb_y] = 'b'

    def find_closest_to_flag(self):
        min_squared_distance = (self.flag[0]-2033)**2 + self.flag[1]**2
        closest_coords = (2033, 0)
        for i in range(2033, self.min_x, -1):
            for j in range(self.max_y):
                if self.safe_squares[i][j] == '0':
                    cur_distance = (self.flag[0] - i)**2 + (self.flag[1] - j)**2
                    if cur_distance < min_squared_distance:
                        closest_coords = (i, j)
                        min_squared_distance = cur_distance
        return closest_coords

    def move_to(self, target_coords):
        h = []
        counter = 0
        visited = []

        for letter in letter_directions.keys():
            check_loc = (self.current_location[0] + letter_directions[letter][0], self.current_location[1] + letter_directions[letter][1])
            distance_to = (target_coords[0]-check_loc[0])**2 + (target_coords[1]-check_loc[1])**2
            heappush(h, (distance_to, counter, check_loc, letter))
            counter += 1

        while h:
            (dist, c, cur_loc, path) = heappop(h)

            if cur_loc == target_coords:
                logging.debug("Path: " + path)
                return path
            if not self.is_valid_coords(cur_loc) or self.safe_squares[cur_loc[0]][cur_loc[1]] == '1' or cur_loc in visited:
                continue

            visited.append(cur_loc)
            for letter in letter_directions.keys():
                check_loc = (cur_loc[0] + letter_directions[letter][0], cur_loc[1] + letter_directions[letter][1])
                distance_to = (target_coords[0]-check_loc[0])**2 + (target_coords[1]-check_loc[1])**2
                heappush(h, (distance_to, counter, check_loc, path + letter))
                counter += 1
        logging.debug("No found path")
        return ""

    def follow_instructions(self, path):
        for char in path:
            self.mov(char)

    def is_valid_coords(self, coords):
        if coords[0] < self.min_x or coords[0] > 2033 or coords[1] < 0 or coords[1] > self.max_y:
            return False
        return True

    def is_close_coords(self, coords, distance, leniency):
        manhattan = abs(coords[0] - self.flag[0]) + abs(coords[1] - self.flag[1])
        if self.is_valid_coords(coords) and (manhattan <= distance + leniency):
            return True
        return False

    def return_to_start(self):
        path = self.move_to((2033,0))
        self.follow_instructions(path)














remote = remote_maze()

print(remote.get_flag_location())
print(remote.get_current_location())
#remote.start_find_zero_area()
print(remote.get_current_location())
remote.pretty_print_safe()

while True:
    try:
        i = input(">>> ").strip()
        if i == 'z':
            remote.start_find_zero_area()
        elif i == 'u':
            remote.start_find_zero_area_v2()
        elif i == 'y':
            remote.sudoku_bombs()
        elif i == 'f':
            coords = remote.find_closest_to_flag()
            print("Closest coordinates:", coords)
        elif i == 'v':
            coords = remote.find_closest_to_flag()
            path = remote.move_to(coords)
            remote.follow_instructions(path)
            print("Moved to closest: ", remote.current_location)
        elif i == 'c':
            remote.start_find_zero_area_v2()
            coords = remote.find_closest_to_flag()
            path = remote.move_to(coords)
            remote.follow_instructions(path)
            remote.sudoku_bombs()
        elif i == 'x':
            remote.pretty_print_bombs()
        elif i == '3':
            remote.three_print_bombs()
        elif i == 'e':
            code = input("Code: ")
            try:
                print(str(eval(code)))
            except Exception as e:
                print("Exception: " + str(e))
        elif i.startswith("m"):
            letter = i[1]
            newpos = remote.current_location[0] + letter_directions[letter][0], remote.current_location[1] + letter_directions[letter][1]
            remote.num_bombs[newpos[0]][newpos[1]] = "b"
            remote.pretty_print_bombs()
        elif i.startswith("p"):
            path = i[1:]
            remote.follow_instructions(path)
        elif i.startswith("g"):
            target = i[1:]
            coords = tuple(map(int, target.split(',')))
            remote.move_to(coords)
        else:
            print("Nearby bombs: " + str(remote.mov(i)))
            print("Loc: " + str(remote.get_current_location()))
            remote.pretty_print_bombs()
    except Exception as e:
        print("An error occurred: " + str(e))
