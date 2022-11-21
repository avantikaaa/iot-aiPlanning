(define (domain strips-gripper) 
(:predicates 	(at ?b ?r)
	(at-robby ?r)
	(carry ?o ?g)
)
(:action pick
	:parameters (?obj ?room ?gripper)
	:precondition (and  (ball ?obj) (room ?room) (gripper ?gripper) (at ?obj ?room) (at-robby ?room) (free ?gripper))
	:effect (and (carry ?obj ?gripper) (not (at ?obj ?room)) (not (free ?gripper))))
(:action move
	:parameters (?from ?to)
	:precondition (and  (room ?from) (room ?to) (at-robby ?from))
	:effect (and  (at-robby ?to) (not (at-robby ?from))))
(:action drop
	:parameters (?obj  ?room ?gripper)
	:precondition (and  (ball ?obj) (room ?room) (gripper ?gripper) (carry ?obj ?gripper) (at-robby ?room))
	:effect (and (at ?obj ?room) (free ?gripper) (not (carry ?obj ?gripper))))
)