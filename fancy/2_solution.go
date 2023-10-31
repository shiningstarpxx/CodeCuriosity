package fancy

// Accumulator 是一个在n个变量上累加的结构体
type Accumulator struct {
	data []float64
}

// NewAccumulator 创建一个新的Accumulator实例
func NewAccumulator(n int) *Accumulator {
	data := make([]float64, n)
	return &Accumulator{data: data}
}

// Add 使用给定的参数累加当前存储在data中的值
func (a *Accumulator) Add(args ...float64) {
	for i, b := range args {
		a.data[i] += b
	}
}

// Reset 重置data中的所有元素为0.0
func (a *Accumulator) Reset() {
	for i := range a.data {
		a.data[i] = 0.0
	}
}

// Get 返回指定索引处的值
func (a *Accumulator) Get(idx int) float64 {
	return a.data[idx]
}

/*
func main() {
	// 示例：创建一个累加器，添加值并获取结果
	acc := NewAccumulator(2)
	acc.Add(1.0, 2.0)
	acc.Add(3.0, 4.0)
	fmt.Println(acc.Get(0)) // 输出：4.0
	fmt.Println(acc.Get(1)) // 输出：6.0
}
*/
