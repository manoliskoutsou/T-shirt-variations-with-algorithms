import random

shirt_list = []
dummy_tshirt_list = []

'''T-shirt with different prices for color, size and fabric'''
class TShirt:
    
    color = sorted(['red','orange','yellow','green','blue','indigo','violet']) 
    size = sorted(['xs','s','m','l','xl','xxl','xxxl'])
    fabric = sorted(['wool','cotton','polyester','rayon','linen','cashmere','silk'])
    
    def __init__(self, t_color=None, t_size=None, t_fabric=None):
        self._t_color = t_color
        self._t_size = t_size
        self._t_fabric = t_fabric
        
    #Dummie data for T-shirts
        if t_color is None:    
            self._t_color = self.color[random.randrange(len(self.color))]
            self._t_color = self.color.index(self._t_color)
             
        if t_size is None:
            self._t_size = self.size[random.randrange(len(self.size))]
            self._t_size = self.size.index(self._t_size)

        if t_fabric is None:
            self._t_fabric = self.fabric[random.randrange(len(self.fabric))]
            self._t_fabric = self.fabric.index(self._t_fabric)
            
    def __str__(self):
        return f"T-Shirt  Size: {self.size[self._t_size]} , Color: {self.color[self._t_color]} , Fabric: {self.fabric[self._t_fabric]}."
    
    '''function for checking if feature of t-shirt1 is greater than feature of t-shirt2.'''    
    def greaterThan(self, tshirt2, feature): 
        if type(feature) == list:
            for feat in feature:
                if getattr(self, feat) > getattr(tshirt2, feat):
                    return True
                elif getattr(self, feat) < getattr(tshirt2, feat):
                    return False
            return False
        else:
            return getattr(self, feature) > getattr(tshirt2, feature)
            
    '''function for checking if feature of t-shirt1 is greater than or equal to feature of t-shirt2.'''
    def greaterThanEqual(self, tshirt2, feature): 
        if type(feature) == list:
            for featIndex, feat in enumerate(feature):
                if getattr(self, feat) > getattr(tshirt2, feat):
                    return True
                elif getattr(self, feat) < getattr(tshirt2, feat):
                    return False
                elif getattr(self, feat) == getattr(tshirt2, feat) and featIndex == (len(feature) - 1):
                    return True
            return False
        else:
            return getattr(self, feature) >= getattr(tshirt2, feature)

    '''function for checking if feature of t-shirt1 is less than feature of t-shirt2.'''    
    def lessThan(self, tshirt2, feature):
        if type(feature) == list:
            for feat in feature:
                if getattr(self, feat) < getattr(tshirt2, feat):
                    return True
                elif getattr(self, feat) > getattr(tshirt2, feat):
                    return False
            return False
        else:
            return getattr(self, feature) < getattr(tshirt2, feature)

    '''function for checking if feature of t-shirt1 is less than or equal to feature of t-shirt2.'''    
    def lessThanEqual(self, tshirt2, feature):
        if type(feature) == list:
            for featIndex, feat in enumerate(feature):
                if getattr(self, feat) < getattr(tshirt2, feat):
                    return True
                elif getattr(self, feat) > getattr(tshirt2, feat):
                    return False
                elif getattr(self, feat) == getattr(tshirt2, feat) and featIndex == (len(feature) - 1):
                    return True
            return False
        else:
            return getattr(self, feature) <= getattr(tshirt2, feature)

    '''get number of buckets for bucketSorting'''
    def bucketsNum(features):
        featureToArray = {'_t_color':TShirt.color,'_t_size':TShirt.size,'_t_fabric':TShirt.fabric}
        return len(featureToArray[features[0]])
    
    '''get bucket index for bucketSorting'''
    def toIndex(self,features, asc=True):
        featureToArray = {'_t_color':TShirt.color,'_t_size':TShirt.size,'_t_fabric':TShirt.fabric}
        if asc:
            return getattr(self, features[0])
        else:
            return (len(featureToArray[features[0]]) - 1) - getattr(self, features[0])
        
    @staticmethod
    def setPrice():
        total_price = TShirt.color_price + TShirt.size_price + TShirt.fabric_price
        return total_price

    

