from typing import List, Tuple
def get_router_info(no: int, dm: List[List[int]]) -> List[Tuple[int, int, int]]:
    route = []
    for i in range(no):
        dist = []
        from_ = []
        for j in range(no):
            dist.append(dm[i][j])
            from_.append(j)
        route.append((dist, from_))

    flag = 1
    while flag:
        flag = 0
        for i in range(no):
            for j in range(no):
                for k in range(no):
                    if route[i][0][j] > (route[i][0][k] + route[k][0][j]):
                        route[i][0][j] = route[i][0][k] + route[k][0][j]
                        route[i][1][j] = k
                        flag = 1

    result = []
    for i in range(no):
        result.append([(j+1, route[i][1][j]+1, route[i][0][j]) for j in range(no)])
    return result

no = int(input("Enter no of nodes: "))
print("Enter the distance matrix:")
dm = []
for i in range(no):
    dm.append([int(x) for x in input().split()])

result = get_router_info(no, dm)
for i in range(no):
    print(f"Router info for router: {i+1}")
    print("Dest\tNext Hop\tDist")
    for j in result[i]:
        print(f"{j[0]}\t\t{j[1]}\t\t\t{j[2]}")