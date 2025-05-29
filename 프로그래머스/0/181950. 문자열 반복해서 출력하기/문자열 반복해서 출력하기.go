package main

import (
    "fmt"
    "strings"
)

func main() {
    var s1 string
    var a int
    fmt.Scan(&s1, &a)
    
    var sb strings.Builder
    for i := 0; i < a; i++ {
        sb.WriteString(s1)
    } 
    fmt.Println(sb.String())
    
}