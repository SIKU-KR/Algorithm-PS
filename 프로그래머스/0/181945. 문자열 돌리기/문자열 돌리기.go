package main

import (
	"fmt"
)

func main() {
	var s1 string
	fmt.Scan(&s1)
	runes := []rune(s1)
	for i := 0; i < len(runes); i++ {
		fmt.Println(string(runes[i]))
	}
}
