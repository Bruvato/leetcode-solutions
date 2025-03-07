class Solution {
    public String breakPalindrome(String palindrome) {
        int length = palindrome.length();

        if (length == 1){
            return "";
        }

        for (int i = 0; i < length/2; i++){
            if (palindrome.charAt(i) != 'a'){
                return palindrome.substring(0, i) + 'a' + palindrome.substring(i + 1);
            }
        }

        return palindrome.substring(0, length - 1) + 'b';
    }
}


