;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-advanced-reader.ss" "lang")((modname mymap) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #t #t none #f ())))
(define (mymap function listvar)
    (cond
      ((null? listvar) '())
      ((list? (car listvar)) (cons(mymap function (car listvar)) (mymap function (cdr listvar)))) 
      ( else (cons (function (car listvar)) (mymap function (cdr listvar))))))