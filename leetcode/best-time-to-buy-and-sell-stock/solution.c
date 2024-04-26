int maxProfit(int* prices, int pricesSize) {
    int max_ = 0;
    int min_ = 1e7;
    for(int i=0; i<pricesSize; i++) {
        if(prices[i] < min_) {
            min_ = prices[i];
        } else {
            max_ = (prices[i] - min_ > max_) ? prices[i] - min_ : max_;
        }
    }
    return max_;
}
