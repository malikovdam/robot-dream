## Algorithm (v1.0)

### I. Read data in simulation loop

At first I created two variables:
```python
isBlocked = False
last_spike_time = 0
```
First variable is answering for 'ready state' of algorithm to 'eat' new data. And the second one `last_spike_time` helps us to change the flag state.  
Of course we can use only `last_spike_time`. But in the future I guess we will use buffer of data files (for example if we read one file and next file on the way).

Check, if we ready to read new data. Comparison of the `last_spike_time` with `t` shows us whether the interval has ended. Then try to find data file with `filename` name. If we find nothing, then skip steps and start a new iteration of the simulation.

```python
for t in np.arange(0, T, dt):
	if last_spike_time <= t:
		isBlocked = False
	if not isBlocked:
		if os.path.isfile(filename):
```

### II. Convert data to spike times
Open file, read data (it is one line) and put it into list of intervals. I added the coefficient (dividing by 100) to decrease the simulation time.
```python
with open(filename, 'r') as f:
	intervals = [float(time) / 100 for time in f.readline().split(" ")]
```

Then start to transfer it to a spike times list. The first interval will start from `t`.
```python
intervals[0] += t
```

Next, add current interval value to the previous.
```python
for i in xrange(1, len(intervals)):
	intervals[i] += intervals[i - 1]
```

Update variable
```python       
last_spike_time = intervals[-1]
```

### III. Create and connect a generator

First of all we should create one spike generator, and then change its status by new data.
```python     
generator = nest.Create('spike_generator', 1)
nest.SetStatus(generator, {'spike_times': intervals, 'spike_weights': [100. for i in intervals]})
```

For example connect to the first neuron of the column:
```python 
nest.Connect(generator, (Cortex[L4][L4_Glu0][column][0],) )
```

After this, change state of flag, delete old intervals and rename old data file (mark that it have been read)
```python 
isBlocked = True
del intervals
os.rename(filename, filename + "_done")
```

Continue simulation with new generator behaviour.
```python 
nest.Simulate(dt)
```

### Full code
```python 
isBlocked = False
last_spike_time = 0

for t in np.arange(0, T, dt):
    if last_spike_time <= t:
        isBlocked = False
    if not isBlocked:
        if os.path.isfile(filename):
            with open(filename, 'r') as f:
                intervals = [float(time) / 100 for time in f.readline().split(" ")]

            intervals[0] += t
            for i in xrange(1, len(intervals)):
                intervals[i] += intervals[i - 1]

            last_spike_time = intervals[-1]
            generator = nest.Create('spike_generator', 1)
            nest.SetStatus(generator, {'spike_times': intervals, 'spike_weights': [100. for i in intervals]})

            nest.Connect(generator, (Cortex[L4][L4_Glu0][column][0],) )

            isBlocked = True
            del intervals
            os.rename(filename, filename + "_done")
    nest.Simulate(dt)
```
