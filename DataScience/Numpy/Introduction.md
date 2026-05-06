# Numpy
  Tutorial: https://www.youtube.com/watch?v=VXU4LSAQDSc
  
  Google Colab: https://colab.research.google.com/

 Numpy is used for building and manipulating N dimensional arrays. Numpy is short form Numerical Python
 Numpy is a python module which is wrapper module for calling c based numpy module.
 Python list is slower when compared to Numpy arrays

 ### How to create Numpy array
    import numpy as np

    array = np.array([1,2,3,4])
	print(array) # will print [1 2 3 4]
	
	array = np.array('A')
	print(array) # will print A
	
	array = np.array([[1,2,3],[4,5,6]])
	print(array) 
	# Will print as [[1 2 3]
	                 [4 5 6]]
 
 ## Getting number of dimension of numpy array
	array = np.array([1,2,3,4])
	print(array.ndim) # will 1
	
	array = np.array('A')
	print(array.ndim) # will print 0
	
	array = np.array([[1,2,3],[4,5,6]])
	print(array.ndim) # will print 2
	
	array = np.array([[[1,2,3]], [[4,5,6]]])
	print(array.ndim) # will print 3
	
	array = np.array([])
	print(arra.ndim) # will print 1

**Note**:
	     Dimensions are determined based on number of opening square brackets. If no square bracket then dimension will be 0. If one square bracket then dimension will 1.If 2 square bracket then dimension will 2, if 3 square bracket then dimension will be 3 and so on
 
 ## Numpy shape gives 2 information 
   - Number of rows
   - Number of elements in each row

   So output will be a tuple as (<no.of.rows>, <no.of.elements.in.each.row>)

   **Note**:
      If <no.of.rows> = 1, then shape will be (<no.of.elements.in.each.row>, )  
	  Example:

		   array = np.array('A')
		   print(array.shape) # will print (), that means no shape
		   
		   array = np.array([1,2,3,4])
		   print(array.shape) # This will print (4,). That means its a 1D array. In Numpy, ID arrays is orientation-less. That means it doesnt posses the concept of being
		                      # 'row' or 'column'. It is simply a sequence of elements in single dimension.
							  # So most will expect the shape as (1, 4). But in Numpy such array will be represented using np.array([[1,2,3,4]])
							  
		   array = np.array([[1,2,3,4]])
		   print(array.shape) # This will print (1,4)
		   
		   array = np.array([])
		   print(array.shape) # This will print (0,). This means 1D array with zero elements
           
		   array = np.array([ [[1, 2, 3]], [[4, 5, 6]] ])
		   print(array.shape) # This will print as (2, 1 ,3). Meaning it has 2 levels and each level has one row and each row has 3 columns

		   array = np.array([ [[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]] ])
           print(array.shape) # This will print as (2, 2 ,3). Meaning it has 2 levels and each level has 2 row and each row has 3 columns

		   array = np.array([ [[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[10, 11, 12], [13, 14, 15], [16, 17, 18]] ])
		   print(array.shape) # This will print as (2, 3 ,3). Meaning it has 2 levels and each level has 3 row and each row has 3 columns


 ## Chain Indexing and Multi-dimensional indexing
 
      array = np.array([[[1, 2, 3]], [[4, 5, 6]]])
	  print(array[0][0][0]) # will print as 1
	  print(array[0][0][2]) # will print as 3
	  print(array[1][0][2]) # will print as 6
	  print(array[2][0][2]) # will cause IndexError exception

This is called chain indexing
	  
Same values can be accessed using multi-dimensional indexing as well

	  array = np.array([[[1, 2, 3]], [[4, 5, 6]]])
	  print(array[0,0,0]) # will print as 1
	  print(array[0,0,2]) # will print as 3
	  print(array[1,0,2]) # will print as 6
	  print(array[2,0,2]) # will cause IndexError exception
	  
 ## Array Slicing using Numpy
   Numpy arrays can sliced in two ways
     1. Row slicing
	      format will be array[start:end:step]
			     
     2. Column slicing
          format will be array[start:end:step, start:end:step]
          First range represents row and second represents column


	    Example (Row Slicing)
		   array = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]])
		   print(array[0:2])
				o/p: [[1 2 3 4]
                      [5 6 7 8]]
		
		   print(array[0:5:2])
			   o/p: [[ 1  2  3  4]
				     [ 9 10 11 12]		   
		   
		   print(array[::-1])
		       o/p: [[13 14 15 16]
					 [ 9 10 11 12]
                     [ 5  6  7  8]
                     [ 1  2  3  4]]
		   print(array[::-2])
			   o/: [[13 14 15 16]
					[ 5  6  7  8]]
					
		Example: Column Slicing
			array = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]])
			print(array[:, 0:2])
			o/p: [[ 1  2]
				  [ 5  6]
                  [ 9 10]
                  [13 14]]
				  
			print(array[:,0:5])
			o/p: [[ 1  2  3  4]
                  [ 5  6  7  8]
                  [ 9 10 11 12]
                  [13 14 15 16]]
				  
			print(array[:,::-1]
			o/p: [[ 4  3  2  1]
				  [ 8  7  6  5]
                  [12 11 10  9]
                  [16 15 14 13]]
				  
			print(array[0:2,0:2])
			o/p: [[1 2]
                  [5 6]]
				  
			print(array[0:5:2,0:2])
			o/p: [[ 1  2]
                  [ 9 10]]
				  
			print(array[0:5:2,0:5:2])
			o/p: [[ 1  3]
                  [ 9 11]]
			
			print(array[:,-1:-5:-1])
			o/p: [[ 4  3  2  1]
                  [ 8  7  6  5]
                  [12 11 10  9]
                  [16 15 14 13]]
				  
			print(array[::-1,-1:-5:-1])
			o/p: [[16 15 14 13]
                  [12 11 10  9]
                  [ 8  7  6  5]
                  [ 4  3  2  1]]
			   
  --> Arithmetic in Numpy
      There are different ways arithmetic operations can be performed using Numpy
      a) Scalar arithmetic
           Example
               import numpy as np
			   array = np.array([1, 2, 3, 4])
			   print(array + 1)
			   o/p
			      [2 3 4 5]
			   
			   print(array - 1)
			   o/p
			      [0 1 2 3]
			   
			   print(array * 2)
			   o/p
			      [2 4 6 8]
				  
			   print(array / 2)
			   o/p
			      [0.5 1. 1.5 2.]
			
			   print(array ** 2)
			   o/p
			      [1 4 9 16]
				  
	   b) Arithmetic using vector math functions
	       Example
		       import numpy as np
			   array = np.array([4, 9, 16, 25])
			   print(np.sqrt(array))
			   o/p
			      [2. 3. 4. 5.]
				  
		  Examples of mathematical constants defined in numpy
		       print(np.pi)
			   o/p
			      3.141592653589793
				  
	   c) Element-wise arithmetic
	      Example
		      array1 = np.array([2,3,4,5])
			  array2 = np.array([5,6,7,8])
			  
			  print(array1 + array2)
			  o/p 
			    [ 7  9 11 13]
				
			  print(array1 - array2)
			  o/p
			    [-3 -3 -3 -3]
				
			  print(array1 * array2)
			  o/p
			    [10 18 28 40]
				
			  print(array1 / array2)
			  o/p
			    [0.4        0.5        0.57142857 0.625     ]
				
			  print(array1 ** array2)
			  o/p
			    [    32    729  16384 390625]
				
		d) Comparison arithmetic
		   With this arithmetic we can create boolean arrays
		
		   Example 1
		      marks = np.array([95, 65, 58, 85, 74, 100])
			  prit(marks >= 65) # Pass
			  o/p
			     [ True  True False  True  True  True]
			  
			  print(marks < 65)
		      o/p
			     [False False  True False False False]
				 
		   Example 2
		      marks = np.array([95, 65, 58, 85, 74, 100])
			  marks[marks < 65] = 0
			  print(marks)
			  o/p
			     [ 95  65   0  85  74 100]
				 
			  Similarly
			  marks[marks > 65] = 0
			  print(marks)
			  o/p
			     [ 0  65   58  0  0 0]
			    
