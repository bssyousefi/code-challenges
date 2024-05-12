bool searchMatrix(int** matrix, int matrixSize, int* matrixColSize, int target) {
    int l = 0;
    int r = matrixSize - 1;
    int m = 0;
    int ll = 0;
    int rr = 0;

    while(l<=r) {
        m = (l+r) / 2;
        if(matrix[m][0] == target) {
            return 1;
        } else if(matrix[m][0] < target) {
            l = m + 1;
        } else {
            r = m - 1;
        }
    }
    if(l == 0) {
        return 0;
    }
    rr = matrixColSize[l-1] - 1;

    while(ll<=rr) {
        m = (ll+rr) / 2;
        if(matrix[l-1][m] == target) {
            return 1;
        } else if(matrix[l-1][m] < target) {
            ll = m + 1;
        } else {
            rr = m - 1;
        }
    }

    return 0;

}
