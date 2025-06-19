package main

import (
	"fmt"
	"strconv"

	rl "github.com/gen2brain/raylib-go/raylib"
)

type Organism interface {
	getName() string
	update()
	whenEaten(Animal)
	makeChild() Organism
	alive() bool
	getTurn() int
	setTurn(turn int)
	setChildCooldown()
	getChildCooldown() int
	getNumOfChildren() int
}

type Animal interface {
	Organism
	willEat(org Organism) bool
	addPower(amount int)
	isFed() bool
}

type pos struct {
	x int
	y int
}

// var amounts = map[string]int{
// 	"bunny": c.initialBunny,
// 	"fox":   c.initialFox,
// 	"grass": c.initialGrass}
// var turn int = 0

// var grid [][]Organism

func main() {
	initialiaze()
	if c.worldAmount == 1 {
		screenWidth := 800
		screenHeight := 600
		tileSize := 20

		rl.InitWindow(int32(screenWidth), int32(screenHeight), "Organism Grid")
		defer rl.CloseWindow()
		rl.SetTargetFPS(60)
		w := &World{}
		w.initialize()
		i := 0
		speed := 1
		turn := 0
		auto := false
		for !rl.WindowShouldClose() {
			if rl.IsKeyPressed(rl.KeySpace) {
				w.makeTurn()
			}
			if rl.IsKeyPressed(rl.KeyLeft) {
				if speed != 0 {
					speed--
				}
			}
			if rl.IsKeyPressed(rl.KeyRight) {
				speed++
			}
			if rl.IsKeyPressed(rl.KeyA) {
				if auto {
					auto = false
				} else {
					auto = true
				}
			}
			i++
			if auto && i >= speed && w.amounts["fox"] > 0 && w.amounts["grass"] > 0 && w.amounts["bunny"] > 0 {
				turn++
				turnString := ""
				if turn < 10 {
					turnString = "00" + strconv.Itoa(turn)
				} else if turn < 100 {
					turnString = "0" + strconv.Itoa(turn)
				} else {
					turnString = strconv.Itoa(turn)
				}

				rl.TakeScreenshot("screenshots/frame" + turnString + ".png")
				i = 0
				w.makeTurn()
			}

			rl.BeginDrawing()
			rl.ClearBackground(rl.RayWhite)

			w.drawGrid(tileSize)

			rl.EndDrawing()
		}
	} else {
		turns := make(chan int)
		sum := 0
		for i := 0; i < c.worldAmount; i++ {
			go simulate(turns)
		}

		for i := 0; i < c.worldAmount; i++ {
			sum += <-turns
		}
		fmt.Print(sum / c.worldAmount)
	}
}

func simulate(turns chan int) {
	w := &World{}
	w.initialize()
	for w.amounts["fox"] > 0 && w.amounts["grass"] > 0 && w.amounts["bunny"] > 0 && w.turn <= c.turnLimit {
		w.makeTurn()
	}
	turns <- w.turn
}

// func makeTurn() {
// 	turn++
// 	if turn%c.grassSpawnEvery == 0 {
// 		randX := rand.Int() % c.gridX
// 		randY := rand.Int() % c.gridY
// 		if grid[randX][randY] == nil {
// 			grid[randX][randY] = &Grass{1}
// 			amounts["grass"] += 1
// 		}
// 	}
// 	for x, row := range grid {
// 		for y, organism := range row {
// 			if organism != nil {
// 				organism.update()
// 				if !organism.alive() {
// 					amounts[organism.getName()] -= 1
// 					grid[x][y] = nil
// 					continue
// 				}
// 			}
// 			if animal, ok := organism.(Animal); ok {
// 				if animal.getTurn() != turn {
// 					// println(x, y)
// 					animal.setTurn(turn)
// 					free, danger, ally, food := checkTiles(x, y, animal)
// 					if len(danger) != 0 {
// 						moved := false
// 						for _, el := range danger {
// 							if isOnGrid(x+(el.x*-1), y+el.y*-1) && grid[x+(el.x*-1)][y+el.y*-1] == nil {
// 								grid[x+(el.x*-1)][y+el.y*-1] = grid[x][y]
// 								grid[x][y] = nil
// 								moved = true
// 								break
// 							}
// 						}
// 						if moved {
// 							continue
// 						}
// 					}
// 					if len(ally) > 0 && animal.getChildCooldown() <= 0 && len(free) > 0 && animal.isFed() {
// 						mate := ally[rand.Int()%len(ally)]
// 						target := free[rand.Int()%len(free)]
// 						grid[x+target.x][y+target.y] = animal.makeChild()
// 						amounts[animal.getName()] += 1
// 						mate.setChildCooldown()
// 						animal.setChildCooldown()
// 					} else if len(food) > 0 {
// 						target := food[rand.Int()%len(food)]
// 						grid[x+target.x][y+target.y].whenEaten(animal)
// 						if !grid[x+target.x][y+target.y].alive() {
// 							amounts[grid[x+target.x][y+target.y].getName()] -= 1
// 							grid[x+target.x][y+target.y] = nil
// 						}
// 					} else if len(free) != 0 {
// 						target := free[rand.Int()%len(free)]
// 						grid[x+target.x][y+target.y] = grid[x][y]
// 						grid[x][y] = nil
// 					}
// 				}
// 			}
// 		}
// 	}
// }

// func checkTiles(x int, y int, me Animal) ([]pos, []pos, []Animal, []pos) {
// 	free := make([]pos, 0, 8)
// 	danger := make([]pos, 0, 8)
// 	ally := make([]Animal, 0, 8)
// 	food := make([]pos, 0, 8)
// 	for rx := -1; rx <= 1; rx++ {
// 		for ry := -1; ry <= 1; ry++ {
// 			if (rx == 0 && ry == 0) || !isOnGrid(x+rx, y+ry) {
// 				continue
// 			}
// 			if grid[x+rx][y+ry] == nil {
// 				free = append(free, pos{rx, ry})
// 			} else {
// 				org := grid[x+rx][y+ry]
// 				if animal, ok := org.(Animal); ok {
// 					if animal.willEat(me) {
// 						danger = append(danger, pos{rx, ry})
// 					}
// 					if me.getName() == animal.getName() && animal.getChildCooldown() <= 0 && animal.isFed() {

// 						ally = append(ally, animal)
// 					}
// 				}
// 				if me.willEat(org) {
// 					food = append(food, pos{rx, ry})
// 				}
// 			}
// 		}
// 	}
// 	return free, danger, ally, food
// }

// func drawGrid(grid [][]Organism, tileSize int) {
// 	for x, row := range grid {
// 		for y, organism := range row {
// 			posX := int32(x * tileSize)
// 			posY := int32(y * tileSize)
// 			rect := rl.NewRectangle(float32(posX), float32(posY), float32(tileSize), float32(tileSize))

// 			var color rl.Color
// 			if organism != nil {
// 				color = colorForName(organism.getName())
// 			} else {
// 				color = rl.LightGray
// 			}

// 			rl.DrawRectangleRec(rect, color)
// 			rl.DrawRectangleLines(posX, posY, int32(tileSize), int32(tileSize), rl.Black)
// 		}
// 	}
// 	y := int32(580)
// 	order := []string{"grass", "bunny", "fox"}
// 	for _, name := range order {
// 		text := fmt.Sprintf("%s: %d", name, amounts[name])
// 		rl.DrawText(text, 20, y, 20, rl.Black)
// 		y -= 30
// 	}
// }

// func isOnGrid(x, y int) bool {
// 	return x >= 0 && x < c.gridX && y >= 0 && y < c.gridY
// }
