import numpy as np
points = np.random.randint(1000,size =(1000,2))
centers = np.random.randint(1000,size=(3,2))
print(centers)

new_centers = np.random.randint(1000,size=(3,2))
print(new_centers)
labels = [[],[],[]]

def nn(centers):
    centers = new_centers
    print("old centers " ,  centers)
    for point in points:
        ds = np.linalg.norm(point - centers, axis =1)
        labels[np.argmin(ds, axis=0)].append(point)

    for i in range(3):   
        new_centers[i] = np.mean(np.array(labels[i]), axis = 0).astype(int)
    print("new centers ", new_centers)
    return centers, new_centers

def changed_centers(centers,new_centers):
    # sum_ds = 0
    # for i in range(3):
    #    sum_ds += np.linalg.norm(centers[i] - new_centers[i])
    return np.sum(np.linalg.norm(centers - new_centers))

while changed_centers(centers,new_centers) > 10:  
    centers, new_centers = nn(centers)
    