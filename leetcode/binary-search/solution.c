int search(int* nums, int numsSize, int target) {
    int l = 0;
    int r = numsSize - 1;
    int m = 0;
    while(l<=r) {
        m = (l+r) / 2;
        if(nums[m] == target) {
            return m;
        } else if(nums[m] < target) {
            l = m + 1;
        } else {
            r = m - 1;
        }
    }
    return -1;
}
