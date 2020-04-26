/*

Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,1]
Output: 1

Example 2:

Input: [4,1,2,1,2]
Output: 4

*/

// Solution 1 using HashSet
// Runtime O(n)

public class Solution1 {
    
    public int SingleNumber(int[] nums) {
        HashSet<int> myset = new HashSet<int>();
        foreach(int num in nums) {
            if (myset.Contains(num)){
                myset.Remove(num);
            } else {
                myset.Add(num);
            }
        }
        if (myset.Count() == 1) {
            return myset.First();
        }
        return 0;
    }
}

// Solution 2 using Dictionary
// Runtime O(n)
public class Solution2 {
    public int SingleNumber(int[] nums) {
        Dictionary<int, int> myset = new Dictionary<int, int>();
        foreach(int num in nums) {
            if (myset.ContainsKey(num)){
                myset[num]++;
            } else{
                myset.Add(num, 1);            
            }
        }
        foreach(KeyValuePair<int, int> entry in myset) {
            if (entry.Value == 1) {
                return entry.Key;
            }
        }
        return -1;
    }
}