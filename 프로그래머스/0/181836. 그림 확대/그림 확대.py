def solution(picture, k):
    newPicture = []
    for i in picture:
        pictureItem = []
        for j in list(i):
            pictureItem.append(j*k)
            
        newPicture.append(''.join(pictureItem))
        
    result = []
    for newItem in newPicture:
        for _ in range(k):
            result.append(newItem)
            
    return result