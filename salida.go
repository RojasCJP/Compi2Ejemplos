/*----HEADER----*/
package main;

import (
	"fmt"
)

var t0, t1, t2 float64;
var P, H float64;
var stack [30101999]float64;
var heap [30101999]float64;



func main(){
	/* compilacion de valor de la variable */
	/* fin de compilacion de valor de variable */
	stack[int(0)]=123;
	
	/* compilacion de valor de la variable */
	/* esto es un acceso */
	t0=stack[int(0)];
	/* fin de compilacion de acceso */
	
	/* fin de compilacion de valor de variable */
	stack[int(1)]=t0;
	
	/* esto es un acceso */
	t1=stack[int(0)];
	/* fin de compilacion de acceso */
	
	fmt.Printf("%d", int(t1));
	fmt.Printf("%c", int(32));
	/* esto es un acceso */
	t2=stack[int(1)];
	/* fin de compilacion de acceso */
	
	fmt.Printf("%d", int(t2));
	fmt.Printf("%c", int(32));
	fmt.Printf("%c", int(10));

}