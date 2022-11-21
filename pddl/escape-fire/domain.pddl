(define (domain escape-fire)
    (:predicates
        (person ?p)
        (position ?p)
        (fire ?f)
        (extinguisher ?e)
        (putout ?f)
        (at ?object ?position)
        (have ?e)
    )
    
    (:action move
        :parameters (?person ?from ?to)
        :precondition (and (person ?person) (position ?from) (position ?to) (at ?person ?from))
        :effect (and (not (at ?person ?from)) (at ?person ?to))
    )
    
    (:action pickExtinguisher
        :parameters (?e ?p ?position)
        :precondition (and (extinguisher ?e) (person ?p) (position ?position) (at ?e ?position) (at ?p ?position))
        :effect (have ?e)
    )
    (:action extinguish
        :parameters (?e ?p ?f ?position)
        :precondition (and (extinguisher ?e) (person ?p) (fire ?f) (position ?position) (not (putout ?f))
            (at ?f ?position) (at ?p ?position) (have ?e))
        :effect (putout ?f)
    )
)