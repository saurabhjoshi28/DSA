package Solutions;

import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class MinimumWindowSubstring {
    public String run(){
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter string s: ");
        String s = sc.nextLine();
        System.out.println("Enter string t: ");
        String t = sc.nextLine();
        String result = minWindow(s, t);
        return "Result is: " + result;
    }

    public static String minWindow(String s, String t) {
            int n = s.length(), m = t.length();
            Map<Character, Integer> mpp = new HashMap<>();
            for (int i = 0; i < m; i++){
                mpp.put(t.charAt(i), mpp.getOrDefault(t.charAt(i), 0) + 1);
            }
            int cnt = 0;
            int l = 0, r = 0;
            int minLen = Integer.MAX_VALUE, startIdx = -1, endIdx = Integer.MAX_VALUE;
            while (r < n){
                if (mpp.containsKey(s.charAt(r))){
                   if (mpp.get(s.charAt(r)) > 0){
                       cnt += 1;
                   }
                   mpp.put(s.charAt(r), mpp.get(s.charAt(r)) - 1);
                }
                while (cnt == m){
                    if ((r - l + 1) < minLen){
                        minLen = (r - l + 1);
                        startIdx = l;
                        endIdx = r;
                    }
                    if (mpp.containsKey(s.charAt(l))){
                        mpp.put(s.charAt(l), mpp.get(s.charAt(l)) + 1);
                        if (mpp.get(s.charAt(l)) > 0){
                            cnt -= 1;
                        }
                    }
                    l += 1;
                }
                r += 1;
            }
            if (startIdx == -1){
                return "";
            } else{
                return s.substring(startIdx, endIdx + 1);
            }
    }
}
