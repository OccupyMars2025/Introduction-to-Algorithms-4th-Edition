To design an algorithm to sort \( n \) points in the unit disk by their distances from the origin using bucket sort with an average-case running time of \( \Theta(n) \), follow these steps:

### 1. **Understand the problem**

Each point \( p_i = (x_i, y_i) \) lies within the unit disk, i.e., \( 0 < x_i^2 + y_i^2 \leq 1 \). The task is to sort the points by their distance from the origin, where the distance \( d_i \) is given by:

\[
d_i = \sqrt{x_i^2 + y_i^2}
\]

Since the points are uniformly distributed, the probability of finding a point in any region of the disk is proportional to the area of that region. The distance \( d_i \) can range from 0 to 1, and the number of points is \( n \).

### 2. **Choosing the bucket sizes**

Since the points are uniformly distributed within the unit disk, we can utilize a bucket sort approach based on the distance from the origin. To sort the points efficiently, we need to map the distance values to buckets.

The square of the distance \( d_i^2 = x_i^2 + y_i^2 \) is uniformly distributed in the range \( [0, 1] \). We can then use \( d_i^2 \) to assign points to buckets, as the distribution of \( d_i^2 \) is uniform, which simplifies the sorting process.

### 3. **Bucket Sort Design**

#### Step 1: **Transform the problem**

Instead of sorting the distances \( d_i = \sqrt{x_i^2 + y_i^2} \), we sort the squared distances \( d_i^2 = x_i^2 + y_i^2 \). This transformation does not change the relative order of the points, and simplifies the comparison since the squared distances are easier to compute.

#### Step 2: **Define the number of buckets**

We will divide the squared distance range \( [0, 1] \) into \( m \) equal-sized intervals. The number of buckets \( m \) can be chosen as \( m = \Theta(n) \), so that the average number of points in each bucket is \( \Theta(1) \). This ensures the total time complexity is \( \Theta(n) \).

Each bucket corresponds to an interval of squared distances. Specifically, the \( k \)-th bucket will correspond to the interval:

\[
\left[ \frac{k-1}{m}, \frac{k}{m} \right)
\]

for \( k = 1, 2, \dots, m \).

#### Step 3: **Distribute points into buckets**

For each point \( p_i = (x_i, y_i) \), compute its squared distance \( d_i^2 = x_i^2 + y_i^2 \). The bucket index for this point is given by:

\[
\text{bucket index} = \left\lfloor m \cdot d_i^2 \right\rfloor
\]

Place the point in the corresponding bucket.

#### Step 4: **Sort within buckets**

Each bucket will contain points that fall within a small range of squared distances. Since the squared distances are uniformly distributed, the number of points in each bucket will be small on average. We can sort the points within each bucket using an efficient sorting algorithm, such as insertion sort, which works well when the number of elements is small. The sorting of each bucket takes \( O(1) \) on average.

#### Step 5: **Combine the results**

Finally, collect the points from the buckets in order of increasing squared distance and compute the original distances \( d_i = \sqrt{x_i^2 + y_i^2} \) for each point to obtain the sorted list of points.

### 4. **Time Complexity Analysis**

- **Distributing points into buckets**: Computing the squared distance for each point takes \( O(1) \), and assigning it to a bucket also takes \( O(1) \). Thus, distributing all \( n \) points into \( m \) buckets takes \( O(n) \).
  
- **Sorting within buckets**: Since there are \( m \) buckets, and the average number of points per bucket is \( O(1) \), sorting within each bucket takes \( O(1) \) on average. The total time for sorting within all buckets is \( O(n) \).

- **Combining results**: Collecting the points from the buckets and computing the distances takes \( O(n) \).

Thus, the total time complexity is:

\[
O(n) + O(n) + O(n) = O(n)
\]

Since we chose \( m = \Theta(n) \), the average-case running time is \( \Theta(n) \).

### 5. **Summary**

The algorithm works as follows:

1. Compute the squared distance \( d_i^2 = x_i^2 + y_i^2 \) for each point.
2. Distribute the points into \( m = \Theta(n) \) buckets based on the squared distances.
3. Sort the points within each bucket using an efficient algorithm like insertion sort.
4. Combine the sorted points from all buckets and compute the final distances.

This bucket-sort-based algorithm sorts the points by their distance from the origin in \( \Theta(n) \) average-case time.