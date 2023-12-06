package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
)

var RED = 12
var GREEN = 13
var BLUE = 14
var total = 0
var total2 = 0

func main() {
	content, _ := os.ReadFile("input.txt")
	input := string(content)
	lines := strings.Split(input, "\n")
	for _, s := range lines {
		isValid := true
		parts := strings.Split(s, ":")
		game, line := parts[0], parts[1]
		game_num, _ := strconv.Atoi(strings.Split(game, " ")[1])
		greatest_red := 0
		greatest_blue := 0
		greatest_green := 0
		for _, round := range strings.Split(line, ";") {
			for _, draw := range strings.Split(round, ",") {
				draw_parts := strings.Split(draw, " ")
				color := draw_parts[2]
				value, _ := strconv.Atoi(draw_parts[1])
				switch color {
				case "red":
					if value > RED {
						isValid = false
					}
					if greatest_red < value {
						greatest_red = value
					}
				case "blue":
					if value > BLUE {
						isValid = false
					}
					if greatest_blue < value {
						greatest_blue = value
					}
				case "green":
					if value > GREEN {
						isValid = false
					}
					if greatest_green < value {
						greatest_green = value
					}
				}
			}
		}

		if isValid {
			total += game_num
		}
		total2 += greatest_red * greatest_blue * greatest_green

	}
	fmt.Println("Part 1:", total)
	fmt.Println("Part 2:", total2)
}
