function solution(arr, queries) {
    return queries.map(([s, e, k]) => {
        const subArr = arr.slice(s, e+1);
        const subArrFiltered = subArr.filter(value => value > k);
        if (subArrFiltered.length === 0){
            return -1;
        }
        return Math.min(...subArrFiltered);
    });
}