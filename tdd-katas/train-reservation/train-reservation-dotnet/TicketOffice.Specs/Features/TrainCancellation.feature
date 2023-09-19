Feature: Ticket cancellation
	In order to promote ticket reservations
	As a customer
	I want to be able to cancel a reservation

Scenario: Cancel a reservation
	Given I have made a reservation with booking reference 75bcd15
	When I cancel my reservation
	Then the reserved seats should be available again
