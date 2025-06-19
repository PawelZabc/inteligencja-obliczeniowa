package main

type Fox struct {
	power         int
	childCooldown int
	turn          int
	age           int
}

func (f *Fox) getChildCooldown() int {
	return f.childCooldown
}

func (f *Fox) getNumOfChildren() int {
	return c.foxChildren
}

func (f *Fox) whenEaten(animal Animal) {
	f.power = 0
	animal.addPower(c.foxFood)
}

func (f *Fox) isFed() bool {
	return (f.power >= c.foxFed)
}

func (f *Fox) setChildCooldown() {
	f.childCooldown = c.foxCooldown
}
func (f *Fox) getTurn() int {
	return f.turn
}

func (f *Fox) setTurn(turn int) {
	f.turn = turn
}

func (f *Fox) addPower(amount int) {
	f.power += amount
}

func (f *Fox) getName() string {
	return "fox"
}

func (f *Fox) update() {
	f.power -= 1
	f.age++
	if f.childCooldown > 0 {
		f.childCooldown -= 1
	}
}

func (f *Fox) alive() bool {
	return (f.power > 0 && f.age < c.foxLiveLength)
}

func (f *Fox) makeChild() Organism {
	return &Fox{c.foxStart, c.foxCooldown, f.turn, 0}
}

func (f *Fox) willEat(org Organism) bool {
	return (org.getName() == "bunny")
}
