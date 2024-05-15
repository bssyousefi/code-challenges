int search(int* nums, int numsSize, int target) {
    int l = 0;
    int r = numsSize - 1;
    int m = 0;

    while(l<=r) {
        m = (l+r) / 2;
        if(nums[l] < nums[m]) {
            if(nums[m] == target) {
                return m;
            } else if((nums[m] > target && nums[l] > target) || nums[m] < target) {
                l = m + 1;
            } else {
                r = m - 1;
            }
        } else if(nums[l] > nums[m]) {
            if(nums[m] == target) {
                return m;
            } else if((nums[m] < target && nums[r] < target) || nums[m] > target) {
                r = m - 1;
            } else {
                l = m + 1;
            }
        } else {
            if(nums[l] == target) {
                return l;
            } else {
                l = m + 1;
            }
        }
    }
    return -1;
}
