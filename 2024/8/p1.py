def main():
    total = 0
    num_rows = 0
    row_length = 0
    # antennas with a list of coordinates
    antenna_coordinates: dict[str, list[tuple[int, int]]] = {}
    with open("input.txt", "r") as input:
        for y, line in enumerate(input):
            line = line.strip()
            for x, char in enumerate(line):
                if char != ".":
                    if char not in antenna_coordinates:
                        antenna_coordinates[char] = [(y, x)]
                    else:
                        antenna_coordinates[char].append((y, x))
            num_rows += 1
            # set every loop, whatever
            row_length = len(line)

    seen = set()
    for coordinates in antenna_coordinates.values():
        for coordinate_pair in generate_all_coord_pairs(coordinates):
            antinode_locations = calculate_antinode_locations(coordinate_pair)
            for y, x in antinode_locations:
                if (
                    y >= 0
                    and y < num_rows
                    and x >= 0
                    and x < row_length
                    and (y, x) not in seen
                ):
                    seen.add((y, x))
                    total += 1

    print(f"Part 1 answer: {total}")


def calculate_antinode_locations(
    coordinate_pair: tuple[tuple[int, int], tuple[int, int]]
) -> tuple[tuple[int, int], tuple[int, int]]:
    y_diff = coordinate_pair[0][0] - coordinate_pair[1][0]
    x_diff = coordinate_pair[0][1] - coordinate_pair[1][1]

    coord1 = (coordinate_pair[0][0] + y_diff, coordinate_pair[0][1] + x_diff)
    coord2 = (coordinate_pair[1][0] - y_diff, coordinate_pair[1][1] - x_diff)
    return (coord1, coord2)


def generate_all_coord_pairs(
    coordinates: list[tuple[int, int]]
) -> list[tuple[tuple[int, int], tuple[int, int]]]:
    pairs = []
    for i in range(len(coordinates)):
        for j in range(i + 1, len(coordinates)):
            pairs.append((coordinates[i], coordinates[j]))
    return pairs


if __name__ == "__main__":
    main()
