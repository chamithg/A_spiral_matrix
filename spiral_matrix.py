class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        output =[]
        
        if not matrix:
            return output
        
        if len(matrix[0]) ==1:
            for each in matrix:
                output.append(each[0])
            return output
        
        if len(matrix) ==1:
            for each in matrix[0]:
                output.append(each)
            return output
        
        def run(arr):
            i = 0
            j = 0
            
            if i == 0:
                    for each in arr[i]:
                        output.append(each)
                    i += 1
                    j = len(arr[0])-1
            while i > 0 and i < len(arr)-1 and j == len(arr[0])-1 and arr[i] != []: 
                output.append(arr[i][j])
                arr[i].pop()
                i+=1
            
            if i == len(arr)-1:
                    for each in arr[i][::-1]:
                        output.append(each)
                    i -= 1
                    j = 0
            
            while i > 0 and i < len(arr)-1 and j == 0 and arr[i] != []:
                output.append(arr[i][j])
                arr[i].pop(0)
                i -=1
            arr.pop(0)
            if arr:    
                arr.pop()
            if arr:
                run(arr)   
            
            print(matrix)       
                                    
        run(matrix)
        
        return output
    
obj = Solution()
matrix = [[1,2,3],[4,5,6],[7,8,9]]
matrix1 = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]

##[1,2,3,4,8,12,11,10,9,5,6,7]
## [1, 2, 3, 4, 7, 12, 11, 10, 9, 5, 6, 7]
print(obj.spiralOrder(matrix1))