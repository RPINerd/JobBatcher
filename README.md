# Universal Job Batcher

A python script/module to execute any generic terminal command or python script in a distributed manner to utilize all available CPU cores.

## Project Goal

Input will be a function or script to be executed, a list of static arguments to be passed, and a collection of "items" to run the script on. The script will execute the function/script for each item in the collection such that as many CPU cores as desired are running the jobs

### Key Functional Points

- Provide a way to specify the number of cores to be used for execution
- Inspect local machine for max number of cores and use that as default
- Be aware of applications that are being passed a "-t" or "--threads" argument and adjust the number of cores used accordingly
- Modularize so that incorporation can be as simple as "import JobBatcher as jb" and then "jb.run(function, args, items)"
