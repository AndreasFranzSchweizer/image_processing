import filter

def read_image(filename):
    image = []
    with open(filename, "r") as file:
        image = file.readlines()

    image[:] = [x for x in image if not x.startswith("#")]
    
    width, height = map(int, image[1].split())

    image = image [3::]
    raw = []
    for line in image:
        for value in line.split():
            if value.strip().isnumeric():
                raw.append(int(value))

    return width,height,raw

def write_image(filename, width, height, raw):
    with open(filename, "w") as file:
        file.write("P2\n") # fileformat
        file.write(f"# {filename}\n")
        file.write(f"{width} {height}\n")
        file.write("255\n") # max grayscale

        pixel_per_line = 20
        number_of_lines = len(raw) // pixel_per_line

        for line_index in range(number_of_lines):
            line = " ".join(map(str,map(int, raw[line_index*pixel_per_line:(line_index+1)*pixel_per_line])))
            file.write(line + "\n")

        last_line = " ".join(map(str, map(int, raw[number_of_lines*pixel_per_line::])))
        file.write(last_line + "\n")




width, height, raw = read_image("surf.ascii.pgm")
write_image("test.pgm", width, height, raw)