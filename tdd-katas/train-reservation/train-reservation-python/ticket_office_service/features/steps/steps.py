from behave import *
from ticket_office import TicketOffice
from rest_calls import *

@given(u'I have made a reservation with booking reference {booking_reference}')
def i_have_made_a_reservation_with_booking_reference(context, booking_reference):
    context.booking_reference = booking_reference
    context.train_id = "express_2000"

    seats = ["1A", "2A"]
    train = book_seats(context.train_id, seats, booking_reference)
    
    assert train["seats"]["1A"]["booking_reference"] == booking_reference
    assert train["seats"]["2A"]["booking_reference"] == booking_reference

@when(u'I cancel my reservation')
def i_cancel_my_reservation(context):
    TicketOffice().cancel_reservation(context.train_id, context.booking_reference)

@then(u'the reserved seats should be available again')
def the_reserved_seats_should_be_available_again(context):
    train = get_data_for(context.train_id)
  
    assert train["seats"]["1A"]["booking_reference"] == ""
    assert train["seats"]["2A"]["booking_reference"] == ""
