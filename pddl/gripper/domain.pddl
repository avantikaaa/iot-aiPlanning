(define (domain gripper-strips)
    (:predicates (ball ?b)
        (room ?r)
        (gripper ?g)
        (carry ?b ?g)
        (at-robby ?r)
        (at ?b ?r)
        (free ?h))
    
    (:action move
        :parameters (?from ?to)
        :precondition (and (room ?from) (room ?to) (at-robby ?from))
        :effect (and (not (at-robby ?from)) (at-robby ?to)))
        
    (:action pickup
        :parameters (?b ?h ?r)
        :precondition (and (ball ?b) (gripper ?h) (room ?r)
            (at ?b ?r) (free ?h) (at-robby ?r))
        :effect (and (not (free ?h)) (not (at ?b ?r)) (carry ?b ?h)))

            
    (:action drop
      :parameters  (?obj  ?room ?gripper)
      :precondition  (and  (ball ?obj) (room ?room) (gripper ?gripper)
			    (carry ?obj ?gripper) (at-robby ?room))
      :effect (and (at ?obj ?room)
		    (free ?gripper)
		    (not (carry ?obj ?gripper))))

)