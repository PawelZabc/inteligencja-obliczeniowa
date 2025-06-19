package main

type Bunny struct {
	power         int
	childCooldown int
	turn          int
	age           int
}

func (b *Bunny) whenEaten(animal Animal) {
	b.power = 0
	animal.addPower(c.bunnyFood)
}

func (b *Bunny) getNumOfChildren() int {
	return c.bunnyChildren
}

func (b *Bunny) getChildCooldown() int {
	return b.childCooldown
}
func (b *Bunny) setChildCooldown() {
	b.childCooldown = c.bunnyCooldown
}

func (b *Bunny) getTurn() int {
	return b.turn
}

func (b *Bunny) addPower(amount int) {
	b.power += amount
}

func (b *Bunny) setTurn(turn int) {
	b.turn = turn
}

func (b *Bunny) getName() string {
	return "bunny"
}

func (b *Bunny) isFed() bool {
	return (b.power >= c.bunnyFed)
}

func (b *Bunny) update() {
	b.power -= 1
	b.age++
	if b.childCooldown > 0 {
		b.childCooldown -= 1
	}
}

func (b *Bunny) alive() bool {
	return (b.power > 0 && b.age < c.bunnyLiveLength)
}

func (b *Bunny) makeChild() Organism {
	return &Bunny{c.bunnyStart, c.bunnyCooldown, b.turn, 0}
}

func (b *Bunny) willEat(org Organism) bool {
	return (org.getName() == "grass")
}
