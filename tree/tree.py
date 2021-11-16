#!/usr/bin/env python3

import threading
import random
import os
import time

mutex = threading.Lock()

tree = list(open('tree2.txt').read().rstrip())


def colored_dot(color):
    if color == 'red':
        return f'\033[91m•\033[0m'
    if color == 'green':
        return f'\033[92m•\033[0m'
    if color == 'yellow':
        return f'\033[93m•\033[0m'
    if color == 'blue':
        return f'\033[94m•\033[0m'


def lights(color, indexes):
    off = True
    while True:
        for idx in indexes:
            tree[idx] = colored_dot(color) if off else '•'

        mutex.acquire()
        os.system('cls' if os.name == 'nt' else 'clear')
        print(''.join(tree))
        mutex.release()

        off = not off

        time.sleep(random.uniform(.5, 1.5))


yellow = []
red = []
green = []
blue = []

for i, c in enumerate(tree):
    if c == '★':
        tree[i] = f'\033[93m★\033[0m'
    if c == 'y':
        yellow.append(i)
        tree[i] = '•'
    if c == 'r':
        red.append(i)
        tree[i] = '•'
    if c == 'B':
        blue.append(i)
        tree[i] = '•'
    if c == '*':
        green.append(i)
        tree[i] = f'\033[92m•\033[0m'
    if c in 'mWm':
        tree[i] = f'\u001b[38;5;130m{c}\u001b[0m'
    if c in 'MERRY CHRISTMAS':
        tree[i] = f'\033[91m{c}\033[0m'


ty = threading.Thread(target=lights, args=('yellow', yellow), daemon=True)
tr = threading.Thread(target=lights, args=('red', red), daemon=True)
tb = threading.Thread(target=lights, args=('blue', blue), daemon=True)

for t in [ty, tr, tb]:
    t.start()
for t in [ty, tr, tb]:
    t.join()
