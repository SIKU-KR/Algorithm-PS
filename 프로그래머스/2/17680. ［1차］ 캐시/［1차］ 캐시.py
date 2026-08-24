def solution(cacheSize, cities):
    if cacheSize == 0:
        return len(cities) * 5
    
    answer = 0
    cache = []
    for city in cities:
        city = city.lower()
        if city in cache:
            # cache hit
            answer += 1
            cache.remove(city)
        else:
            # cache miss
            answer += 5
            if cache and len(cache) == cacheSize:
                del cache[0]
        cache.append(city)
        
    return answer