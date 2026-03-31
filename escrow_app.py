from pyteal import *

def approval_program():
    total = Bytes("TOTAL")
    paid = Bytes("PAID")
    members = Bytes("MEMBERS")

    return Cond(
        [Txn.application_id() == Int(0),
         Seq(
             App.globalPut(total, Btoi(Txn.application_args[0])),
             App.globalPut(members, Btoi(Txn.application_args[1])),
             App.globalPut(paid, Int(0)),
             Return(Int(1))
         )],

        [Txn.on_completion() == OnComplete.NoOp,
         Seq(
             App.globalPut(paid, App.globalGet(paid) + Int(1)),
             Return(Int(1))
         )],

        [Txn.on_completion() == OnComplete.DeleteApplication,
         Return(App.globalGet(paid) == App.globalGet(members))]
    )