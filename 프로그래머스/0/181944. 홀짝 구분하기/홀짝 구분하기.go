package main

import "fmt"

func main() {
	var str int
	fmt.Scan(&str)
	if str%2 == 0 {
		fmt.Println(str, "is even")
	} else {
		fmt.Println(str, "is odd")
	}
}
