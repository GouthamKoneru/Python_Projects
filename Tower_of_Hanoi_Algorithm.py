def hanoi_solver(n):
    rods = [list(range(n, 0, -1)), [], []]
    moves = []

    def record_state():
        moves.append(" ".join(str(rod) for rod in rods))

    def move_disk(source, target):
        rods[target].append(rods[source].pop())
        record_state()

    def solve(disks, source, target, auxiliary):
        if disks == 1:
            move_disk(source, target)
        else:
            solve(disks - 1, source, auxiliary, target)
            move_disk(source, target)
            solve(disks - 1, auxiliary, target, source)

    record_state()

    if n > 0:
        solve(n, 0, 2, 1)

    return "\n".join(moves)
