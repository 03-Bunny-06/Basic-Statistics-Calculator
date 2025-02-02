#Basic Statistics Calculator
import numpy as np

def basic_stat_calculator(data):
    arr_data = np.array(data)

    print('---Basic Statistics Calculator---\n1. Mean\n2. Median\n3. Variance\n4. Standard Deviation\n5. Sort the Array\n6. All the above operations\n7. Exit')

    def mean():
        mean_data = np.mean(arr_data)
        return mean_data
    
    def median():
        median_data = np.median(arr_data)
        return median_data
    
    def variance():
        variance_data = np.var(arr_data)
        return f'{variance_data:.2f}'

    def standard_deviation():
        std_data = np.std(arr_data)
        return f'{std_data:.2f}'

    def sort():
        sort_data = np.sort(arr_data)
        return sort_data
    
    z = True
    while z:
        i = input('Enter the option to proceed: ')
        if i == '1':
            print(f'The mean of the array is: {mean()}')
        elif i == '2':
            print(f'The median of the array is: {median()}')
        elif i == '3':
            print(f'The variance of the array is: {variance()}')
        elif i == '4':
            print(f'The standard deviation of the array is: {standard_deviation()}')
        elif i == '5':
            print(f'The sorted array is: {sort()}')
        elif i == '6':
            print(f'The mean of the array is: {mean()}')
            print(f'The median of the array is: {median()}')
            print(f'The variance of the array is: {variance()}')
            print(f'The standard deviation of the array is: {standard_deviation()}')
            print(f'The sorted array is: {sort()}')
        elif i == '7':
            print('Exiting the calculator....\nThanks for using our calci!')
            z = False
        else:
            print('Enter a valid option.')

data = list(map(int,input('Enter space seperated integers (Ex: 1 2 3 4 5 6): ').split()))
basic_stat_calculator(data)