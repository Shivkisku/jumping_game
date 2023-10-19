SCREEN_WIDTH  = 1000
SCREEN_HEIGHT =  600
SCREEN_SIZE   = (SCREEN_WIDTH, SCREEN_HEIGHT)

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE  = (0, 0, 255)
GREEN = (0, 255, 0)
RED   = (255, 0, 0)

LOWER_BLOCK = {'NAME': 'Lower', 'COLOR': BLUE}
UPPER_BLOCK = {'NAME': 'upper', 'COLOR': RED}
COUNT_C = GREEN
LEVEL_C = GREEN

B_MIN_DISTANCE = 100

LEVEL1 = {'NAME': 'Level 1', 'MOVE_X': -3, 'BLOCK_FREQUENCY': [4, 5, 500]}
LEVEL2 = {'NAME': 'Level 2', 'MOVE_X': -5, 'BLOCK_FREQUENCY': [4, 5, 500]}
LEVEL3 = {'NAME': 'Level 3', 'MOVE_X': -5, 'BLOCK_FREQUENCY': [16, 20, 500]}
LEVEL4 = {'NAME': 'Level 4', 'MOVE_X': -8, 'BLOCK_FREQUENCY': [8, 10, 500]}
LEVEL5 = {'NAME': 'Level 5', 'MOVE_X': -8, 'BLOCK_FREQUENCY': [16, 20, 500]}

LEVEL = [LEVEL1, LEVEL2, LEVEL3, LEVEL4, LEVEL5]
CH_LEVEL = [10, 30, 50, 80]

MOVE_UP = -SCREEN_HEIGHT // 30
MOVE_DOWN = SCREEN_HEIGHT // 60
