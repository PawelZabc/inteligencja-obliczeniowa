package main

type Grass struct {
	childCooldown int
	turn          int
	dead          bool
	age           int
}

func (g *Grass) getName() string {
	return "grass"
}

func (g *Grass) getNumOfChildren() int {
	return c.grassLiveLength
}

func (g *Grass) getChildCooldown() int {
	return g.childCooldown
}

func (g *Grass) getTurn() int {
	return g.turn
}

func (g *Grass) setTurn(turn int) {
	g.turn = turn
}

func (g *Grass) setChildCooldown() {
	g.childCooldown = c.grassCooldown
}

func (g *Grass) alive() bool {
	return (!g.dead && g.age < c.grassLiveLength)
}

func (g *Grass) makeChild() Organism {
	return &Grass{childCooldown: c.grassCooldown, turn: g.turn}
}

func (g *Grass) update() {
	g.age++
	g.childCooldown -= 1
}

func (g *Grass) whenEaten(animal Animal) {
	g.dead = true
	animal.addPower(c.grassFood)
}
