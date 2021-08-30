const but = document.querySelector("body > div > button");
but.addEventListener("click", submitData);

const cycle = document.querySelector("body > div > div:nth-child(1) > input[type=text]");
const settle = document.querySelector("body > div > div:nth-child(2) > input[type=text]");
const payday = document.querySelector("body > div > div:nth-child(3) > input[type=date]");
const today = document.querySelector("body > div > div:nth-child(4) > input[type=date]");

function submitData(){
    let data = {};
    data.cycle = cycle.value;
    data.settle = settle.value;
    data.payday = payday.value;
    data.today = today.value;

    if(!parseInt(data.cycle) | data.cycle < 0){
        alert("計費周期請輸入正整數");
        location.reload();
    } else if(!parseInt(data.settle)){
        alert("收費日請輸入正確之日期(1~31)");
        location.reload();
    } else if(!data.today){
        alert("請填入今日日期");
        location.reload();
    } else if(!data.payday){
        alert("請填入預計收費日");
        location.reload();
    }

    if(data.settle > 28){
        alert("填入之日期若於某些月份並不存在，會以當日最後一天為準。")
    } else if(data.settle < 1 | data.settle > 31){
        alert("收費日請輸入正確之日期(1~31)");
        location.reload();
    }

    let request = new XMLHttpRequest();
    let requestURL = "http://127.0.0.1:5000/q2";
    let data_to_python = JSON.stringify(data);
    request.onload = function(){
        if(request.status == 200){
            let json = JSON.parse(request.responseText);
            alert(json.message);
            location.reload();
        }
    }
    request.open("POST", requestURL, true);
    request.setRequestHeader('content-type', 'application/json');
    request.send(data_to_python);
}

