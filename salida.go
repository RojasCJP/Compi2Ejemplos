/*----HEADER----*/
package main;

import (
	"fmt"
)

var t0, t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13 float64;
var P, H float64;
var stack [30101999]float64;
var heap [30101999]float64;

/*-----NATIVES-----*/
func print_string(){
	t5=P+1;
	t6=stack[int(t5)];
	L4:
	t7=heap[int(t6)];
	if t7 == -1 {goto L3;}
	fmt.Printf("%c", int(t7));
	t6=t6+1;
	goto L4;
	L3:
	return;
}

/*-----FUNCS-----*/
func prueba(){
	t10=H;
	heap[int(H)]=0;
	H=H+1;
	heap[int(H)]=98;
	H=H+1;
	heap[int(H)]=117;
	H=H+1;
	heap[int(H)]=101;
	H=H+1;
	heap[int(H)]=110;
	H=H+1;
	heap[int(H)]=97;
	H=H+1;
	heap[int(H)]=115;
	H=H+1;
	heap[int(H)]=-1;
	H=H+1;
	t10=t10+0.12837;
	t11=P+1;
	t11=t11+1;
	stack[int(t11)]=t10;
	P=P+1;
	print_string();
	t12=stack[int(P)];
	P=P-1;
	fmt.Printf("%c", int(32));
	fmt.Printf("%c", int(10));
	return;
}

func main(){
	/* compilacion de valor de la variable */
	/* fin de compilacion de valor de variable */
	stack[int(0)]=1;
	
	L0:
	/* inicio de expression realcional */
	/* esto es un acceso */
	t0=stack[int(0)];
	/* fin de compilacion de acceso */
	
	if t0 < 10 {goto L1;}
	goto L2;
	/* fin de la expression relacional */
	
	L1:
	/* esto es un acceso */
	t1=stack[int(0)];
	/* fin de compilacion de acceso */
	
	fmt.Printf("%d", int(t1));
	fmt.Printf("%c", int(32));
	fmt.Printf("%c", int(10));
	/* compilacion de valor de la variable */
	/* esto es un acceso */
	t2=stack[int(0)];
	/* fin de compilacion de acceso */
	
	t3=t2+1;
	/* fin de compilacion de valor de variable */
	stack[int(0)]=t3;
	
	goto L0;
	L2:
	t4=H;
	heap[int(H)]=0;
	H=H+1;
	heap[int(H)]=112;
	H=H+1;
	heap[int(H)]=114;
	H=H+1;
	heap[int(H)]=117;
	H=H+1;
	heap[int(H)]=101;
	H=H+1;
	heap[int(H)]=98;
	H=H+1;
	heap[int(H)]=97;
	H=H+1;
	heap[int(H)]=32;
	H=H+1;
	heap[int(H)]=115;
	H=H+1;
	heap[int(H)]=116;
	H=H+1;
	heap[int(H)]=114;
	H=H+1;
	heap[int(H)]=105;
	H=H+1;
	heap[int(H)]=110;
	H=H+1;
	heap[int(H)]=103;
	H=H+1;
	heap[int(H)]=-1;
	H=H+1;
	t4=t4+0.12837;
	t8=P+1;
	t8=t8+1;
	stack[int(t8)]=t4;
	P=P+1;
	print_string();
	t9=stack[int(P)];
	P=P-1;
	fmt.Printf("%c", int(32));
	fmt.Printf("%c", int(10));
	t13=P+2;
	P=P+1;
	prueba();
	t13=stack[int(P)];
	P=P-1;

}