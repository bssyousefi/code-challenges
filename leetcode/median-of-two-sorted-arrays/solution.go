// First solution (beats 100%)
func findMedianSortedArrays(nums1 []int, nums2 []int) float64 {
    var S, B []int
    var Sl, Sr, Bl, Br int
    var k, l int
    if len(nums1) < len(nums2) {
        S, B = nums1, nums2
    } else {
        S, B = nums2, nums1
    }
    i, j := 0, len(S) - 1
    s := (len(S) + len(B)) / 2
    for {
        if i + j == -1 {
            k = -1
        } else {
            k = (i + j) /2
        }
        //k := (i + j) / 2; beacause -1 / 2 == 0 not -1
        l = s - 1 - k - 1
        if k >= 0 {
            Sl = S[k]
        } else {
            //Sl = math.Inf(-1)
            Sl = -10e7
        }
        if k < len(S) - 1 {
            Sr = S[k+1]
        } else {
            //Sr = math.Inf(1)
            Sr = 10e7
        }
        if l >= 0 {
            Bl = B[l]
        } else {
            //Bl = math.Inf(-1)
            Bl = -10e7
        }
        if l < len(B) - 1 {
            Br = B[l+1]
        } else {
            //Br = math.Inf(1)
            Br = 10e7
        }
        if Sl <= Br && Bl <= Sr {
            if (len(S) + len(B)) % 2 == 1 {
                return float64(min(Sr, Br))
            } else {
                return float64(max(Sl, Bl) + min(Sr, Br)) / 2.0
            }
        } else if Sl > Br {
            j = k - 1
        } else {
            i = k + 1
        }
    }
}
