def main():
    total = 0
    grid = []
    with open("input.txt", "r") as input:
        for line in input:
            grid.append(line.strip())

    # note: x and y are reversed from more usual euclidian representation
    for x in range(len(grid)):
        for y in range(len(grid[x])):
            if grid[x][y] == "X":
                # basically do all combos of x and y directions
                # in a convoluted way to avoid extra code for no
                # good reason
                x_dir = -1
                y_dir = -1
                while True:
                    if x_dir == 2:
                        x_dir = -1
                        y_dir += 1
                    if y_dir == 2:
                        break
                    coordinates = (x, y)
                    is_found = True
                    for letter in "MAS":
                        # something I could never do in school or work
                        coordinates = (coordinates[0] + x_dir, coordinates[1] + y_dir)
                        if (
                            coordinates[0] < 0
                            or coordinates[1] < 0
                            or coordinates[0] >= len(grid)
                            or coordinates[1] >= len(grid[x])
                            or grid[coordinates[0]][coordinates[1]] != letter
                        ):
                            is_found = False
                            break
                    if is_found:
                        total += 1
                    x_dir += 1

    print(f"Part 1 answer: {total}")


if __name__ == "__main__":
    main()
