#lang racket
;Funcion para calcular Fibonacci
(define (fibonacci n)
    (if (or (eq? n 1) (eq? n 2))
        1
        (+ (fibonacci(- n 1)) (fibonacci(- n 2)))
    )
)
;Funcion para obtener la nueva lista
(define (get-converted-list my-list)
    (map fibonacci my-list)
)

;Pruebas
(define list1 '(1 3 4 7))
(get-converted-list list1)