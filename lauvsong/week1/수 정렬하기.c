/* Quick Sort */
#include <stdio.h>
int nums[1000];
int partition(int left, int right) {
	int low = left + 1;
	int high = right;
	int pivot = nums[left];
	int tmp;
	while (low <= high) {
		while (pivot > nums[low] && low <= right)
			low++;
		while (pivot < nums[high] && high >= (left + 1))
			high--;
		if (low < high) {
			tmp = nums[low];
			nums[low] = nums[high];
			nums[high] = tmp;
		}
	}
	tmp = nums[left];
	nums[left] = nums[high];
	nums[high] = tmp;
	return high;
}

void qsort(int left, int right) {
	if (left < right) {
		int pivot = partition(left, right);
		qsort(left, pivot - 1);
		qsort(pivot + 1, right);
	}
}

int main() {
	int n;
	scanf("%d", &n);
	for (int i = 0; i < n; i++)
		scanf("%d", &nums[i]);
	qsort(0, n - 1);
	for (int i = 0; i < n; i++)
		printf("%d\n", nums[i]);
}
