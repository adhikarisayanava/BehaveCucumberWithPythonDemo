from behave import *
from twentyone import *

@given('a dealer')
def step_impl(context):
    context.dealer = Dealer()

@when('the round starts')
def step_impl(context):
    context.dealer.new_round()


@then('the dealer gives itself two cards')
def step_impl(context):
    assert (len(context.dealer.hand) == 2)

@given('a {hand}')
def step_impl(context, hand):
    context.dealer = Dealer()
    context.dealer.hand = hand.split(',')

@when('the dealer sums the cards')
def step_impl(context):
    context.dealer_total = context.dealer.get_hand_total()

#here below,"d" is a shortcut to tell Behave to treat the parameter as an integer 
@then('the {total:d} is correct')
def step_impl(context, total):
    assert (context.dealer_total == total)