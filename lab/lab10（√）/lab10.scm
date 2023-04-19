(define (over-or-under num1 num2)
    (if (= num1 num2)
        0
        (if (< num1 num2)
            -1
             1)))

(define (make-adder num)
        (lambda (inc) (+ num inc)))

(define (composed f g)
        (lambda (x) (f (g x))))

(define lst
        (list (cons 1 nil) 2 (cons 3 (cons 4 nil)) 5))

(define (remove item lst)
        (filter (lambda (x) (not (= x item))) lst))
