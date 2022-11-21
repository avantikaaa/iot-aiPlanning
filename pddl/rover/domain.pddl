(define (domain rover)
    (:predicates
        (rover ?r)
        (sample ?s)
        (site ?s)
        (at ?obj ?site)
        (free ?rover)
        (carry ?rover ?s)
    )
    
    (:action pickup
        :parameters (?rover ?s ?site)
        :precondition (and (rover ?rover) (sample ?s) (site ?site)
            (free ?rover) (at ?rover ?site) (at ?s ?site))
        :effect (and (not (free ?rover)) (not (at ?s ?site)) (carry ?rover ?s))
    )
    
    (:action drop
        :parameters (?rover ?s ?site)
        :precondition (and (rover ?rover) (sample ?s) (site ?site)
            (at ?rover ?site) (carry ?rover ?s))
        :effect (and (at ?s ?site) (free ?rover) (not(carry ?rover ?s)))
    )
    
    (:action move
        :parameters (?from ?to ?rover)
        :precondition (and (rover ?rover) (site ?to) (site ?from) (at ?rover ?from))
        :effect (and (not (at ?rover ?from)) (at ?rover ?to))
    )
)