def solution(genres, plays):
    answer = []

    dict = {} # main dict
    cnt = {} # genre : count

    for i in range(len(plays)):
        if genres[i] in dict:
            dict[genres[i]][i] = plays[i]
        else :
            dict[genres[i]] = {
                i : plays[i]
            }

        cnt[genres[i]] = cnt.get(genres[i], 0) + plays[i]

    for (genre, count) in sorted(cnt.items(), reverse=True, key = lambda item:item[1]):
        for (key,value) in sorted(dict[genre].items(), reverse=True, key = lambda item:item[1])[:2]:
            answer.append(key)

    return answer


def solution_zip_enum(genres, plays):
    answer = []

    dict = {} # main dict
    cnt = {} # genre : count


    for i,(genre, play) in enumerate(zip(genres, plays)):
        if genre in dict:
            dict[genre][i] = play
        else :
            dict[genre] = {
                i : play
            }

        cnt[genres[i]] = cnt.get(genres[i], 0) + plays[i]

    for (genre, count) in sorted(cnt.items(), reverse=True, key = lambda item:item[1]):
        for (key,value) in sorted(dict[genre].items(), reverse=True, key = lambda item:item[1])[:2]:
            answer.append(key)

    return answer



genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]

print(solution(genres,plays))