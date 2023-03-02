import pygame


def init():
    pygame.init()
    win = pygame.display.set_mode((400, 400))


def getKey(keyName):
    ans = False
    for eve in pygame.event.get(): pass
    key_input = pygame.key.get_pressed()
    my_key = getattr(pygame, 'K_{}'.format(keyName))
    if key_input[my_key]:
        ans = True
    pygame.display.update()
    return ans


def main():
    if getKey("LEFT"):
        print(getKey("LEFT"))

    if getKey("RIGHT"):
        print(getKey("RIGHT"))

    if getKey("UP"):
        print(getKey("UP"))
    if getKey("DOWN"):
        print(getKey("DOWN"))
    if getKey("w"):
        print(getKey("w"))
    if getKey("s"):
        print(getKey("s"))
    if getKey("a"):
        print(getKey("a"))
    if getKey("d"):
        print(getKey("d"))
    if getKey("q"):
        print(getKey("q"))
    if getKey("e"):
        print(getKey("e"))

    if getKey("f"):
        print("Your Tello is Ready To Detect!")
        print(getKey("f"))


if __name__ == '__main__':
    init()
    while True:
        main()
