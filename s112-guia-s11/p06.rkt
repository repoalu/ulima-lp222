#lang racket
;Definimos la funcion (no debemos llamar a length)
(define (len-list my-list)
    ;Caso base: Lista vacia - retorna cero
    (if (eq? my-list '())
        0
        ;Caso contrario: 1 + longitud(resto)
        (+ 1 (len-list (cdr my-list)))
    )
)
;Pruebas
(define my-list '(2 2 3 4 8 2))
(len-list my-list)