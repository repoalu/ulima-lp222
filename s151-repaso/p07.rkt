#lang racket/base
(define (belongs-to number a b)
    (and (>= number a) (<= number b))
)

(define (filter-interval my-list a b)
    (filter (lambda (x) (belongs-to x a b)) my-list)
)


(belongs-to 10 1 100)
(belongs-to 12 1 100)
(belongs-to 300 1 100)
(define my-list '(10 20 30 40 50 60))
(filter-interval my-list 25 55)
