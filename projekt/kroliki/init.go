package main

import (
	"flag"
)

func initialiaze() {
	// oldGridX := c.gridX
	// oldGridY := c.gridY
	// oldBunny := c.initialBunny
	// oldGrass := c.initialGrass
	// oldFox := c.initialFox

	flag.IntVar(&c.gridX, "gridX", c.gridX, "Grid width")
	flag.IntVar(&c.gridY, "gridY", c.gridY, "Grid height")
	flag.IntVar(&c.initialBunny, "initialBunny", c.initialBunny, "Initial number of bunnies")
	flag.IntVar(&c.initialGrass, "initialGrass", c.initialGrass, "Initial amount of grass")
	flag.IntVar(&c.initialFox, "initialFox", c.initialFox, "Initial number of foxes")

	flag.IntVar(&c.bunnyStart, "bunnyStart", c.bunnyStart, "Bunny start power")
	flag.IntVar(&c.bunnyFood, "bunnyFood", c.bunnyFood, "Bunny food amount")
	flag.IntVar(&c.bunnyCooldown, "bunnyCooldown", c.bunnyCooldown, "Bunny cooldown")
	flag.IntVar(&c.bunnyFed, "bunnyFed", c.bunnyFed, "Bunny fed threshold")
	flag.IntVar(&c.bunnyChildren, "bunnyChildren", c.bunnyChildren, "Number of bunny children per birth")
	flag.IntVar(&c.bunnyLiveLength, "bunnyLiveLength", c.bunnyLiveLength, "Number of turns that bunny lives")

	flag.IntVar(&c.foxStart, "foxStart", c.foxStart, "Fox start power")
	flag.IntVar(&c.foxFood, "foxFood", c.foxFood, "Fox food amount")
	flag.IntVar(&c.foxCooldown, "foxCooldown", c.foxCooldown, "Fox cooldown")
	flag.IntVar(&c.foxFed, "foxFed", c.foxFed, "Fox fed threshold")
	flag.IntVar(&c.foxChildren, "foxChildren", c.foxChildren, "Number of fox children per birth")
	flag.IntVar(&c.foxLiveLength, "foxLiveLength", c.foxLiveLength, "Number of turns that fox lives")

	flag.IntVar(&c.grassStart, "grassStart", c.grassStart, "Grass start age")
	flag.IntVar(&c.grassFood, "grassFood", c.grassFood, "Grass food amount")
	flag.IntVar(&c.grassCooldown, "grassCooldown", c.grassCooldown, "Grass cooldown")
	flag.IntVar(&c.grassChildren, "grassChildren", c.grassChildren, "Number of grass children per birth")
	flag.IntVar(&c.worldAmount, "worldAmount", c.worldAmount, "Number of worlds to test")
	flag.IntVar(&c.turnLimit, "turnLimit", c.turnLimit, "Turn number to end simulations at")
	flag.IntVar(&c.grassLiveLength, "grassLiveLength", c.grassLiveLength, "Number of turns that grass lives")

	flag.Parse()

	// randomSpawn()
	// if c.gridX != oldGridX || c.gridY != oldGridY || c.initialBunny != oldBunny || c.initialGrass != oldGrass || c.initialFox != oldFox {
	// 	randomSpawn()
	// } else {
	// 	staticSpawn()
	// }
}

// func randomSpawn() {
// 	amounts["bunny"] = c.initialBunny
// 	amounts["fox"] = c.initialFox
// 	amounts["grass"] = c.initialGrass
// 	if (c.initialBunny + c.initialFox + c.initialGrass) > (c.gridX * c.gridY) {
// 		panic("too many animals")
// 	} else {
// 		for i := 0; i < c.initialBunny; i++ {
// 			for {
// 				randX := rand.Int() % c.gridX
// 				randY := rand.Int() % c.gridY
// 				if grid[randX][randY] == nil {
// 					grid[randX][randY] = &Bunny{c.bunnyStart, 0, 0}
// 					break
// 				}
// 			}
// 		}
// 		for i := 0; i < c.initialFox; i++ {
// 			for {
// 				randX := rand.Int() % c.gridX
// 				randY := rand.Int() % c.gridY
// 				if grid[randX][randY] == nil {
// 					grid[randX][randY] = &Fox{c.foxStart, 0, 0}
// 					break
// 				}
// 			}
// 		}
// 		for i := 0; i < c.initialGrass; i++ {
// 			for {
// 				randX := rand.Int() % c.gridX
// 				randY := rand.Int() % c.gridY
// 				if grid[randX][randY] == nil {
// 					grid[randX][randY] = &Grass{c.grassStart}
// 					break
// 				}
// 			}
// 		}
// 	}
// }

// func staticSpawn() {
// 	grid[1][1] = &Grass{c.grassStart}
// 	grid[2][2] = &Grass{c.grassStart}
// 	grid[5][5] = &Grass{c.grassStart}
// 	grid[6][3] = &Grass{c.grassStart}
// 	grid[10][10] = &Grass{c.grassStart}

// 	grid[3][3] = &Bunny{c.bunnyStart, 0, 0}
// 	grid[7][6] = &Bunny{c.bunnyStart, 0, 0}
// 	grid[8][2] = &Bunny{c.bunnyStart, 0, 0}
// 	grid[11][7] = &Bunny{c.bunnyStart, 0, 0}
// 	grid[4][3] = &Bunny{c.bunnyStart, 0, 0}
// 	grid[8][6] = &Bunny{c.bunnyStart, 0, 0}
// 	grid[9][2] = &Bunny{c.bunnyStart, 0, 0}
// 	grid[13][7] = &Bunny{c.bunnyStart, 0, 0}

// 	grid[4][4] = &Fox{c.foxStart, 0, 0}
// 	grid[6][6] = &Fox{c.foxStart, 0, 0}
// 	grid[9][1] = &Fox{c.foxStart, 0, 0}
// 	grid[13][8] = &Fox{c.foxStart, 0, 0}

// }

// func createGrid(x, y int) [][]Organism {
// 	grid := make([][]Organism, x)
// 	for i := range grid {
// 		grid[i] = make([]Organism, y)
// 	}
// 	return grid
// }
