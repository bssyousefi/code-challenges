package main

import (
    "bufio"
    "fmt"
    "io"
    "os"
    "strconv"
    "strings"
)

/*
 * Complete the 'formingMagicSquare' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts 2D_INTEGER_ARRAY s as parameter.
 */

func formingMagicSquare(s [][]int32) int32 {
    // Write your code here
    ms := [8][3][3]int32{
        {{2,9,4},{7,5,3},{6,1,8}},
        {{2,7,6},{9,5,1},{4,3,8}},
        {{4,9,2},{3,5,7},{8,1,6}},
        {{4,3,8},{9,5,1},{2,7,6}},
        {{6,1,8},{7,5,3},{2,9,4}},
        {{6,7,2},{1,5,9},{8,3,4}},
        {{8,1,6},{3,5,7},{4,9,2}},
        {{8,3,4},{1,5,9},{6,7,2}},
    }
    diff := func(a [3][3]int32) int32 {
        agg := int32(0)
        for r:=0;r<3;r++ {
            for c:=0;c<3;c++ {
                d := (s[r][c] - a[r][c])
                if d > 0 {
                    agg += d
                } else {
                    agg -= d
                }
            }
        }
        return agg
    }
    min_ := int32(81)
    for _, a:= range ms {
        d:= diff(a)
        if d < min_ {
            min_ = d
        }
    }
    return min_
}

func main() {
    reader := bufio.NewReaderSize(os.Stdin, 16 * 1024 * 1024)

    stdout, err := os.Create(os.Getenv("OUTPUT_PATH"))
    checkError(err)

    defer stdout.Close()

    writer := bufio.NewWriterSize(stdout, 16 * 1024 * 1024)

    var s [][]int32
    for i := 0; i < 3; i++ {
        sRowTemp := strings.Split(strings.TrimRight(readLine(reader)," \t\r\n"), " ")

        var sRow []int32
        for _, sRowItem := range sRowTemp {
            sItemTemp, err := strconv.ParseInt(sRowItem, 10, 64)
            checkError(err)
            sItem := int32(sItemTemp)
            sRow = append(sRow, sItem)
        }

        if len(sRow) != 3 {
            panic("Bad input")
        }

        s = append(s, sRow)
    }

    result := formingMagicSquare(s)

    fmt.Fprintf(writer, "%d\n", result)

    writer.Flush()
}

func readLine(reader *bufio.Reader) string {
    str, _, err := reader.ReadLine()
    if err == io.EOF {
        return ""
    }

    return strings.TrimRight(string(str), "\r\n")
}

func checkError(err error) {
    if err != nil {
        panic(err)
    }
}

