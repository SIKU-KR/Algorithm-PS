class Solution {
    public boolean isValid(String s) {
        Deque<Character> stk = new ArrayDeque();
        for(int i = 0; i < s.length(); i++){
            Character c = s.charAt(i);
            if (c.equals('(') || c.equals('{') || c.equals('[')){
                stk.offerLast(c);
            } else if (c.equals(')') && !stk.isEmpty()){
                if (!stk.pollLast().equals('(')){
                    return false;
                }
            } else if (c.equals('}') && !stk.isEmpty()){
                if (!stk.pollLast().equals('{')){
                    return false;
                }
            } else if (c.equals(']') && !stk.isEmpty()){
                if (!stk.pollLast().equals('[')){
                    return false;
                }
            } else {
                return false;
            }
        }
        if(!stk.isEmpty()){
            return false;
        }
        return true;
    }
}