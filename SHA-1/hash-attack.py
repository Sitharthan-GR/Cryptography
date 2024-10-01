import hashlib
import random
import string
import matplotlib.pyplot as plt
import numpy as np
import math
import datetime
def Sha1(message,nB):
    sha1_hash = hashlib.sha1(message.encode()).hexdigest()
    hex_length = nB // 4
    truncated_hash = sha1_hash[:hex_length]
    return truncated_hash


def generate_random_string(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    random_string = ''.join(random.choice(characters) for _ in range(length))
    return random_string


def collisionAttack(samples,nB):
    ComparedHash = []
    # atte
    rounds=0
    while True:
        rounds=rounds + 1
        message = generate_random_string(16)
        hash=Sha1(message,nB)
        if hash in ComparedHash:
            return rounds
        else:
            ComparedHash.append(hash)
        # else:
        #     print("collision not found")
        
        
        # print(message)
    return attempts


def preimageAttack(samples,nB):
    target_input="qwertyuiopasdfgh"
    # ComparedHash = []
    attempts=[]
    rounds=0
    while True:
        rounds=rounds + 1
        hash_target_input=Sha1(target_input,nB)
        message = generate_random_string(16)
        hash=Sha1(message,nB)
        if hash == hash_target_input:
            return rounds
        # else:
        #     ComparedHash.append(hash)
        # else:
        #     print("collision not found")
        
        
        # print(message)
    return attempts
 

def drawCollisionGraph(collision_data,expected_collision_attempts):
    data_lists = [values for values in collision_data.values()]

    # Calculate the average of each array in whiskey_data
    averages = [np.mean(values) for values in collision_data.values()]

    # Convert the dictionary keys to strings for labeling
    labels = [str(key) for key in collision_data.keys()]



    
    plt.figure(figsize=(12, 6))
    plt.boxplot(data_lists, labels=labels)
    plt.xlabel('No of bits')
    plt.ylabel('Attempts (log scale)')
    plt.title('Collision Attack')
    plt.yscale("log")  # Set the y-axis to logarithmic scale

    x_values = np.arange(1, len(labels) + 1)  # Adjust x-coordinates
   
    plt.plot(x_values, expected_collision_attempts, marker='o', linestyle='-', color='r', label='Expected number of iterations')
    plt.legend()

    #for displaying the averages value
    for i, avg in enumerate(averages):
        color = 'b'
        plt.annotate(f'Avg: {avg:.2f}', (x_values[i], avg), textcoords="offset points", xytext=(0, 15), ha='center', color='b',label='Averages')
   
    # plt.legend(color, legend_labels, loc='upper right')
    # Show the plot
    # blue_avg_value = ave]
    # blue_avg_index = averages.index(min(averages))
    # blue_avg_value = averages[blue_avg_index]
    # plt.text(x_values[blue_avg_index], blue_avg_value, 'Average', color='b', ha='right', va='bottom')

    plt.grid(True)
    plt.show()

def calculate_collsion_expected_iterations(bit_size):
    val=[]
    for bit  in bit_size:
        expected_iterations = 1.1774 * math.pow(2, bit / 2)
        val.append(expected_iterations)
    return val


def calculate_preimg_expected_iterations(bit_size):
    val=[]
    for bit  in bit_size:
        expected_iterations = math.pow(2, bit)
        val.append(expected_iterations)
    
    return val


def drawPreimgGraph(preimg_data,expected_preimg_attempts):
    data_lists = [values for values in preimg_data.values()]


    averages = [np.mean(values) for values in preimg_data.values()]

 
    labels = [str(key) for key in preimg_data.keys()]




    plt.figure(figsize=(12, 6))
    plt.boxplot(data_lists, labels=labels)
    plt.xlabel('No of bits')
    plt.ylabel('Attempts (log scale)')
    plt.title('Preimage Attack')
    plt.yscale("log")  

    x_values = np.arange(1, len(labels) + 1)  

    plt.plot(x_values, expected_preimg_attempts, marker='o', linestyle='-', color='r', label='Expected number of iterations')
    plt.legend()


    for i, avg in enumerate(averages):
        plt.annotate(f'Avg: {avg:.2f}', (x_values[i], avg), textcoords="offset points", xytext=(0, 15), ha='center', color='b',label='Averages')
   

    # Show the plot
    plt.grid(True)
    plt.show()
        

def main():
    # print("Start time:", datetime.datetime.now())
    # bit_sizes = [8,10]
    bit_sizes = [8,10,12,14,16,17,18,19]
    # bit_sizes = [8, 10, 12, 14, 16, 18, 20, 22]
    expected_collision_attempts=calculate_collsion_expected_iterations(bit_sizes)
    expected_preimg_attempts=calculate_preimg_expected_iterations(bit_sizes)
    samples=50
    col_dataset={}
    preimg_dataset={}    
    for i in range (len(bit_sizes)):

        col_attempts=[]
        preimg_attempts=[]
        for sample in range (samples):
            success_col_attempts = collisionAttack(samples,bit_sizes[i])
            col_attempts.append(success_col_attempts)
            
            success_preimg_attempts= preimageAttack(samples,bit_sizes[i])
            preimg_attempts.append(success_preimg_attempts)
        col_dataset[bit_sizes[i]]=col_attempts
        preimg_dataset[bit_sizes[i]]=preimg_attempts

        # print(f"successful preimage attack attempts for {nB} bits of {samples} are {success_preimg_attempts}")
    # print(f"\nsuccessful collision attack attempts for bits of {col_dataset} ")
    drawCollisionGraph(col_dataset,expected_collision_attempts)       
    drawPreimgGraph(preimg_dataset,expected_preimg_attempts)
    # print(f"\nsuccessful preimg attack attempts for bits of {preimg_dataset} ")
    # print("End time:", datetime.datetime.now())      



if __name__ == "__main__":
    main()



# successful collision attack attempts for bits of [1487, 985, 646, 1097, 531, 1034, 2735, 1215, 2571, 880, 342, 597, 2672, 1226, 1545, 534, 2122, 1982, 1727, 1871, 1562, 2309, 464, 714, 1120, 1989, 796, 1282, 1390, 350, 1585, 1252, 628, 1220, 874, 2273, 1576, 607, 1110, 2069, 1606, 1276, 2121, 1226, 1229, 939, 770, 364, 956, 1847] 
# successful preimg attack attempts for bits of [1146526, 1066931, 231302, 282081, 903677, 642036, 3062595, 359501, 4816442, 957398, 940840, 156258, 92194, 521846, 292232, 947271, 141203, 586033, 171336, 862908, 1026176, 1908263, 1186219, 267838, 440365, 524316, 1839881, 468669, 485936, 775373, 429767, 2846477, 308159, 1862874, 3283459, 6862867, 182028, 292944, 438871, 266954, 2251601, 897074, 389431, 118601, 306984, 667443, 1865788, 296076, 7934188, 1839550] 