package fancy

import (
	"testing"
)

func TestAccumulator(t *testing.T) {
	acc := NewAccumulator(2)

	acc.Add(1.0, 2.0)
	if acc.Get(0) != 1.0 || acc.Get(1) != 2.0 {
		t.Errorf("Expected values 1.0 and 2.0, but got %f and %f", acc.Get(0), acc.Get(1))
	}

	acc.Add(3.0, 4.0)
	if acc.Get(0) != 4.0 || acc.Get(1) != 6.0 {
		t.Errorf("Expected values 4.0 and 6.0, but got %f and %f", acc.Get(0), acc.Get(1))
	}

	acc.Reset()
	if acc.Get(0) != 0.0 || acc.Get(1) != 0.0 {
		t.Errorf("Expected values 0.0 and 0.0 after reset, but got %f and %f", acc.Get(0), acc.Get(1))
	}
}
