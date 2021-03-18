
tic = ["X","O","X"]
tac = ["O","X","O"]
toe = ["X","O","O"]
def tic_tac_toe (tic,tac,toe):
    set_tic = set(tic)
    set_tac = set(tac)
    set_toe = set(toe)
    if len(set_tic) == 1:
        set_tic = list(set_tic)
        return f"AND THE WINNER IS... DRUM ROLL PLEASE...{set_tic[0]}"
    elif len(set_tac) == 1:
        set_tac = list(set_tac)
        return f"AND THE WINNER IS... DRUM ROLL PLEASE...{set_tac[0]}"
    elif len(set_toe) == 1:
        set_toe = list(set_toe)
        return f"AND THE WINNER IS... DRUM ROLL PLEASE...{set_toe[0]}"
    for tics,tacs,toes in zip(tic,tac,toe):
        if tics==tacs==toes:
            return f"AND THE WINNER IS... DRUM ROLL PLEASE...{tics}"
    if tic[0] == tac[1] == toe[2]:
        return f"AND THE WINNER IS... DRUM ROLL PLEASE...{tic[0]}"
    elif tic[2]==tac[1]==toe[0]:
        return f"AND THE WINNER IS... DRUM ROLL PLEASE...{tic[2]}"
print(tic_tac_toe(tic,tac,toe))