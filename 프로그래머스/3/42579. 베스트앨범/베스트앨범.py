def solution(genres, plays):
    answer = []
    
    li = [] 
    sum_dict = {}
    
    for i in range(len(genres)):
        li.append((i, genres[i], plays[i]))
        if genres[i] in sum_dict:
            sum_dict[genres[i]] += plays[i]
        else:
            sum_dict[genres[i]] = plays[i]
    
    sorted_li = sorted(li, key= lambda x: [-x[2], x[0]])
    
    sum_dict_list = []
    for k in sum_dict:
        sum_dict_list.append((k, sum_dict[k]))
    sum_dict_list.sort(reverse=True, key=lambda x: x[1])
    
    for target, total in sum_dict_list:
        count = 0
        for i in range(len(sorted_li)):
            if count == 2:
                break
            songid, genre, play = sorted_li[i]
            if genre == target:
                answer.append(songid)
                count += 1

    return answer