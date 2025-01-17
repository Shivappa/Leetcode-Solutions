var minimumCost = function(cost) {
    if (cost.length < 3) {
        return cost.reduce((prev, cur) => prev + cur);
    }
    
    cost.sort((a, b) => b - a);
    let count = 0;
    let sum = 0;
    
    for (const num of cost) {
        if (count === 2) {
            count = 0;
            continue;
        }
        sum += num;
        count++;
    }
    
    return sum;
};
