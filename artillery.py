import cmath
import math
import sys

class Coord:
    def __init__(self, dist, azi):
        self.azi = azi
        self.dist = dist

    @classmethod
    def fromstring(self, s):
        azi, dist = map(int, s.split(" "))
        return self(dist, azi * math.pi / 180)

    @classmethod
    def fromcomplex(self, j):
        return self(*cmath.polar(j))

    def __neg__(self):
        return Coord(self.dist, -self.azi)

    def __add__(self, other: 'Coord'):
        return Coord.fromcomplex(self.rect() + other.rect())

    def rect(self):
        return cmath.rect(self.dist, self.azi)

    def __str__(self):
        azi = self.azi * 180 / math.pi
        if azi < 0:
            azi += 360
        return f"{azi:0.0f} {self.dist:0.0f}"
        


print("Hi! It looks like you're trying to spot for artillery!")

print("Please go within binoc range of the artillery and note down its position.")

spotter_pos = -Coord.fromstring(input("Artillery position> "))

print(f"Your position is at {spotter_pos}, okay. Memorize where you are standing and advance.")

while True:
    print("If you advanced, check the coordinates of your previous position, or finalize with Enter.")
    new_input = input("Previous position> ")
    if new_input:
        spotter_pos += -Coord.fromstring(new_input)
        print(f"Your new position is {spotter_pos}")
    else:
        break

print(f"Your position is confirmed as {spotter_pos}. You may now begin calling artillery strikes. Try not to call them on yourself.")

while True:
    new_input = input("Target position> ")
    if new_input:
        target_pos = spotter_pos + Coord.fromstring(new_input)
        print(f"> {target_pos}")
    else:
        break
