#lang racket/base
;Definiendo funciones
(define (F x)
  (+ (* 2 x) 3)
)
;Funciones anonimas
(define my-function (lambda (x) (+ (* 2 x) 3)))
(my-function 4)

;Map: Permite evaluar la funcion en cada valor de la lista (retorna una nueva)
(define my-list '(1 2 3 4))

(map F my-list)
(map my-function my-list)
(map (lambda (x) (+ (* 2 x) 3)) my-list )

;Filter: Permite evaluar la funcion y obtener una nueva lista con los valores
;que cumplan una condicion (que se va a evaluar a traves de una funcion)

#|
Implemente una funcion que reciba una nota (vigesimal) y
retorne verdadero en caso el alumno haya aprobado o falso en caso
contrario
|#
(define (approved-logic grade) 
  (>= grade 11)
)
;Filter para obtener solo los alumnos aprobados
(define grades2 '(10, 20, 18, 12, 7, 4, 14))
