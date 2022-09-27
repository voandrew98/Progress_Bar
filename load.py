import time
import tqdm #utilized to create progress bars or meters

counter = 0

for i in tqdm.tqdm(range(100)): #adjust integer within parantheses for specific percentage
    counter += i
    time.sleep(0.4) # only for test

print(f'{counter = }')