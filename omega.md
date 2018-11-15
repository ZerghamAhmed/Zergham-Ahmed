# Omega Directive

## Questions

6.1. Selection sort has to do with choosing the correct element in one scan. Whereas, bubble sort
is when you compare and swap every adjacent element. The best case for bubble sort would be if the numbers
,for example, 12345 were already in ascending order that we wanted them to be. The first element 1, would be compared
with the second element 2, and since 1 is less than two there will be no swaps. This will repeat for 2 and 3, etc.for an
order of n.

Keeping the example of 12345 with ascending order, selection sort would work by scanning the numbers after 1 and seeing that they
are each greater than 1. Then, moving on to 2 and scanning 3,4,5 to see they are smaller than 2. Then, this would repeat 3 more times, so
we see that it is an order of n^2 even in the best senerio where the numbers are already in ascending order.

6.2. This is because the problem keeps being divided up so that each division has a
maximum comparison of n/2. This does not matter whether the numbers are already arranged since
it would still be divided and compared n/2 each division.


6.3. Because the worst case and best case are the same since the length of
the string will always be that number. The program simply goes through each number
and counts it as 1, then totals it to give the strlen.

6.4. Since a list is an object it keeps track of its own length as it is being created and then we can
access it in constant time.

6.5. isupper works on char* arrays which are contiguously stored in memory, so it can be traversed in constant time.

## Debrief

a. Bubble sorting
https://www.youtube.com/watch?v=ds_4wTSYd8k

Merge sort
https://stackoverflow.com/questions/7801861/why-is-merge-sort-worst-case-run-time-o-n-log-n
https://medium.com/karuna-sehgal/a-simplified-explanation-of-merge-sort-77089fe03bb2

Complexity of len(list)
https://www.reddit.com/r/learnpython/comments/752zbp/why_is_the_complexity_of_lenlist_o1/

list
https://stackoverflow.com/questions/1115313/cost-of-len-function


b. 50 minutes
