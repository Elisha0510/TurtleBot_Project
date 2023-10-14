var arr = [false,false,false,false,false,false,
            false,false,false,false,false,false,
            false,false,false,false,false,false,false];

function c_1(num){
    arr[num] ^= true;
    const b_1 = document.getElementById("circle_"+num);
    b_1.style.display = arr[num] ? "block" : "none";
    
}