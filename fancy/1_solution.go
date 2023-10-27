package fancy

import (
	"fmt"
	"math/rand"

	"gonum.org/v1/gonum/mat"
)

func main() {
	features := mat.NewDense(4, 2, []float64{1, 2, 3, 4, 5, 6, 7, 8})
	labels := mat.NewVecDense(4, []float64{0, 1, 2, 3})
	batchSize := 2

	for batch := range dataIter(batchSize, features, labels) {
		batchFeatures := batch[0].(*mat.Dense)
		batchLabels := batch[1].(*mat.VecDense)
		fmt.Printf("Batch features:\n%v\nBatch labels:\n%v\n", mat.Formatted(batchFeatures), mat.Formatted(batchLabels))
	}
}

func dataIter(batchSize int, features *mat.Dense, labels *mat.VecDense) <-chan [2]interface{} {
	numExamples, _ := features.Dims()
	ch := make(chan [2]interface{})

	go func() {
		defer close(ch)

		indices := make([]int, numExamples)
		for i := 0; i < numExamples; i++ {
			indices[i] = i
		}

		rand.Shuffle(len(indices), func(i, j int) {
			indices[i], indices[j] = indices[j], indices[i]
		})

		for i := 0; i < numExamples; i += batchSize {
			end := i + batchSize
			if end > numExamples {
				end = numExamples
			}
			batchIndices := indices[i:end]

			batchFeatures := mat.NewDense(len(batchIndices), 2, nil)
			batchLabels := mat.NewVecDense(len(batchIndices), nil)

			for j, idx := range batchIndices {
				batchFeatures.SetRow(j, features.RawRowView(idx))
				batchLabels.SetVec(j, labels.AtVec(idx))
			}

			ch <- [2]interface{}{batchFeatures, batchLabels}
		}
	}()

	return ch
}
