(define (problem escape-fire2)
    (:domain escape-fire)
    
    (:objects person extinguisher position position0 position1 position2 fire1 fire2)
    
    (:init (person person)
        (extinguisher extinguisher)
        (position position1)
        (position position2)
        (position position)
        (position position0)
        (fire fire1)
        (fire fire2)
        (at person position)
        (at extinguisher position0)
        (at fire1 position1)
        (at fire2 position2)
    )
    
    (:goal (and
            (putout fire1)
            (putout fire2)
        )
    )
)