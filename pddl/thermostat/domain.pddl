(define (domain thermostat)

	(:requirements :strips :fluents)
    (:predicates
    )

	; (:functions
	; 	(current)
	; )


    
    (:action increase_temp
        :parameters (?current ?goal_temp)
        :precondition (and (<(?current, ?goal_temp)))
        :effect (increase(?current, 1))
    )

	(:action decrease_temp
        :parameters (?current ?goal_temp)
        :precondition (and (>(?current, ?goal_temp)))
        :effect (decrease(?current, 1))
    )
)