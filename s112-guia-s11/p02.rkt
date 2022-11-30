#lang racket
;Definicion de funcion
(define (G x y)
    (+ (* 2 x) (* 3 y) 5)
)
;Pruebas
(G 0 0)
(G 1 0)
(G 5 5)
