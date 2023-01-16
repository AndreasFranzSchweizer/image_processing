# Import statistics Library
import statistics

def get_2d_pixel_list(width, height, raw):
    pixel = []

    for column in range(int(height)):
        pixel.append(raw[column*int(width):(column+1)*int(width)])

    return pixel


def get_raw_from_pixel_map(pixel):
    raw = []
    for line in pixel:
        raw.extend(line)

    return raw


def mean_filter(pixel):
    for line in range(1, len(pixel)-1):
        for index in range(1, len(pixel[line])-1):
            pixel[line][index] = \
                statistics.mean([\
                pixel[line-1][index-1],\
                pixel[line-1][index],\
                pixel[line-1][index+1],\
                pixel[line][index-1],\
                pixel[line][index],\
                pixel[line][index+1],\
                pixel[line+1][index-1],\
                pixel[line+1][index],\
                pixel[line+1][index+1]])

    return pixel


def median_filter(pixel):
    for line in range(1, len(pixel)-1):
        for index in range(1, len(pixel[line])-1):
            pixel[line][index] = \
                statistics.median([\
                pixel[line-1][index-1],\
                pixel[line-1][index],\
                pixel[line-1][index+1],\
                pixel[line][index-1],\
                pixel[line][index],\
                pixel[line][index+1],\
                pixel[line+1][index-1],\
                pixel[line+1][index],\
                pixel[line+1][index+1]])

    return pixel


def edge_filter(pixel):
    for line in range(1, len(pixel)-1):
        for index in range(1, len(pixel[line])-1):
            scale = 0.45
            pixel[line][index] = \
                scale*-1 * pixel[line-1][index-1]+\
                scale*0 * pixel[line-1][index]+\
                scale*1 * pixel[line-1][index+1]+\
                scale*-2 * pixel[line][index-1]+\
                scale*0 * pixel[line][index]+\
                scale*2 * pixel[line][index+1]+\
                scale*-1 * pixel[line+1][index-1]+\
                scale*0 * pixel[line+1][index]+\
                scale*1 * pixel[line+1][index+1]

    return pixel