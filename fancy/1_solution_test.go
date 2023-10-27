package fancy

import (
	"sort"
	"testing"

	"gonum.org/v1/gonum/mat"
)

func Test_dataIter_Size2(t *testing.T) {
	// Create a small dataset for testing
	features := mat.NewDense(4, 2, []float64{
		1, 2,
		3, 4,
		5, 6,
		7, 8,
	})
	labels := mat.NewVecDense(4, []float64{0, 1, 0, 1})

	// Test with a batch size of 2
	batchSize := 2
	iter := dataIter(batchSize, features, labels)

	allFeatures := &mat.Dense{}
	allLabels := &mat.VecDense{}

	for batch := range iter {
		actualFeatures := batch[0].(*mat.Dense)
		actualLabels := batch[1].(*mat.VecDense)

		r1, _ := allFeatures.Dims()
		_, c2 := actualFeatures.Dims()
		allFeatures = mat.DenseCopyOf(mat.NewDense(r1+c2, actualFeatures.RawMatrix().Cols, append(allFeatures.RawMatrix().Data, actualFeatures.RawMatrix().Data...)))

		r3 := allLabels.Len()
		r4 := actualLabels.Len()
		allLabels = mat.VecDenseCopyOf(mat.NewVecDense(r3+r4, append(allLabels.RawVector().Data, actualLabels.RawVector().Data...)))
	}

	// Sort the features and labels
	sortFeatures := func(m *mat.Dense) {
		rows, cols := m.Dims()
		data := make([][]float64, rows)
		for i := 0; i < rows; i++ {
			data[i] = make([]float64, cols)
			for j := 0; j < cols; j++ {
				data[i][j] = m.At(i, j)
			}
		}
		sort.Slice(data, func(i, j int) bool { return data[i][0] < data[j][0] })
		for i := 0; i < rows; i++ {
			for j := 0; j < cols; j++ {
				m.Set(i, j, data[i][j])
			}
		}
	}
	sortLabels := func(v *mat.VecDense) {
		data := make([]float64, v.Len())
		for i := 0; i < v.Len(); i++ {
			data[i] = v.AtVec(i)
		}
		sort.Float64s(data)
		for i := 0; i < v.Len(); i++ {
			v.SetVec(i, data[i])
		}
	}

	sortFeatures(allFeatures)
	sortFeatures(features)
	sortLabels(allLabels)
	sortLabels(labels)

	if !mat.Equal(allFeatures, features) {
		t.Errorf("Expected features %v, but got %v", features, allFeatures)
	}

	if !mat.Equal(allLabels, labels) {
		t.Errorf("Expected labels %v, but got %v", labels, allLabels)
	}
}
