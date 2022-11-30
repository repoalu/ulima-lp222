#lang racket
;Definicion de funcion
(define (I x y z)
    (* (+ (* 12 x) (* 15 y)) (+ x y z))
)
;Pruebas
(I 0 0 0)
(I 0 1 0)
(I 2 2 1)
