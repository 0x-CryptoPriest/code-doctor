package checkout

import (
	"testing"
	"time"
)

func TestTotalWithoutCoupon(t *testing.T) {
	order := Order{
		UserID: "alice",
		Items: []Item{
			{SKU: "book", Quantity: 2, UnitCents: 1200},
			{SKU: "pen", Quantity: 1, UnitCents: 300},
		},
	}

	got := TotalCents(order, time.Now())

	if got != 2700 {
		t.Fatalf("TotalCents() = %d, want 2700", got)
	}
}

func TestTotalWithSimpleCoupon(t *testing.T) {
	now := time.Date(2026, 6, 9, 12, 0, 0, 0, time.UTC)
	order := Order{
		UserID: "alice",
		Items: []Item{{SKU: "book", Quantity: 1, UnitCents: 1000}},
		Coupon: &Coupon{
			Code: "SAVE10", PercentOff: 10, OwnerID: "alice", ExpiresAt: now.Add(time.Hour),
		},
	}

	got := TotalCents(order, now)

	if got != 900 {
		t.Fatalf("TotalCents() = %d, want 900", got)
	}
}
