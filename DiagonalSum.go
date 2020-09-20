package main

import "fmt"

func diagonalSum(mat [][]int) int {
	n := len(mat)
	sum := 0
	// Sums diagonal values
	for i := 0; i < len(mat); i++ {
		sum += mat[i][i] + mat[i][n-i-1]
	}
	// Removes middle value of index if size of index is odd.
	if n%2 == 1 {
		sum = sum - mat[n/2][n/2]
	}
	return sum
}

func main() {

	mat := [][]int{
		{1, 2, 3, 4},
		{1, 2, 3, 4},
		{1, 2, 3, 4},
		{1, 2, 3, 4},
	}

	fmt.Println(diagonalSum(mat))
}
