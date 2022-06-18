# Investigation of sorting algorithms

## Quick sort

Quick sort fails when it exceeds maximum recursion, which happens when the list is nearly sorted or there are many repeated values. 

This plot shows the boundary between where quick sort succeeds and fails, based on the list length and the sample size. The failure here is due to too many repeated values. 

<img src="./images/qsort_failure_boundary.png" alt="drawing" width="400"/>

The runtime is longer where as there are more repeated values, even when the quick sort eventually succeeds. 

<img src="./images/qsort_efficiency_near_failure.png" alt="drawing" width="400"/>

## Radix sort

...

<img src="./images/radix_efficiency.png" alt="drawing" width="600"/>

## Merge sort

...

<img src="./images/merge_efficiency.png" alt="drawing" width="600"/>