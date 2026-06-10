package checkout

import "time"

type Item struct {
	SKU       string
	Quantity  int
	UnitCents int
}

type Coupon struct {
	Code       string
	PercentOff int
	OwnerID    string
	ExpiresAt  time.Time
}

type Order struct {
	UserID   string
	Currency string
	Items    []Item
	Coupon   *Coupon
}

func TotalCents(order Order, now time.Time) int {
	total := 0
	for _, item := range order.Items {
		total += item.Quantity * item.UnitCents
	}

	if order.Coupon != nil {
		total = total * (100 - order.Coupon.PercentOff) / 100
	}

	if total < 0 {
		return 0
	}
	return total
}
