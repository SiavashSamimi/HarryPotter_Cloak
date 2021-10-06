# HarryPotter_Cloak
## ***Requirements***  
- Python 3.5 or above
- opencv 4.0 or above
### Create Anaconda env:
```bash
conda create --name <name of env>
```
### Install Requirements by conda or pip After Activate env:
```bash
conda install python
pip install opencv-python

```
# Run:
first, run the 
``` python 
python mask.py
```
for to make a mask that matches the color of the cape
and save the color range array with the  's'  key in current path.
then run the 
```python
python HarryPotter_cloak.py --input webcam
```
### ***Notice:*** 
When the webcam is turned on, the initial input frame should be a motionless frame, meaning you are not standing in front of it.

then you can stand in front of the webcam with your cape.
