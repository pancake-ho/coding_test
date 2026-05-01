def solution(name, yearning, photo):
    answer = [0] * len(photo)
    photo_dict = {}
    
    for i in range(len(name)):
        if not name[i] in photo_dict:
            photo_dict[name[i]] = yearning[i]
            
    for i in range(len(photo)):
        for name in photo[i]:
            if name in photo_dict:
                answer[i] += photo_dict[name]

    return answer