( define (domain findGold)
    (:predicates 
        (box ?box)
        (key ?key)
        (diamond ?d)
        (contains ?box ?object)
        (locked ?box)
        (opens ?box ?key)
        (hand ?obj)
    )
    
    ; and also pick the object in the box
    (:action openbox
        :parameters (?box ?key ?obj)
        :precondition (and (box ?box) (key ?key) (contains ?box ?obj)
            (hand ?key) (locked ?box) (opens ?box ?key))
        :effect (and
            (not (locked ?box)) (not (hand ?key)) (hand ?obj))
        )
)