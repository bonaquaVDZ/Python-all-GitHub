var_1 = 100


def main():
    penthouse(200, 200, 30, 25)   # None


def penthouse(x, y, width, height):
    """ Here we can comment on our function. It is necessary to describe
    the function, because it will be helpful for somebody,
    who will work with this document in the future and
    also that could be helpful for you to comprehend, what did you
    write down here.   """
    paint_walls(x, y, width, height // 2)
    paint_roof(x, y, width, height // 2)
    w_height = height // 6
    w_width = width // 3
    paint_window(x + w_width, y + w_height, w_width, w_height)


print(penthouse(100, 100, 20, 50))

if __name__ == '__main__':
    main()
