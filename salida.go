/*----HEADER----*/
package main;

import (
	"fmt"
)

var t0, t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11, t12, t13, t14 float64;
var P, H float64;
var stack [30101999]float64;
var heap [30101999]float64;

/*-----NATIVES-----*/
func to_upper(){
	t1=P+1;
	t2=stack[int(t1)];
	L1:
	t3=heap[int(t2)];
	if t3 == -1 {goto L0;}
	if t3 < 97 {goto L2;}
	if t3 > 122 {goto L2;}
	t4=t3-32;
	heap[int(t2)]=t4;
	L2:
	t2=t2+1;
	goto L1;
	L0:
	return;
}
func print_string(){
	t8=P+1;
	t9=stack[int(t8)];
	L4:
	t10=heap[int(t9)];
	if t10 == -1 {goto L3;}
	fmt.Printf("%c", int(t10));
	t9=t9+1;
	goto L4;
	L3:
	return;
}


func main(){
	t0=H;
	heap[int(H)]=4;
	H=H+1;
	heap[int(H)]=104;
	H=H+1;
	heap[int(H)]=111;
	H=H+1;
	heap[int(H)]=108;
	H=H+1;
	heap[int(H)]=97;
	H=H+1;
	heap[int(H)]=-1;
	H=H+1;
	t0=t0+0.12837;
	t5=P+0;
	t5=t5+1;
	stack[int(t5)]=t0;
	P=P+0;
	to_upper();
	t7=P+1;
	t6=stack[int(t7)];
	t11=P+0;
	t11=t11+1;
	stack[int(t11)]=t6;
	P=P+0;
	print_string();
	t12=stack[int(P)];
	P=P-0;
	fmt.Printf("%c", int(32));
	fmt.Printf("%c", int(10));
	/* compilacion de len (obtener la longitud de un arreglo o string) */
	t13=H;
	heap[int(H)]=7;
	H=H+1;
	heap[int(H)]=104;
	H=H+1;
	heap[int(H)]=111;
	H=H+1;
	heap[int(H)]=108;
	H=H+1;
	heap[int(H)]=97;
	H=H+1;
	heap[int(H)]=97;
	H=H+1;
	heap[int(H)]=97;
	H=H+1;
	heap[int(H)]=97;
	H=H+1;
	heap[int(H)]=-1;
	H=H+1;
	t13=t13+0.12837;
	t14=t13;
	t14=heap[int(t14)];
	fmt.Printf("%d", int(t14));
	fmt.Printf("%c", int(32));
	fmt.Printf("%c", int(10));

}