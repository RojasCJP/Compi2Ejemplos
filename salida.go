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
	t0=5*8;
	t1=3+t0;
	t2=t1-12;
	/* inicio de expression logica */
	goto L0;
	/* goto para evitar errores */
	goto L2;
	L2:
	goto L1;
	/* goto para evitar errores */
	goto L0;
	/* finalizo la expression logica */
	
	/* inicio de expression realcional */
	if 123 > 53 {goto L3;}
	goto L4;
	/* fin de la expression relacional */
	

}