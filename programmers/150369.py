import heapq
def solution(cap, n, deliveries, pickups):
    answer = 0
    dv_q = []
    for i, delivery in enumerate(deliveries):
        if delivery > 0:
            heapq.heappush(dv_q,((-(i+1), delivery)))
    pk_q = []
    for i, pickup in enumerate(pickups):
        if pickup > 0:
            heapq.heappush(pk_q, ((-(i+1), pickup)))

    farthest_dv = -dv_q[0][0] if dv_q else 0
    farthest_pk = -pk_q[0][0] if pk_q else 0
    dest = max(farthest_dv, farthest_pk)
    while dest > 0:
        dv_cap = cap
        pk_cap = cap
        
        while True:
            if not dv_q:
                break
            top_dv = dv_q[0][1]
            minus = min(dv_cap, top_dv)
            top_dv -= minus
            dv_cap -= minus
            if top_dv == 0:
                heapq.heappop(dv_q)
            else:
                dv_q[0] = (dv_q[0][0], top_dv)
                break
        
        while True:
            if not pk_q:
                break
            top_pk = pk_q[0][1]
            minus= min(pk_cap, top_pk)
            top_pk -= minus
            pk_cap -= minus
            if top_pk == 0:
                heapq.heappop(pk_q)
            else:
                pk_q[0] = (pk_q[0][0], top_pk)
                break

        # print(f"dest: {dest}, dv_q: {dv_q}, pk_q: {pk_q}")
        answer += 2*dest
        farthest_dv = -dv_q[0][0] if dv_q else 0
        farthest_pk = -pk_q[0][0] if pk_q else 0
        dest = max(farthest_dv, farthest_pk)
            
    return answer



cap = 2
n = 7
deliveries = [0, 0, 0, 0, 0, 0, 0]	
pickups = 	[0, 0, 0, 0, 0, 0, 0]	
print(solution(cap, n, deliveries, pickups)) # 16