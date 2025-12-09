function solution(arr, queries) {
    
    for(const [a, b] of queries){
        [arr[a], arr[b]] = [arr[b], arr[a]];
    }
    
    return arr;
}