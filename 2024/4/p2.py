def main():
    total = 0
    grid = []
    with open("input.txt", "r") as input:
        for line in input:
            grid.append(line.strip())

    # note: x and y are reversed from more usual euclidian representation
    for x in range(len(grid)):
        for y in range(len(grid[x])):
            if grid[x][y] == "A":
                corner_pair1 = ((x - 1, y - 1), (x + 1, y + 1))
                corner_pair2 = ((x - 1, y + 1), (x + 1, y - 1))
                if _corners_m_or_s(corner_pair1, grid) and _corners_m_or_s(
                    corner_pair2, grid
                ):
                    total += 1

    print(f"Part 2 answer: {total}")


def _corners_m_or_s(
    coordinate_pairs: tuple[tuple[int, int], tuple[int, int]], grid: list[list[str]]
) -> bool:
    """find if the coordinates correspond to an m and s pair"""
    include = ["M", "S"]
    for x, y in coordinate_pairs:
        if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[x]):
            return False
        try:
            include.remove(grid[x][y])
        except:
            return False
    # if we got here include is empty and the coordinates are M and S
    return True


if __name__ == "__main__":
    main()
