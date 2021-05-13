# CSE 571 Homework 3
For the homework 3, we're going to implement motion planning methods: A*, RRT, RRT*.
For the details, please check the [homework 3 pdf file](https://courses.cs.washington.edu/courses/cse571/21sp/homeworks/hw3.pdf). 


## Rules ##
1. You may only modify the files we mention (those in the [submit.sh](submit.sh) script). We will not grade files outside of these.
1. You may not change the signatures or return types of functions or you will fail our tests. 
   You may add object fields (e.g. `self.data`) or helper functions within the files.
1. You may talk with others about the homework, but you must implement by yourself.
1. Feel free to test as you go and modify whatever you want, but we will only grade the files from [submit.sh](submit.sh).


## Notes ##
1. Every planner returns `PlanResult` instance from `plan` function. Please check if you return the actual values (including elapsed time) in the `PlanResult` instance. This may be used in grading.


## Turn it in ##
Run the `submit.sh` script by running:

```bash
bash submit.sh
```

This will create the file `submit.zip` in your directory with all the code you need to submit.
Submit `submit.zip` to `Homework 3 (Programming problems)` at [gradescope](https://gradescope.com).
