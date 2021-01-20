

const verifyNots = (digit,args) => {
    let isVerified = false;
    args = new Set(args);
    Array.from(args).forEach( arg => isVerified = (isVerified || !(digit%arg)) )
    return isVerified;
}
    


const multiples = (limit = 1000, args = [3,5]) => {
    let sumOfMulitples = 0;
    const mininimum = Math.min(...args);
    for(let i=mininimum; i<limit; i++){
        if(verifyNots(i, args)) sumOfMulitples+=i;
    }
    return sumOfMulitples;
}

console.log(multiples())

