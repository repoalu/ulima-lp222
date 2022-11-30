#lang racket
;Primero definimos una funcion que calcula la suma
(define (sum-list my-list)
    ;Caso base: Lista vacia - retorna cero
    (if (eq? my-list '())
        0
        ;Caso contrario: primero elemento + suma(resto)
        (+ (car my-list) (sum-list (cdr my-list)))
    )
)
;Obtiene el promedio llamando a la funcion anterior y con la longitud (lenght)
(define (average-list my-list)
    (define list-length (length my-list))
    ;Colocamos 1.0 para mantener la parte decimal
    (* 1.0 (/ (sum-list my-list) list-length))
    
)

;Pruebas
(define my-list '(2 2 3 4 8))
(sum-list my-list)
(average-list my-list)
