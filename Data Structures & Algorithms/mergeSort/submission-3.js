class Solution {
    // Time Complexity – O(N log N)
    // Space Complexity – O(N)
    mergeSort(pairs) {
        const aux = new Array(pairs.length);

        const merge = (s, m, e) => {
            for (let k = s; k <= e; k++) aux[k] = pairs[k];

            let left = s;
            let right = m + 1;

            for (let k = s; k <= e; k++) {
                if (left > m) {
                    pairs[k] = aux[right++];
                } else if (right > e) {
                    pairs[k] = aux[left++];
                } else if (aux[left].key <= aux[right].key) {
                    pairs[k] = aux[left++];
                } else {
                    pairs[k] = aux[right++];
                }
            }
        }

        const sort = (s, e) => {
            if (s >= e) return;

            const m = Math.floor((s + e) / 2);

            sort(s, m);
            sort(m + 1, e);

            merge(s, m, e);
        }

        sort(0, pairs.length - 1);
        
        return pairs;
    }
}