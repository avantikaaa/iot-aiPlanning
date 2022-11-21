(define (problem rover4)
    (:domain rover)
    
    (:objects rover site0 site1 site2 sample1 sample2 sample3 sample4)
    
    (:init (rover rover)
        (site site0)
        (site site1)
        (site site2)
        (sample sample1)
        (sample sample2)
        (sample sample3)
        (sample sample4)
        (free rover)
        (at sample1 site1)
        (at sample2 site1)
        (at sample3 site1)
        (at sample4 site1)
        (at rover site0)
    )
    
    (:goal (and
            (at sample1 site2)
            (at sample2 site2)
            (at sample3 site2)
            (at sample4 site2)
        )
    )
)