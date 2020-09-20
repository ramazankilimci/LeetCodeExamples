package main

import "fmt"
import "strings"

func defangIPaddress(address string) string {
	// Used strings.Replace method for the func.
	// "-1" means replace all the "."
	address = strings.Replace(address, ".", "[.]", -1)
	return address
}

func main() {
	// Test string for the function
	testIP := "10.10.10.10"
	// Print the output without using any variable
	fmt.Println(defangIPaddress(testIP))
}
