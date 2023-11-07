package main

import (
	"fmt"
	"math/rand"
	"time"
)

type KaggleHouse struct {
	batchSize int
	train     [][]float64
	val       [][]float64
}

/*
`kFoldData`函数中的`dropRows`和`getRows`函数分别用于从原始训练数据集中删除和获取给定索引的行。
这是为了在创建k个子集时，将原始训练数据集分为两部分：新的训练集（不包含当前子集的数据）和新的验证集（仅包含当前子集的数据）。

- `dropRows`函数：这个函数从原始训练数据集中删除给定索引的行。这是为了创建一个新的训练集，其中不包含当前子集的数据。
这样，在k折交叉验证过程中，我们可以确保每个子集都有一次作为验证集的机会，而不会在训练过程中使用它们。

- `getRows`函数：这个函数从原始训练数据集中获取给定索引的行。这是为了创建一个新的验证集，其中仅包含当前子集的数据。
这样，在k折交叉验证过程中，我们可以确保每个子集都有一次作为验证集的机会，以评估模型在不同数据子集上的性能。

总之，`dropRows`和`getRows`函数分别用于从原始训练数据集中删除和获取给定索引的行，以便在k折交叉验证过程中创建新的训练集和验证集。
这有助于更全面地评估模型的性能，减少过拟合，并提高模型的泛化能力。
*/

func kFoldData(data KaggleHouse, k int) []KaggleHouse {
	rets := make([]KaggleHouse, 0)
	foldSize := len(data.train) / k

	for j := 0; j < k; j++ {
		idx := makeRange(j*foldSize, (j+1)*foldSize)
		newTrain := dropRows(data.train, idx)
		newVal := getRows(data.train, idx)
		rets = append(rets, KaggleHouse{data.batchSize, newTrain, newVal})
	}

	return rets
}

func makeRange(min, max int) []int {
	a := make([]int, max-min)
	for i := range a {
		a[i] = min + i
	}
	return a
}

func dropRows(data [][]float64, idx []int) [][]float64 {
	newData := make([][]float64, 0)
	for i, row := range data {
		if !contains(idx, i) {
			newData = append(newData, row)
		}
	}
	return newData
}

func getRows(data [][]float64, idx []int) [][]float64 {
	newData := make([][]float64, 0)
	for i, row := range data {
		if contains(idx, i) {
			newData = append(newData, row)
		}
	}
	return newData
}

func contains(arr []int, val int) bool {
	for _, a := range arr {
		if a == val {
			return true
		}
	}
	return false
}

func main() {
	rand.Seed(time.Now().UnixNano())
	data := KaggleHouse{10, generateDummyData(10, 10), generateDummyData(5, 10)}
	fmt.Println("Original train data:", data.train)
	fmt.Println("Original val data:", data.val)
	kFoldedData := kFoldData(data, 5)
	for i, d := range kFoldedData {
		fmt.Printf("K-folded %d train data %v: \n", i, d.train)
		fmt.Printf("K-folded %d val data %v: \n", i, d.val)
	}
}

func generateDummyData(rows, cols int) [][]float64 {
	data := make([][]float64, rows)
	for i := range data {
		data[i] = make([]float64, cols)
		for j := range data[i] {
			data[i][j] = rand.Float64()
		}
	}
	return data
}
