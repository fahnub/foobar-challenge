def solution(x, y):
    worker_id = (((x + y - 2) * (x + y - 1)) / 2) + x
    return str(worker_id)
