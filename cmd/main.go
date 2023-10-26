package main

import (
	"github.com/gofiber/fiber/v2"
)

func indexHandler(c *fiber.Ctx) error {
	return c.SendString("Hello, world!")
}

func main() {
	app := fiber.New()

	app.Get("/", indexHandler)

	app.Listen(":3000")
}
