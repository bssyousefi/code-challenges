// First solution (beats 75%) (Kruskal's algorithm)
type Cost struct {
    cost float64
    i    int
    j    int
}

func minCostConnectPoints(points [][]int) int {
    l := len(points)
    costs := make([]Cost,0,l*(l-1)/2)
    for i:=0;i<l;i++ {
        for j:=i+1;j<l;j++ {
            costs = append(costs, Cost{(math.Abs(float64(points[i][0]-points[j][0])))+(math.Abs(float64(points[i][1]-points[j][1]))), i, j})
        }
    }
    slices.SortFunc(costs, func(i,j Cost) int {
        if i.cost < j.cost {
            return -1
        } else {
            return 1
        }
    })
    parents := make([]int, l)
    for i:=0;i<l;i++ {
        parents[i] = i
    }
    ret := float64(0)
    counter := 0
    var find func(int)int
    find = func(i int) int {
        if parents[i] != i {
            parents[i] = find(parents[i])
        }
        return parents[i]
    }
    for _, cost := range costs {
        iRep := find(cost.i)
        jRep := find(cost.j)
        if iRep != jRep {
            parents[jRep] = iRep
            counter++
            ret += cost.cost
            if counter == l-1 {
                break
            }
        }
    }
    return int(ret)
}
// Second solution (beats 100%) (Prim's algorithm)
func minCostConnectPoints(points [][]int) int {
    dist := make([]int, len(points))
    for i := range dist {
        dist[i] = math.MaxInt
    }
    ans := 0

    for i := 0; i < len(points)-1; i++ {
        for j := i + 1; j < len(points); j++ {
            dist[j] = min(dist[j], abs(points[i][0]-points[j][0])+abs(points[i][1]-points[j][1]))
            if dist[j] < dist[i+1] {
                points[j], points[i+1] = points[i+1], points[j]
                dist[j], dist[i+1] = dist[i+1], dist[j]
            }
        }
        ans += dist[i+1]
    }

    return ans
}

func min(a, b int) int {
    if a < b {
        return a
    }
    return b
}

func abs(a int) int {
    if a < 0 {
        return -a
    }
    return a
}
