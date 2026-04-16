class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        int n = nums.size();

        int counter = 0;
        while (counter < n) {
            int val = nums[counter];
            for (int i = 0; i < n; i++) {
                if (nums[i] == val && i != counter) {
                    return true;
                }
            }

            counter++;
        }

        return false;
        
    }
};
