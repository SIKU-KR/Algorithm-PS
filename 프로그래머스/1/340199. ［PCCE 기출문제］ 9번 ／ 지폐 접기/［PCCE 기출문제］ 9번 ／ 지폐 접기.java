class Solution {
    public int solution(int[] wallet, int[] bill) {
        int answer = 0;
        while(true){
            if(!isFit(wallet, bill)){
                bill = fold(bill);
                answer++;
            } else {
                return answer;
            }
        }
    }
    
    int[] fold(int[] bill){
        if(bill[0] > bill[1]){
            return new int[]{bill[0]/2, bill[1]};
        } else {
            return new int[]{bill[0], bill[1]/2};
        }
    }
    
    boolean isFit(int[] wallet, int[] bill){
        if(Math.min(bill[0], bill[1]) > Math.min(wallet[0], wallet[1]) || Math.max(bill[0], bill[1]) > Math.max(wallet[0], wallet[1])){
            return false;
        } 
        return true;
    }
}