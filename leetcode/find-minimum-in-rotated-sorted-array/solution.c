int findMin(int* nums, int numsSize) {
    int l = 0;
    int r = numsSize - 1;
    int m = 0;

    while(l<r) {
        m = (l+r) / 2;
        if(nums[l] < nums[r]) {
            return nums[l];
        }
        if(nums[l] <= nums[m]) {
            l = m + 1;
        } else {
            r = m;
        }
    }
    return nums[r];
}
