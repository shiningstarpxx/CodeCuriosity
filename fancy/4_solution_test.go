package main

import (
	"testing"

	"github.com/go-gota/gota/dataframe"
	"github.com/stretchr/testify/assert"
)

func TestKFoldData(t *testing.T) {
	data := KaggleHouse{10, generateDummyData(1000, 10), generateDummyData(200, 10), dataframe.DataFrame{}, dataframe.DataFrame{}}
	kFoldedData := kFoldData(data, 5)

	assert.Equal(t, 5, len(kFoldedData), "kFoldData should return 5 subsets")

	for _, subset := range kFoldedData {
		assert.Equal(t, 10, subset.batchSize, "Batch size should be 10")
		assert.Equal(t, 200, subset.train.Nrow(), "Training set size should be 200")
		assert.Equal(t, 200, subset.val.Nrow(), "Validation set size should be 200")
	}
}

func TestPreprocess(t *testing.T) {
	data := KaggleHouse{10, generateDummyData(1000, 10), generateDummyData(200, 10), dataframe.DataFrame{}, dataframe.DataFrame{}}
	data.preprocess()

	assert.Equal(t, 1000, data.train.Nrow(), "Training set size should be 1000")
	assert.Equal(t, 200, data.val.Nrow(), "Validation set size should be 200")
}
