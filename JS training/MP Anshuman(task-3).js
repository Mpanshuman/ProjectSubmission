function grade(mark){
  if(mark>= 250){
    return 'A'
  }
  else if(mark >=200){
    return 'B'
  }
  else if(mark >=150){
    return 'C'
  }
  else if(mark >=100){
    return 'D'
  }
  else if(mark >=50){
    return 'E'
  }
  else{
    return 'F'
  }

}

const student_list = [
  {
  name: 'A',
  mark: {
    Math: 90,
    Science: 88,
    IT: 75
  }
},
{
  name: 'D',
  mark: {
    Math: 30,
    Science: 11,
    IT: 10
  }
},
{
  name: 'B',
  mark: {
    Math: 72,
    Science: 55,
    IT: 87
  }
},
{
  name: 'C',
  mark: {
    Math: 80,
    Science: 95,
    IT: 88
  }
}]

const studentmark = []
for(var i=0;i<student_list.length;i++){

 var y = [student_list[i].mark]
var totalmark = y.reduce(
 (total,element)=>total+element.Math+element.Science+element.IT,0
);

studentmark.push({name:student_list[i].name,marks:totalmark,grade:grade(totalmark)})
console.log(`${studentmark[i].name} got ${studentmark[i].marks} Marks with ${studentmark[i].grade} Grade.`)
}