class Algorithms:
    '''BucketSort Algorithm'''
    def insertionSort(b,features,asc=True):
        for i in range(1, len(b)):
            up = b[i]
            j = i - 1
            while ( j >= 0 and b[j].greaterThan(up,features) and  asc) or (j >= 0 and b[j].lessThan(up,features) and not asc): 
                b[j + 1] = b[j]
                j -= 1
            b[j + 1] = up    
        return b    

    def bucketSort(x, features, asc=True): 
        slot_num = TShirt.bucketsNum(features) 
        arr = [[] for i in range(slot_num)]
        
        for j in x:
            index_b = j.toIndex(features, asc)
            arr[index_b].append(j)
        
        for i in range(len(arr)):
            arr[i] = Algorithms.insertionSort(arr[i],features,asc)
            
        k = 0
        for i in range(len(arr)):
            for j in range(len(arr[i])):
                x[k] = arr[i][j]
                k += 1
        return x

    '''BubbleSort Algorithm'''
    def bubbleSort(data,features,asc=True):
        n = len(data)
        for i in range(n-1):
            for j in range(0,n-i-1):
                if (data[j].greaterThan(data[j+1],features) and asc) or (data[j].lessThan(data[j+1],features) and not asc): 
                    data[j], data[j+1] = data[j+1], data[j]

    '''Quick sort algorithm'''
    def partition(array, features, asc, start, end):
        pivot_index = start 
        pivot = array[pivot_index]
        while start < end:
            while start < len(array) and ((array[start].lessThanEqual(pivot,features) and asc) or (array[start].greaterThanEqual(pivot,features) and not asc)):
                start += 1
            while (array[end].greaterThan(pivot,features) and asc) or (array[end].lessThan(pivot,features) and not asc):
                end -= 1
            if(start < end):
                array[start], array[end] = array[end], array[start]
        array[end], array[pivot_index] = array[pivot_index], array[end]
        return end
      
    def quick_sort(array, features, asc=True, start=0, end=None):
        if end is None: end = len(array)-1
        if (start < end):
            p = Algorithms.partition(array, features, asc, start, end)
            Algorithms.quick_sort(array, features, asc, start, p - 1)
            Algorithms.quick_sort(array, features, asc, p + 1, end)

        
