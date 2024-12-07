def main():
    grid = []
    current_coordinates = (0, 0)
    # initialize grid, records starting coordinates
    with open("input.txt", "r") as input:
        for i, line in enumerate(input):
            grid_row = []
            for j, pos in enumerate(line.strip()):
                if pos == "^":
                    current_coordinates = (i, j)
                    grid_row.append("X")
                else:
                    grid_row.append(pos)
            grid.append(grid_row)
    direction = 0
    # loop through changing dir as needed until complete
    while (
        current_coordinates[0] != 0
        and current_coordinates[1] != 0
        and current_coordinates[0] < len(grid) - 1
        and current_coordinates[1] < len(grid[current_coordinates[0]]) - 1
    ):
        i_offset, j_offset = degree_to_coordinate_offset(direction)
        new_coordinates = (
            current_coordinates[0] + i_offset,
            current_coordinates[1] + j_offset,
        )
        if grid[new_coordinates[0]][new_coordinates[1]] == "#":
            direction += 90
            if direction == 360:
                direction = 0
        else:
            current_coordinates = new_coordinates
            grid[current_coordinates[0]][current_coordinates[1]] = "X"

    # beautiful
    spaces_traversed = str(grid).count("X")
    print(f"Part 1 answer: {spaces_traversed}")


def degree_to_coordinate_offset(degree: int) -> tuple[int, int]:
    if degree == 0:
        return (-1, 0)
    if degree == 90:
        return (0, 1)
    if degree == 180:
        return (1, 0)
    if degree == 270:
        return (0, -1)


if __name__ == "__main__":
    main()
