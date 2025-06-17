package main

import (
	"flag"
	"fmt"
	"math/rand"
	"strings"
	"time"
)

type OrganismType int

const (
	Grass OrganismType = iota
	Bunny
	Fox
)

type Organism struct {
	Type          OrganismType
	X, Y          int
	Power         int
	ChildCooldown int

	Fed  bool
	dead bool
	Age  int
}

type World struct {
	Grid          [][]*Organism
	Organisms     []*Organism
	Width, Height int
	Counts        [3]int
}

type Options struct {
	gridX         int
	gridY         int
	simulations   int
	initial       [3]int
	liveLength    [3]int
	childRequired [3]int

	// hungerThreshold [3]int
	// hungerDrain     [3]int
}

var p Options

func NewWorld(width, height int) *World {
	grid := make([][]*Organism, width)
	for i := range grid {
		grid[i] = make([]*Organism, height)
	}
	return &World{
		Grid:      grid,
		Width:     width,
		Height:    height,
		Organisms: make([]*Organism, 0),
	}
}

func (w *World) SpawnRandom(typ OrganismType, count int, startPower int) {
	for count > 0 {
		x := rand.Intn(w.Width)
		y := rand.Intn(w.Height)
		if w.Grid[x][y] == nil {
			org := &Organism{Type: typ, X: x, Y: y, Power: startPower}
			w.Grid[x][y] = org
			w.Organisms = append(w.Organisms, org)
			count--
			w.Counts[typ]++
		}
	}
}

func (w *World) String() string {
	var sb strings.Builder
	for y := 0; y < w.Height; y++ {
		for x := 0; x < w.Width; x++ {
			org := w.Grid[x][y]
			if org == nil {
				sb.WriteString(".") // puste pole
			} else {
				switch org.Type {
				case Grass:
					sb.WriteString("G")
				case Bunny:
					sb.WriteString("B")
				case Fox:
					sb.WriteString("F")
				default:
					sb.WriteString("?")
				}
			}
		}
		sb.WriteString("\n")
	}
	return sb.String()
}

func (w *World) Action(org *Organism) {

	dirs := []struct{ x, y int }{
		{-1, -1}, {-1, 0}, {-1, 1},
		{0, -1}, {0, 1},
		{1, -1}, {1, 0}, {1, 1},
	}
	rand.Shuffle(len(dirs), func(i, j int) { dirs[i], dirs[j] = dirs[j], dirs[i] })

	for _, d := range dirs {
		x := org.X + d.x
		y := org.Y + d.y

		if !w.isOnWorld(x, y) {
			continue
		}

		target := w.Grid[x][y]

		if org.Type == Grass {
			// println(target == nil, org.Power, p.childRequired[Grass])
			if target == nil && org.Power > p.childRequired[Grass] {
				child := &Organism{Type: Grass, X: x, Y: y, Power: 10, ChildCooldown: 5}
				w.Grid[x][y] = child
				w.Counts[Grass]++
				org.Power -= 3
				return
			}
			continue
		}

		if target != nil && target.Type == org.Type-1 {
			target.dead = true
			w.Counts[target.Type]--
			org.Power += 5 // może warto zależnie od rodzaju
			w.Grid[x][y] = nil
			return
		}

		if target == nil && org.Power > p.childRequired[org.Type] {
			child := &Organism{
				Type:          org.Type,
				X:             x,
				Y:             y,
				Power:         org.Power / 2,
				ChildCooldown: 5,
			}
			org.Power /= 2
			org.ChildCooldown = 5
			w.Organisms = append(w.Organisms, child)
			w.Grid[x][y] = child
			w.Counts[org.Type]++
			// org.Power -= 3
			return
		}

		if target == nil {
			w.Grid[org.X][org.Y] = nil
			w.Grid[x][y] = org
			org.X, org.Y = x, y
			return
		}
	}
}

func removeDeadOrganisms(organisms []*Organism) []*Organism {
	live := organisms[:0] // reuse the same underlying array
	for _, org := range organisms {
		if !org.dead {
			live = append(live, org)
		}
	}
	return live
}

func (w *World) cleanUp() {
	w.Organisms = removeDeadOrganisms(w.Organisms)
}

func (w *World) isOnWorld(x, y int) bool {
	return x >= 0 && x < w.Width && y >= 0 && y < w.Height
}

func (w *World) Update() {
	length := len(w.Organisms)
	for i := 0; i < length; i++ {
		org := w.Organisms[i]
		if org.dead {
			continue
		}
		if org.ChildCooldown > 0 {
			org.ChildCooldown--
		}
		org.Age++
		if org.Type == Grass {
			org.Power++
		}
		if org.Age > p.liveLength[org.Type] {
			org.dead = true
			w.Counts[org.Type]--
			w.Grid[org.X][org.Y] = nil
		} else {
			w.Action(org)
		}

	}
	w.cleanUp()
}

func symulacja(done chan<- int) {
	rand.Seed(time.Now().UnixNano())

	world := NewWorld(p.gridX, p.gridY)

	world.SpawnRandom(Grass, p.initial[Grass], 3)
	world.SpawnRandom(Bunny, p.initial[Bunny], 20)
	world.SpawnRandom(Fox, p.initial[Fox], 40)

	i := 0
	for world.Counts[0] > 0 && world.Counts[1] > 0 && world.Counts[2] > 0 && i < 500 {
		world.Update()
		i++
	}
	done <- i
}

func main() {
	// Definicja flag
	gridX := flag.Int("gridX", 20, "width of the world grid")
	gridY := flag.Int("gridY", 20, "height of the world grid")
	initialGrass := flag.Int("initialGrass", 50, "initial grass count")
	initialBunny := flag.Int("initialBunny", 20, "initial bunny count")
	initialFox := flag.Int("initialFox", 10, "initial fox count")
	llGrass := flag.Int("llGrass", 5, "lifetime for grass")
	llBunny := flag.Int("llBunny", 10, "lifetime for bunny")
	llFox := flag.Int("llFox", 20, "lifetime for fox")

	simulations := flag.Int("simulations", 100, "number of simulations to get an average out of")

	flag.Parse()
	p = Options{*gridX, *gridY, *simulations, [3]int{*initialGrass, *initialBunny, *initialFox}, [3]int{*llGrass, *llBunny, *llFox}, [3]int{5, 10, 20}}

	done := make(chan int)
	for i := 0; i < p.simulations; i++ {
		go symulacja(done)
	}

	sum := 0
	for i := 0; i < p.simulations; i++ {
		sum += <-done
		// fmt.Println("Symulacja", sum, "zakończona")
	}
	result := sum / p.simulations
	fmt.Println(result)

}
