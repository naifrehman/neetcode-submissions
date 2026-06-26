class Solution {
    public boolean hasDuplicate(int[] nums) {
        int n = nums.length; 
        
        // 1. The outer loop iterates through the array from the first element
        // up to the second-to-last element (i < n - 1).
        for (int i = 0; i < n; i++) {
            
            // 2. The inner loop compares nums[i] with every element *after* it.
            // Start j at i + 1 to avoid comparing an element to itself 
            // and to avoid checking the same pair twice (e.g., (1, 3) and (3, 1)).
            for (int j = i + 1; j < n; j++) {
                
                // 3. If a match is found, immediately return true.
                if (nums[i] == nums[j]) {
                    return true;
                }
            }
        }
        
        // 4. If the loops complete without finding any match, return false.
        return false;
    }
}