class Call(TShirt, Algorithms):
    def bubble_sort(shirts_list):
        if len(shirts_list) == 0:            
            print('You have to create the dummy list first in order to continue!\n')
        else:
            for case in range(1,9):
                if case == 1:#Size in ascending
                    features=['_t_size']
                    Algorithms.bubbleSort(shirts_list,features)
                    print('Size in ascending order using BubbleSort Method!')
                    print('')
                elif case == 2:#Size in descending
                    features=['_t_size']
                    Algorithms.bubbleSort(shirts_list,features,asc=False)
                    print('Size in descending order using BubbleSort Method!')
                    print('')
                elif case == 3:#Color in ascending
                    features=['_t_color']
                    Algorithms.bubbleSort(shirts_list,features)
                    print('Color in ascending order using BubbleSort Method!')
                    print('')
                elif case == 4:#Color in descending
                    features=['_t_color']
                    Algorithms.bubbleSort(shirts_list,features,asc=False)
                    print('Color in descending order using BubbleSort Method!')
                    print('')
                elif case == 5:#Fabric in ascending
                    features=['_t_fabric']
                    Algorithms.bubbleSort(shirts_list,features)
                    print('Fabric in ascending order using BubbleSort Method!')
                    print('')
                elif case == 6:#Fabric in descending
                    features=['_t_fabric']
                    Algorithms.bubbleSort(shirts_list,features,asc=False)
                    print('Fabric in descending order using BubbleSort Method!')
                    print('')
                elif case == 7:#Size and Color and Fabric in ascending
                    features=['_t_size','_t_color','_t_fabric']
                    Algorithms.bubbleSort(shirts_list,features)
                    print('Size, Color and Fabric in ascending order using BubbleSort Method!')
                    print('')
                elif case == 8:#Size and Color and Fabric in descending
                    features=['_t_size','_t_color','_t_fabric']
                    Algorithms.bubbleSort(shirts_list,features,asc=False)
                    print('Size, Color and Fabric in descending order using BubbleSort Method!')
                    print('')
                x=1
                for shirt in shirts_list:
                    print(f"{x}: {shirt}")
                    x=x+1
                print()
        
    def bucket_sort(shirts_list):
        if len(shirts_list) == 0:            
            print('You have to create the dummy list first in order to continue!\n')
        else:
            for case in range(1,9):
                if case == 1:#Size in ascending
                    features=['_t_size']
                    Algorithms.bucketSort(shirts_list,features,asc=True)
                    print('Size in ascending order using BucketSort Method!')
                    print('')
                elif case == 2:#Size in descending
                    features=['_t_size']
                    Algorithms.bucketSort(shirts_list,features,asc=False)
                    print('Size in descending order using BucketSort Method!')
                    print('')
                elif case == 3:#Color in ascending
                    features=['_t_color'] 
                    Algorithms.bucketSort(shirts_list,features)
                    print('Color in ascending order using BucketSort Method!')
                    print('')
                elif case == 4:#Color in descending
                    features=['_t_color']
                    Algorithms.bucketSort(shirts_list,features,asc=False)
                    print('Color in descending order using BucketSort Method!')
                    print('')
                elif case == 5:#Fabric in ascending
                    features=['_t_fabric']
                    Algorithms.bucketSort(shirts_list,features)
                    print('Fabric in ascending order using BucketSort Method!')
                    print('')
                elif case == 6:#Fabric in descending
                    features=['_t_fabric']
                    Algorithms.bucketSort(shirts_list,features,asc=False)
                    print('Fabric in descending order using BucketSort Method!')
                    print('')
                elif case == 7:#Size and Color and Fabric in ascending
                    features=['_t_size','_t_color','_t_fabric']
                    Algorithms.bucketSort(shirts_list,features)
                    print('Size, Color and Fabric in ascending order using BucketSort Method!')
                    print('')
                elif case == 8:#Size and Color and Fabric in descending
                    features=['_t_size','_t_color','_t_fabric']
                    Algorithms.bucketSort(shirts_list,features,asc=False)
                    print('Size, Color and Fabric in descending order using BucketSort Method!')
                    print('')
                x=1
                for shirt in shirts_list:
                    print(f"{x}: {shirt}")
                    x=x+1
                print()
    
    def quick_sort(shirts_list):
        if len(shirts_list) == 0:            
            print('You have to create the dummy list first in order to continue!\n')
        else:
            for case in range(1,9):
                if case == 1:#Size in ascending
                    features=['_t_size']
                    Algorithms.quick_sort(shirts_list,features)
                    print('Size in ascending order using QuickSort')
                    print('')
                elif case == 2:#Size in descending
                    features=['_t_size']
                    Algorithms.quick_sort(shirts_list,features,asc=False)
                    print('Size in descending order using QuickSort')
                    print('')
                elif case == 3:#Color in ascending
                    features=['_t_color']
                    Algorithms.quick_sort(shirts_list,features)
                    print('Color in ascending order using QuickSort')
                    print('')
                elif case == 4:#Color in descending
                    features=['_t_color']
                    Algorithms.quick_sort(shirts_list,features,asc=False)
                    print('Color in descending order using QuickSort')
                    print('')
                elif case == 5:#Fabric in ascending
                    features=['_t_fabric']
                    Algorithms.quick_sort(shirts_list,features)
                    print('Fabric in ascending order using QuickSort')
                    print('')
                elif case == 6:#Fabric in descending
                    features=['_t_fabric']
                    Algorithms.quick_sort(shirts_list,features,asc=False)
                    print('Fabric in descending order using QuickSort')
                    print('')
                elif case == 7:#Size and Color and Fabric in ascending
                    features=['_t_size','_t_color','_t_fabric']
                    Algorithms.quick_sort(shirts_list,features)
                    print('Size, Color and Fabric in ascending order using QuickSort')
                    print('')
                elif case == 8:
                    features=['_t_size','_t_color','_t_fabric']
                    Algorithms.quick_sort(shirts_list,features,asc=False)
                    print('Size, Color and Fabric in descending order using QuickSort')
                    print('')
                x=1
                for shirt in shirts_list:
                    print(f"{x}: {shirt}")
                    x=x+1
                print()
                
    @staticmethod           
    def createDummyData(dummy_tshirt_list):
        if len(dummy_tshirt_list) == 0: 
            tshirts_list = [TShirt() for i in range(40)]
            print()
            x=1
            for shirt in tshirts_list:
                x=x+1
                dummy_tshirt_list.append(shirt)
            print('Dummy List Created Succesfully!\n')
        else:
            print('Dummy List allready exists!\n')

    
    @staticmethod
    def listBeforeSort(dummy_tshirt_list):
        if len(dummy_tshirt_list) == 0:
            print('You have to create the dummy list first in order to continue!\n')
        else:
            x=1
            for shirt in dummy_tshirt_list:
                print(f"{x}: {shirt}")
                x=x+1
                


'''menu : Variations of t-shirt with different sorting''' 
def menu():
    print ("1 Create Dummy Data ")
    print ("2 View list of 40 items before sorting ")
    print ("3 Use Bubble-Sort Method")
    print ("4 Use Bucket-Sort Method") 
    print ("5 Use Quick-Sort Method")  
    print ("6 Quit")
    
    while True:
        try:
            choice = int(input("Please pick a choice : "))
            if choice == 1 :
                Call.createDummyData(dummy_tshirt_list)
                menu()
            elif choice == 2 :
                Call.listBeforeSort(dummy_tshirt_list)
                menu()
            elif choice ==  3 :
                Call.bubble_sort(dummy_tshirt_list)
                menu()
            elif choice == 4 :
                Call.bucket_sort(dummy_tshirt_list)
                menu()
            elif choice == 5 :
                Call.quick_sort(dummy_tshirt_list)
                menu()
            elif choice == 6 :
                exit()
            else:
                print("Invalid Selection! Please Try Again!")
                menu()
        except ValueError:
            print("No valid integer! Please try again")
            menu()
            
menu()



                               







