function bubbleSort(arr) {
    let n = arr.length;
    let swapped;
    do {
        swapped = false;
        for (let i = 1; i < n; i++) {
            if (arr[i - 1] > arr[i]) {
                // Swap elements
                let temp = arr[i - 1];
                arr[i - 1] = arr[i];
                arr[i] = temp;

                swapped = true;
            }
        }
        // Reduce n because the last element is already in place
        n--;
    } while (swapped);
    return arr;
}

// Example usage:
const arr = [64, 34, 25, 12, 22, 11, 90];
console.log("Sorted array:", bubbleSort(arr));
