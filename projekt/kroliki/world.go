package main

import (
	"fmt"
	rand "math/rand"

	rl "github.com/gen2brain/raylib-go/raylib"
)

type World struct {
	grid    [][]Organism
	amounts map[string]int
	turn    int
}

func (w *World) createGrid(x, y int) {
	w.grid = make([][]Organism, x)
	for i := range w.grid {
		w.grid[i] = make([]Organism, y)
	}
}

func (w *World) initialize() {
	// Inicjalizacja mapy ilości organizmów
	w.amounts = map[string]int{
		"bunny": c.initialBunny,
		"fox":   c.initialFox,
		"grass": c.initialGrass,
	}

	w.createGrid(c.gridX, c.gridY)
	w.randomSpawn()
}

func (w *World) randomSpawn() {
	total := c.initialBunny + c.initialFox + c.initialGrass
	if total > (c.gridX * c.gridY) {
		panic("too many animals")
	}

	// Bunnies
	for i := 0; i < c.initialBunny; i++ {
		for {
			randX := rand.Int() % c.gridX
			randY := rand.Int() % c.gridY
			if w.grid[randX][randY] == nil {
				w.grid[randX][randY] = &Bunny{power: c.bunnyStart, childCooldown: 0, turn: 0}
				break
			}
		}
	}
	// Foxes
	for i := 0; i < c.initialFox; i++ {
		for {
			randX := rand.Int() % c.gridX
			randY := rand.Int() % c.gridY
			if w.grid[randX][randY] == nil {
				w.grid[randX][randY] = &Fox{power: c.foxStart, childCooldown: 0, turn: 0}
				break
			}
		}
	}
	// Grass
	for i := 0; i < c.initialGrass; i++ {
		for {
			randX := rand.Int() % c.gridX
			randY := rand.Int() % c.gridY
			if w.grid[randX][randY] == nil {
				w.grid[randX][randY] = &Grass{childCooldown: c.grassCooldown}
				break
			}
		}
	}
}

func (w *World) makeTurn() {
	w.turn++

	for x, row := range w.grid {
		for y, organism := range row {
			if organism != nil {
				organism.update()
				if !organism.alive() {
					w.amounts[organism.getName()]--
					w.grid[x][y] = nil
					continue
				}
				if organism.getTurn() == w.turn {
					continue
				} else {
					organism.setTurn(w.turn)
				}
			} else {
				continue
			}

			if animal, ok := organism.(Animal); ok {
				free, danger, ally, food := w.checkTiles(x, y, animal)

				// Ucieczka od zagrożeń
				if len(danger) != 0 {
					moved := false
					for _, el := range danger {
						newX := x + (el.x * -1)
						newY := y + (el.y * -1)
						if w.isOnGrid(newX, newY) && w.grid[newX][newY] == nil {
							w.grid[newX][newY] = w.grid[x][y]
							w.grid[x][y] = nil
							moved = true
							break
						}
					}
					if moved {
						continue
					}
				}

				// Rozmnażanie
				if len(ally) > 0 && animal.getChildCooldown() <= 0 && len(free) > 0 && animal.isFed() {
					mate := ally[rand.Int()%len(ally)]
					// target := free[rand.Int()%len(free)]
					// w.grid[x+target.x][y+target.y] = animal.makeChild()
					mate.setChildCooldown()
					animal.setChildCooldown()
					rand.Shuffle(len(free), func(i, j int) { free[i], free[j] = free[j], free[i] })
					for i := 0; i < organism.getNumOfChildren() && i < len(free); i++ {
						pos := free[i]
						w.grid[x+pos.x][y+pos.y] = organism.makeChild()
						w.amounts[organism.getName()]++
					}
					organism.setChildCooldown()

				} else if len(food) > 0 { // Jedzenie
					target := food[rand.Int()%len(food)]
					w.grid[x+target.x][y+target.y].whenEaten(animal)
					if !w.grid[x+target.x][y+target.y].alive() {
						w.amounts[w.grid[x+target.x][y+target.y].getName()]--
						w.grid[x+target.x][y+target.y] = nil
					}

				} else if len(free) > 0 { // Ruch na wolne pole
					target := free[rand.Int()%len(free)]
					w.grid[x+target.x][y+target.y] = w.grid[x][y]
					w.grid[x][y] = nil
				}
			} else {
				if organism.getChildCooldown() <= 0 {
					free := w.getFreeTiles(x, y)
					rand.Shuffle(len(free), func(i, j int) { free[i], free[j] = free[j], free[i] })
					for i := 0; i < c.grassChildren && i < len(free); i++ {
						pos := free[i]
						w.grid[x+pos.x][y+pos.y] = organism.makeChild()
						w.amounts[organism.getName()]++
					}
					organism.setChildCooldown()
				}

			}
		}
	}
}

func (w *World) checkTiles(x int, y int, me Animal) ([]pos, []pos, []Animal, []pos) {
	free := make([]pos, 0, 8)
	danger := make([]pos, 0, 8)
	ally := make([]Animal, 0, 8)
	food := make([]pos, 0, 8)

	for rx := -1; rx <= 1; rx++ {
		for ry := -1; ry <= 1; ry++ {
			if (rx == 0 && ry == 0) || !w.isOnGrid(x+rx, y+ry) {
				continue
			}

			if w.grid[x+rx][y+ry] == nil {
				free = append(free, pos{rx, ry})
			} else {
				org := w.grid[x+rx][y+ry]
				if animal, ok := org.(Animal); ok {
					if animal.willEat(me) {
						danger = append(danger, pos{rx, ry})
					}
					if me.getName() == animal.getName() && animal.getChildCooldown() <= 0 && animal.isFed() {
						ally = append(ally, animal)
					}
				}
				if me.willEat(org) {
					food = append(food, pos{rx, ry})
				}
			}
		}
	}

	return free, danger, ally, food
}

func (w *World) getFreeTiles(x int, y int) []pos {
	free := make([]pos, 0, 8)

	for rx := -1; rx <= 1; rx++ {
		for ry := -1; ry <= 1; ry++ {
			if (rx == 0 && ry == 0) || !w.isOnGrid(x+rx, y+ry) {
				continue
			}

			if w.grid[x+rx][y+ry] == nil {
				free = append(free, pos{rx, ry})
			}
		}
	}

	return free
}

func (w *World) drawGrid(tileSize int) {
	for x, row := range w.grid {
		for y, organism := range row {
			posX := int32(x * tileSize)
			posY := int32(y * tileSize)
			rect := rl.NewRectangle(float32(posX), float32(posY), float32(tileSize), float32(tileSize))

			var color rl.Color
			if organism != nil {
				color = colorForName(organism.getName())
			} else {
				color = rl.LightGray
			}

			rl.DrawRectangleRec(rect, color)
			rl.DrawRectangleLines(posX, posY, int32(tileSize), int32(tileSize), rl.Black)
		}
	}

	y := int32(580)
	order := []string{"grass", "bunny", "fox"}
	for _, name := range order {
		text := fmt.Sprintf("%s: %d", name, w.amounts[name])
		rl.DrawText(text, 20, y, 20, rl.Black)
		y -= 30
	}
}

func (w *World) isOnGrid(x, y int) bool {
	return x >= 0 && x < c.gridX && y >= 0 && y < c.gridY
}

func colorForName(name string) rl.Color {
	switch name {
	case "grass":
		return rl.Green
	case "bunny":
		return rl.Brown
	case "fox":
		return rl.Orange
	default:
		return rl.Gray
	}
}
