function rangeToArray(number) {
    var array = [];
    var i;
    for (i = 0; i < number+1; i++) {
      array.push(i);
    }
    return array;   
  }

  myArray=rangeToArray(5)
  console.log(myArray)