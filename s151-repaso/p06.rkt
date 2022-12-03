#lang racket/base
;Contar digitos
(define (count-digits n) 
    (if (eq? n 0)
        0
        (+ 1 (count-digits (quotient n 10)))
    )
)
;Pruebas
(count-digits 44)
(define my-list '(2376 34 377 283454 1 77))
(map count-digits my-list)