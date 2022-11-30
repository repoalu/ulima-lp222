#lang racket
;Funcion - maximo (Pre - Requisito: Un elemento o mas)
(define (max-list my-list)
    ;Caso base: Un solo elemento - sera el maximo
    (if (eq? (length my-list) 1)
        (car my-list)
        ;En caso contrario, sera el maximo entre el primer elemento
        ;y el mayor elemento que pueda encontrarse en el resto de la lista
        (max (car my-list) (max-list (cdr my-list)))
    )
)
;Funcion - minimo: Por analogia
(define (min-list my-list)
    (if (eq? (length my-list) 1)
        (car my-list)
        (min (car my-list) (min-list (cdr my-list)))
    )
)

;Pruebas
(define my-list '(2 1 3 14 8 11))
(max-list my-list)
(min-list my-list)