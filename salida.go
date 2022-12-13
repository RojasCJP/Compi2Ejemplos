/*----HEADER----*/
package main;

import (
	"fmt"
)

var t0 float64;
var P, H float64;
var stack [30101999]float64;
var heap [30101999]float64;



func main(){
	/* compilacion de valor de la variable */
	/* fin de compilacion de valor de variable */
	stack[int(0)]=123;
	
	/* esto es un acceso */
	t0=stack[int(0)];
	/* fin de compilacion de acceso */
	
	fmt.Printf("%d", int(t0));
	fmt.Printf("%c", int(32));
	fmt.Printf("%d", int(123124));
	fmt.Printf("%c", int(32));
	fmt.Printf("%c", int(10));

}