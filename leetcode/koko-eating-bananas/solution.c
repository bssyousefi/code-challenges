int minEatingSpeed(int* piles, int pilesSize, int h) {
    int min_ = 1;
    int max_ = 0;
    int n = 0;
    int m = 0;
    for(int i=0;i<pilesSize;i++) {
        max_ = max_ < piles[i] ? piles[i] : max_;
    }
    while(min_<max_){
        m = (min_ + max_ ) / 2;
        n = getMoves(piles, pilesSize, m);

        if(n<=h) {
            max_ = m;
        } else {
            min_ = m + 1;
        }
    }
    return min_;
}
int getMoves(int* piles, int pilesSize, int k) {
    int n = 0;
    for(int i=0;i<pilesSize;i++) {
        n += piles[i]/k;
        n += piles[i]%k == 0 ? 0 : 1;
    }
    return n;
}
