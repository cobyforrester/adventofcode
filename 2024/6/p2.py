import copy


def main():
    total = 0
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
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if is_inf_loop(current_coordinates, grid, (i, j)):
                total += 1
    print(f"Part 2 answer: {total}")


def is_inf_loop(
    current_coordinates: tuple[int, int],
    grid: list[list[str]],
    obstruction_coords: tuple[int, int],
):
    direction = 0
    grid = copy.deepcopy(grid)
    while (
        current_coordinates[0] != 0
        and current_coordinates[1] != 0
        and current_coordinates[0] < len(grid) - 1
        and current_coordinates[1] < len(grid[current_coordinates[0]]) - 1
    ):
        i_offset, j_offset = _degree_to_coordinate_offset(direction)
        new_coordinates = (
            current_coordinates[0] + i_offset,
            current_coordinates[1] + j_offset,
        )
        if (
            grid[new_coordinates[0]][new_coordinates[1]] == "#"
            or new_coordinates == obstruction_coords
        ):
            direction += 90
            if direction == 360:
                direction = 0
        else:
            current_coordinates = new_coordinates
            new_val = grid[current_coordinates[0]][current_coordinates[1]]
            if type(new_val) == str:
                grid[current_coordinates[0]][current_coordinates[1]] = set()
            elif direction in new_val:
                return True
            else:
                grid[current_coordinates[0]][current_coordinates[1]].add(direction)
    return False


def _degree_to_coordinate_offset(degree: int) -> tuple[int, int]:
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
