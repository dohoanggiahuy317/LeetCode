class Solution:
    def resultGrid(self, image: List[List[int]], threshold: int) -> List[List[int]]:
        def check_d_x(i, j):
            nonlocal d_x
            if (j-1, i) not in d_x:
                if abs(image[i][j-1] - image[i][j]) > threshold:
                    d_x[(j-1, i)] = False
                else:
                    d_x[(j-1, i)] = True
            if (j, i) not in d_x:
                if abs(image[i][j] - image[i][j+1]) > threshold:
                    d_x[(j, i)] = False
                else:
                    d_x[(j, i)] = True  
                    
        def check_d_y(i, j):
            nonlocal d_y
            if (j, i-1) not in d_y:
                if abs(image[i-1][j] - image[i][j]) > threshold:
                    d_y[(j, i-1)] = False
                else:
                    d_y[(j, i-1)] = True
            if (j, i) not in d_y:
                if abs(image[i][j] - image[i+1][j]) > threshold:
                    d_y[(j, i)] = False
                else:
                    d_y[(j, i)] = True 
            
            
            
        reg_center = {}
        d_x = {}
        d_y = {}
        
        for i in range(1, len(image) - 1):
            for j in range(1, len(image[0]) - 1):
                check_d_x(i-1, j)
                check_d_x(i, j)
                check_d_x(i+1, j)

                check_d_y(i, j-1)
                check_d_y(i, j)
                check_d_y(i, j+1)
                
                
        for i in range(1, len(image) - 1):
            for j in range(1, len(image[0]) - 1):
                if (d_x[(j-1, i-1)] and 
                    d_x[(j, i-1)] and 
                    d_x[(j-1, i)] and 
                    d_x[(j, i)] and 
                    d_x[(j-1, i+1)] and 
                    d_x[(j, i+1)] and 
                    d_y[(j-1, i-1)] and 
                    d_y[(j-1, i)] and 
                    d_y[(j, i-1)] and 
                    d_y[(j, i)] and 
                    d_y[(j+1, i-1)] and 
                    d_y[(j+1, i)]):
                    reg_center[(j, i)] = int((image[i-1][j-1] + 
                                            image[i-1][j] + 
                                            image[i-1][j+1] + 
                                            image[i][j-1] + 
                                            image[i][j] + 
                                            image[i][j+1] + 
                                            image[i+1][j-1] + 
                                            image[i+1][j] + 
                                            image[i+1][j+1])/9)

        if reg_center == []:
            return image
        
        # print(reg_center)
        result = []
        
        for i in range(len(image)):
            temp = image[i][:]
            result.append(temp)
        
        
        for i in range(len(image)):
            for j in range(len(image[0])):
                num = 0
                s = 0
                
                if (j-1, i-1) in reg_center:
                    num += 1
                    s += reg_center[(j-1, i-1)]
                if (j-1, i) in reg_center:
                    num += 1
                    s += reg_center[(j-1, i)]
                if (j-1, i+1) in reg_center:
                    num += 1
                    s += reg_center[(j-1, i+1)]
                    
                if (j, i-1) in reg_center:
                    num += 1
                    s += reg_center[(j, i-1)]
                if (j, i) in reg_center:
                    num += 1
                    s += reg_center[(j, i)]
                if (j, i+1) in reg_center:
                    num += 1
                    s += reg_center[(j, i+1)]
                    
                if (j+1, i-1) in reg_center:
                    num += 1
                    s += reg_center[(j+1, i-1)]
                if (j+1, i) in reg_center:
                    num += 1
                    s += reg_center[(j+1, i)]
                if (j+1, i+1) in reg_center:
                    num += 1
                    s += reg_center[(j+1, i+1)]
                    

                if num > 0:
                    # print(s, num)

                    result[i][j] = int(s/num)
                    
        return result
                    
                
                
                
                    
                