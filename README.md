# CSE 571 Homework 3
For the homework 3, we're going to implement motion planning methods: A*, RRT, RRT*.
For the details, please check the [homework 3 pdf file](https://courses.cs.washington.edu/courses/cse571/21sp/homeworks/hw3.pdf). 


## Rules ##
1. You may only modify the files we mention (those in the [submit.sh](submit.sh) script). We will not grade files outside of these.
1. You may not change the signatures or return types of functions or you will fail our tests. 
   You may add object fields (e.g. `self.data`) or helper functions within the files.
1. You may talk with others about the homework, but you must implement by yourself.
1. Feel free to test as you go and modify whatever you want, but we will only grade the files from [submit.sh](submit.sh).


## Environment setup ##
As you did in [Homework 0](https://github.com/fishbotics/uw-robotics-571-sp21/#homework-0-setup-conda-and-the-codebase), 
you may use the same `conda` environment `robotics-class`.   
In this case, we are using a different repo and not creating a new environment:

```bash
git clone https://github.com/rohjunha/cse571-hw3.git
cd cse571-hw3
conda deactivate
conda activate robotics-class
```

Before starting the homework, you will first need to update the repository to get the new files.
Note that the branch in this repository is called `main` (https://github.com/github/renaming).
```bash
git add -A
git commit -m "before starting new homework"
git pull origin main
```


## Notes ##
1. Every planner returns `PlanResult` instance from `plan` function. Please check if you return the actual values (including elapsed time) in the `PlanResult` instance. This may be used in grading.
1. Do not implement and use a custom sampling or random function other than the provided functions 
   ([MapEnvironment.sample](https://github.com/rohjunha/cse571-hw3/blob/main/environments/MapEnvironment.py#L29-L36),
   [CarEnvironment.sample](https://github.com/rohjunha/cse571-hw3/blob/main/environments/CarEnvironment.py#L40-L49)).
   Using a custom sampling or random function may cause problems in grading.


## Turn it in ##
Run the `submit.sh` script by running:

```bash
bash submit.sh
```

This will create the file `submit.zip` in your directory with all the code you need to submit.
Submit `submit.zip` to `Homework 3 (Programming problems)` at [gradescope](https://gradescope.com).
