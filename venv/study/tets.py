arr = [
  { "id": 1, "nextId": 6 },
  { "id": 2, "nextId": 3 },
  { "id": 3, "nextId": None },
  { "id": 4, "nextId": 5 },
  { "id": 5, "nextId": 7 },
  { "id": 6, "nextId": 4 },
  { "id": 7, "nextId": 2 }
]


def tt(arr):
    dict = {}
    for i in arr:
        dict[1 if i.get("nextId") is None else i.get("nextId")] = i.get("id")

    ans = []
    idx = 1
    while len(ans) < len(dict):
        ans.append(dict[idx])
        idx = dict[idx]

    for i in ans[::-1]:
        print(i, end=" ")


tt(arr)