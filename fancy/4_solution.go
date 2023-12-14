package main

import (
	"fmt"
	"math"
	"math/rand"
	"time"

	"github.com/go-gota/gota"
	"github.com/go-gota/gota/dataframe"
	"github.com/go-gota/gota/series"
	"github.com/gonum/stat"
)

type KaggleHouse struct {
	batchSize int
	rawTrain  dataframe.DataFrame
	rawVal    dataframe.DataFrame
	train     dataframe.DataFrame
	val       dataframe.DataFrame
}

func (k *KaggleHouse) preprocess() {
	label := "SalePrice"

	// Remove the ID and label columns
	features := k.rawTrain.Drop("Id").Drop(label).Concat(k.rawVal.Drop("Id"))

	// Standardize numerical columns
	var numericFeatures []string
	for _, col := range features.Names() {
		if features.Col(col).Type() == series.Float {
			numericFeatures = append(numericFeatures, col)
			colData := features.Col(col).Float()
			mean, std := stat.MeanStdDev(colData, nil)
			newCol := make([]float64, len(colData))
			for i, val := range colData {
				newCol[i] = (val - mean) / std
			}
			features = features.Mutate(series.New(newCol, series.Float, col))
		}
	}

	// Replace NAN numerical features by 0
	for _, colName := range numericFeatures {
		col := features.Col(colName).Float()
		newCol := make([]float64, len(col))
		for i, val := range col {
			if math.IsNaN(val) {
				newCol[i] = 0
			} else {
				newCol[i] = val
			}
		}
		features = features.Mutate(series.New(newCol, series.Float, colName))
	}

	// Replace discrete features by one-hot encoding
	features = oneHotEncoding(features)

	// Save preprocessed features
	trainSize := k.rawTrain.Nrow()
	k.train = features.Subset(gota.IndexRange(0, trainSize))
	labelCol := k.rawTrain.Col(label)
	labelCol.Name = label
	k.train = k.train.Mutate(labelCol)
	k.val = features.Subset(gota.IndexRange(trainSize, features.Nrow()))
}

func oneHotEncoding(df dataframe.DataFrame) dataframe.DataFrame {
	categoricalCols := df.Select(func(col dataframe.Column) bool {
		return col.Type() == series.String
	}).Names()
	for _, colName := range categoricalCols {
		df = df.Drop(colName)
		uniqueValues := df.Col(colName).Unique()
		for _, val := range uniqueValues {
			newColName := fmt.Sprintf("%s_%v", colName, val)
			newCol := make([]int, df.Nrow())
			for i, cell := range df.Col(colName).Records() {
				if cell == val {
					newCol[i] = 1
				} else {
					newCol[i] = 0
				}
			}
			df = df.Mutate(series.Ints(newCol).WithName(newColName))
		}
	}
	return df
}

func main() {
	rand.Seed(time.Now().UnixNano())
	k := KaggleHouse{10, generateDummyData(1000, 10), generateDummyData(200, 10), dataframe.DataFrame{}, dataframe.DataFrame{}}
	k.preprocess()
	fmt.Println("Preprocessed data:", k.train, k.val)
}

func generateDummyData(rows, cols int) dataframe.DataFrame {
	headers := make([]string, cols)
	data := make([][]string, rows)
	for i := range headers {
		headers[i] = fmt.Sprintf("Col_%d", i)
	}
	for i := range data {
		data[i] = make([]string, cols)
		for j := range data[i] {
			data[i][j] = fmt.Sprintf("%f", rand.Float64())
		}
	}
	return dataframe.LoadRecords(data, dataframe.WithHeaders(headers...))
}
