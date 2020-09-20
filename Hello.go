package main

import "fmt"

func shuffle(nums []int, n int) []int {
	numsNew := make([]int, 2*n)
	i := 0
	j := 0
	z := n
	for i < 2*n {
		if i % 2 == 0 {
			numsNew[i] = nums[j]
			j++
		} else {
			numsNew[i] = nums[z]
			z++
		}
		i++
	}
	return numsNew
}

func main() {
	arr := []int{2, 5, 1, 3, 4, 7}
	retArr := shuffle(arr, 3)
	fmt.Printf("%v\n", retArr)

}