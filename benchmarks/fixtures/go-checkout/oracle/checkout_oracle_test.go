package checkout

import (
	"testing"
	"time"
)

func TestCouponMustBelongToOrderUser(t *testing.T) {
	now := time.Date(2026, 6, 9, 12, 0, 0, 0, time.UTC)
	order := Order{
		UserID: "alice",
		Items: []Item{{SKU: "book", Quantity: 1, UnitCents: 1000}},
		Coupon: &Coupon{Code: "BOBONLY", PercentOff: 50, OwnerID: "bob", ExpiresAt: now.Add(time.Hour)},
	}

	got := TotalCents(order, now)

	if got != 1000 {
		t.Fatalf("cross-user coupon applied: got %d, want 1000", got)
	}
}

func TestExpiredCouponIsIgnored(t *testing.T) {
	now := time.Date(2026, 6, 9, 12, 0, 0, 0, time.UTC)
	order := Order{
		UserID: "alice",
		Items: []Item{{SKU: "book", Quantity: 1, UnitCents: 1000}},
		Coupon: &Coupon{Code: "OLD", PercentOff: 50, OwnerID: "alice", ExpiresAt: now.Add(-time.Minute)},
	}

	got := TotalCents(order, now)

	if got != 1000 {
		t.Fatalf("expired coupon applied: got %d, want 1000", got)
	}
}

func TestInvalidCouponPercentIsIgnored(t *testing.T) {
	now := time.Date(2026, 6, 9, 12, 0, 0, 0, time.UTC)
	order := Order{
		UserID: "alice",
		Items: []Item{{SKU: "book", Quantity: 1, UnitCents: 1000}},
		Coupon: &Coupon{Code: "BAD", PercentOff: 150, OwnerID: "alice", ExpiresAt: now.Add(time.Hour)},
	}

	got := TotalCents(order, now)

	if got != 1000 {
		t.Fatalf("invalid coupon percent changed total: got %d, want 1000", got)
	}
}

func TestInvalidItemsAreIgnoredButValidItemsRemain(t *testing.T) {
	order := Order{
		UserID: "alice",
		Items: []Item{
			{SKU: "book", Quantity: 1, UnitCents: 1000},
			{SKU: "bad-qty", Quantity: -4, UnitCents: 100},
			{SKU: "bad-price", Quantity: 1, UnitCents: -500},
		},
	}

	got := TotalCents(order, time.Now())

	if got != 1000 {
		t.Fatalf("invalid items affected total: got %d, want 1000", got)
	}
}
