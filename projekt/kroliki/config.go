package main

type Config struct {
	gridX           int
	gridY           int
	worldAmount     int
	turnLimit       int
	initialBunny    int
	initialGrass    int
	initialFox      int
	bunnyStart      int
	bunnyFood       int
	bunnyCooldown   int
	bunnyFed        int
	bunnyChildren   int
	bunnyLiveLength int
	foxStart        int
	foxFood         int
	foxCooldown     int
	foxFed          int
	foxChildren     int
	foxLiveLength   int
	grassStart      int
	grassFood       int
	grassCooldown   int
	grassChildren   int
	grassLiveLength int
}

var c = Config{gridX: 20, gridY: 20, worldAmount: 1, turnLimit: 500, initialBunny: 12, initialGrass: 60, initialFox: 5,
	bunnyStart: 20, bunnyFood: 20, bunnyCooldown: 5, bunnyFed: 15, bunnyChildren: 1, bunnyLiveLength: 20,
	foxStart: 40, foxFood: 15, foxCooldown: 15, foxFed: 30, foxChildren: 1, foxLiveLength: 40,
	grassStart: 5, grassFood: 3, grassCooldown: 5, grassChildren: 1, grassLiveLength: 10}
