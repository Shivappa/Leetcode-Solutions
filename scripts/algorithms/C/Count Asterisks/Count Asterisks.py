# Added on 2022-08-18 15:51:55.040392

var countAsterisks = function(s) {
    let green=true, count=0;
    for(let i=0; i<s.length; i++){
        if(green && s[i]=="*"){count++};
        if(s[i]=="|"){green=!green};
    }
    return count;
};