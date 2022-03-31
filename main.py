def on_a_pressed():
    global projectile
    projectile = sprites.create_projectile_from_sprite(img("""
            . . . . . . . .
                    . . . . . . . .
                    . . . . . . . .
                    . . . . . . . .
                    . . . 7 7 . . .
                    . . . 7 7 . . .
                    . . . 7 7 . . .
                    . . . 7 7 . . .
        """),
        ship,
        0,
        -140)
    projectile.start_effect(effects.cool_radial, 100)
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

fruit: Sprite = None
projectile: Sprite = None
ship: Sprite = None
asteroids = [sprites.space.space_small_asteroid1,
    sprites.space.space_small_asteroid0,
    sprites.space.space_asteroid0,
    sprites.space.space_asteroid1,
    sprites.space.space_asteroid4,
    sprites.space.space_asteroid3]
foods = [sprites.food.small_apple,
    sprites.food.small_cherries,
    sprites.food.small_strawberry,
    sprites.food.small_lemon]
ship = sprites.create(sprites.space.space_red_ship, SpriteKind.player)
ship.set_stay_in_screen(True)
ship.bottom = 120
controller.move_sprite(ship, 100, 100)
info.set_life(3)
effects.star_field.start_screen_effect()

def on_update_interval():
    global fruit
    fruit = sprites.create_projectile_from_side(foods[randint(0, len(foods) - 1)], 0, 75)
    fruit.set_kind(SpriteKind.food)
    fruit.x = randint(10, 150)
game.on_update_interval(7500, on_update_interval)

def on_update_interval2():
    global projectile
    projectile = sprites.create_projectile_from_side(asteroids[randint(0, len(asteroids) - 1)], 0, 75)
    projectile.set_kind(SpriteKind.enemy)
    projectile.x = randint(10, 150)
game.on_update_interval(500, on_update_interval2)
