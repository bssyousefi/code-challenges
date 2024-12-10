// Solution (beats 100%)
func maxProfit(prices []int) int {
    var min_ int = 1e7
    max_ := 0

    for _, price := range prices {
        if price < min_ {
            min_ = price
        } else if newPrice:=price - min_; newPrice > max_{
            max_ = newPrice
        }
    }
    return max_
}
