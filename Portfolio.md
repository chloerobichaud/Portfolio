```python

```


```python
# Working with Numpy Arrays 
import numpy as np
np_positions = np.array(positions)
np_heights = np.array(heights)
gk_heights = np_heights[np_positions == 'GK']
other_heights = np_heights[np_positions != 'GK']
print("Median height of goalkeepers: " + str(np.median(gk_heights)))
print("Median height of other players: " + str(np.median(other_heights)))


```


```python


```


```python

```


```python

```
