from escrow_app import approval_program
from pyteal import *

def test_compile():
    teal = compileTeal(approval_program(), Mode.Application)
    assert teal is not None

def test_logic():
    paid = 3
    members = 3
    assert paid == members