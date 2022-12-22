/*----HEADER----*/
package main;

import (
	"fmt"
)

var t0, t1, t2, t3, t4, t5, t6, t7, t8 float64;
var P, H float64;
var stack [30101999]float64;
var heap [30101999]float64;

/*-----NATIVES-----*/
func print_string(){
	t2=P+1;
	t3=stack[int(t2)];
	L2:
	t4=heap[int(t3)];
	if t4 == -1 {goto L1;}
	fmt.Printf("%c", int(t4));
	t3=t3+1;
	goto L2;
	L1:
	return;
}

/*-----FUNCS-----*/
func prueba(){
	/* esto es un acceso */
	t1=P+1;
	t0=stack[int(t1)];
	/* fin de compilacion de acceso */
	
	t5=P+2;
	t5=t5+1;
	stack[int(t5)]=t0;
	P=P+2;
	print_string();
	t6=stack[int(P)];
	P=P-2;
	fmt.Printf("%c", int(32));
	fmt.Printf("%c", int(10));
	return;
}

func main(){
	t7=H;
	heap[int(H)]=6;
	H=H+1;
	heap[int(H)]=49;
	H=H+1;
	heap[int(H)]=50;
	H=H+1;
	heap[int(H)]=51;
	H=H+1;
	heap[int(H)]=49;
	H=H+1;
	heap[int(H)]=50;
	H=H+1;
	heap[int(H)]=51;
	H=H+1;
	heap[int(H)]=-1;
	H=H+1;
	t7=t7+0.12837;
	t8=P+1;
	stack[int(t8)]=t7;
	P=P+0;
	prueba();
	t8=stack[int(P)];
	P=P-0;

}