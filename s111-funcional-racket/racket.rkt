;Un comentario (una sola linea)
;Siempre indicaer el lenguaje del modulo (en todos los archivos)
#lang racket

#|
--
Comentario de varias lineas.
--
|#

;Hola mundo
(display "Hola mundo! \n")
;Realizar operaciones (notacion prefija)
;4 + 5
(+ 4 5)
;2 + 2 x 3
(+ 2 (* 2 3))

;Algunas operaciones matematicas
(remainder 10 3)
(expt 2 6)

;Definir una funcion (suma)
(define (sum x y)
    (+ x y)
)
;Invocar una funcion
(sum 3 4)
(sum 8 9)
;Definir una lista
(define my-list '(1 2 3 4 5))
;Obtiene el primer elemento de la lista
(car my-list)
;Obtiene los elementos restantes
(cdr my-list)
;Longitud de la lista
(length my-list)
;Elemento en una posicion (ej: posicion 2)
(list-ref my-list 2)
;Obtiene los elementos de la lista en orden inverso
(reverse my-list)
;Determina si la lista esta vacia o no
(empty? my-list)