(define (my-filter func lst)
        (cond
             ((null? lst)
             nil)
             ((func (car lst))
             (cons (car lst) (my-filter func (cdr lst))))
             (else
             (my-filter func (cdr lst)))
        )
)

(define (interleave s1 s2)
        (cond
             ((and (null? s1) (null? s2))
             nil)
             ((null? s1)
             s2)
             ((null? s2)
             s1)
             (else
             (cons (car s1) (interleave s2 (cdr s1))))
        )
)

(define (accumulate merger start n term)
        (cond
             ((= 1 n)
             (term n))
             ((null? start)
             (merger (term n) (accumulate merger () (- n 1) term)))
             (else
             (merger start (term n) (accumulate merger () (- n 1) term)))
        )
)

(define (no-repeats lst)
        (cond
             ((null? lst)
             lst)
             (else
             (cons (car lst)
                            (no-repeats (my-filter (lambda (x) (not (= x (car lst)))) (cdr lst)))))
        )
)
