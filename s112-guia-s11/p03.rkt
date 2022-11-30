#lang racket
;Definicion de funcion
(define (H z)
    (+ (expt z 2) 12)
)
;Pruebas
(H 0)
(H 1)
(H 5)
