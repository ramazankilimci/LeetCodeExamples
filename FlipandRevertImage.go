package main

import "fmt"

func flipAndReverseImage(A [][]int) [][]int {

	for j, firstRange := range A {
		lenArr := len(firstRange)
		for i, _ := range firstRange {
			if i <= len(firstRange)/2 {
				tmp := firstRange[i] ^ 1
				firstRange[i] = firstRange[lenArr-i-1] ^ 1
				firstRange[lenArr-i-1] = tmp
			}
		}
		A[j] = firstRange
	}

	return A
}

func main() {
	A := [][]int{{1, 1, 0},
		{0, 0, 1},
		{1, 0, 1},
	}

	fmt.Println(flipAndReverseImage(A))

}
