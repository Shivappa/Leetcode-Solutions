class Solution {
    public int minimumDifference(int[] nums, int k) {
        if(k == 1)return 0;
        int i = 0,j = k-1,res = Integer.MAX_VALUE;
		
        Arrays.sort(nums);
        while(j < nums.length){
            res = Math.min(res,nums[j] - nums[i]);
            j++;
            i++;
        }
		
        return res;
    }
}
