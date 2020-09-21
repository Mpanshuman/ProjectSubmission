const arr = [1,2,3,4,5,6,7,8,9,10]
const arr2 = []

//Creating Reversed Array
for (var i=arr.length-1, j=0 ;i>=0;i--,j++){
  arr2[j] = arr[i]
}

//Printing Elements of both the array according to there index position
for(var i=0;i<arr.length;i++){
  console.log(`Element of index[${i}] of array1 is ${arr[i]} and of Reversed array is ${arr2[i]}`)
}
