// ENTRADA	
// a = "hola"
// b = "hola"
// a = "holaa"
// print(a)
// print(b)

// PROGRAMA PYTHON
// self.variables = {a: symbolo(id 'a', pos 2, value '###', type string)}
// self.variables = {b: symbolo(id 'b', pos 1, value '###', type string)}

package main

import (
	"fmt"
)

var P, H float64;
var stack [30101999]float64;
var heap [30101999]float64;
var t1,t2,t3,t4,t5 float64;

func main(){
	P = 0 
	H = 0

	stack[int(P)] = H
	P = P + 1
	heap[int(H)] = 104 // h
	H = H + 1
	heap[int(H)] = 111 // o
	H = H + 1
	heap[int(H)] = 108 // l
	H = H + 1
	heap[int(H)] = 97 // a
	H = H + 1

	stack[int(P)] = H
	P = P + 1
	heap[int(H)] = 104 // h
	H = H + 1
	heap[int(H)] = 111 // o
	H = H + 1
	heap[int(H)] = 108 // l
	H = H + 1
	heap[int(H)] = 97 // a
	H = H + 1

	stack[int(P)] = H
	P = P + 1
	heap[int(H)] = 104 // h
	H = H + 1
	heap[int(H)] = 111 // o
	H = H + 1
	heap[int(H)] = 108 // l
	H = H + 1
	heap[int(H)] = 97 // a
	H = H + 1
	heap[int(H)] = 97 // a
	H = H + 1

	H=stack[2]
	fmt.Printf("%c", int(heap[int(H)]))
	H = H + 1
	fmt.Printf("%c", int(heap[int(H)]))
	H = H + 1
	fmt.Printf("%c", int(heap[int(H)]))
	H = H + 1
	fmt.Printf("%c", int(heap[int(H)]))
	H = H + 1
	fmt.Printf("%c", int(heap[int(H)]))
	H = H + 1

	H=stack[1]
	fmt.Printf("%c", int(heap[int(H)]))
	H = H + 1
	fmt.Printf("%c", int(heap[int(H)]))
	H = H + 1
	fmt.Printf("%c", int(heap[int(H)]))
	H = H + 1
	fmt.Printf("%c", int(heap[int(H)]))
	H = H + 1
}