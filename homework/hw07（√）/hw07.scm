(define (cddr s) (cdr (cdr s)))

(define (cadr s)
        (car (cdr s)))

(define (caddr s)
        (car (cdr (cdr s))))

(define (ordered? s)
        (define (compare prev s)
        (cond 
             ((null? s)
             #t)
             ((> prev (car s))
             #f)
             (else
             (compare (car s) (cdr s)))))
        (compare (car s) (cdr s)))

(define (square x) (* x x))

(define (pow base exp)
        (cond
             ((= base 1)
             1)
             ((= exp 1)
             base)
             (else
             (* base (pow base (- exp 1))))))
