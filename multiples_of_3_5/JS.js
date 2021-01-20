
const multiplesOf3And5 = () =>{
    
    let sumOfMulitples = 0

    for(let i=3; i<1000; i++){
        if(!(i%3) || !(i%5)){
            sumOfMulitples+=i;
        }

    }
    return sumOfMulitples;
}

console.log(multiplesOf3And5())