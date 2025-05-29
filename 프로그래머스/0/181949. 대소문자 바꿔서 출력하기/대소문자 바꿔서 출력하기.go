package main

import (
	"fmt"
	"unicode"
)

func transform(s string) string {
	runes := []rune(s)
	for i, r := range runes {
		if unicode.IsLower(r) {
			runes[i] = unicode.ToUpper(r)
		} else {
			runes[i] = unicode.ToLower(r)
		}
	}
	return string(runes)
}

func main() {
	var a string
	fmt.Scan(&a)
	fmt.Println(transform(a))
}
