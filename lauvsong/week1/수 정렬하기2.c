/* merge sort */
#define MAX 1000000
#include <stdio.h>
int nums[MAX];
void merge(int left, int mid, int right) {
	int low = left, high = mid + 1;
	int i = left;
	int arr[MAX];
	while (low <= mid && high <= right) {
		if (nums[low] < nums[high])
			arr[i++] = nums[low++];
		else
			arr[i++] = nums[high++];
	}
	if (low > mid)
		while (high <= right) arr[i++] = nums[high++];
	else
		while (low <= mid) arr[i++] = nums[low++];
	for (int i = left; i <= right; i++)
		nums[i] = arr[i];
}

void mergeSort(int left, int right) {
	int mid = (left + right) / 2;
	if (left < right) {
		mergeSort(left, mid);
		mergeSort(mid + 1, right);
		merge(left, mid, right);
	}
}

int main() {
	int n;
	scanf("%d", &n);
	for (int i = 0; i < n; i++)
		scanf("%d", &nums[i]);
	mergeSort(0, n - 1);
	for (int i = 0; i < n; i++)
		printf("%d\n", nums[i]);
}
