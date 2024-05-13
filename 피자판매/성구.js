const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().split("\n");
// const input = fs.readFileSync('./예제.txt').toString().split("\n");


const settings = () => {
    const N = Number(input[0]);
    const [m, n] = input[1].split(" ").map(Number);
    const A = input.slice(2, 2+m).map(Number)
    const B = input.slice(2+m, 2+m+n).map(Number)
    return [N, m, n, A, B]
}

const main = (needs) => (m, n) => (A, B) => {
    const candidate = {
        "A" : {},
        "B" : {},
    }
    // console.log(N, m, n, A, B)
    let answer = 0;
    let fin_num = 0;
    for (let i = 0; i < m; i++){
        let pieces = 0;
        for (let j = i; j < i+m; j++){
            pieces += A[j % m];
            if (j === i+m-1){ 
                fin_num = pieces;
                break;
            } 
            if (pieces < needs) {
                if (pieces in candidate["A"]){
                    candidate["A"][pieces] ++;
                }else{
                    candidate["A"][pieces] = 1;
                }
            }else if (pieces === needs){
                answer ++;
            }else break;
        }
    }
    if (fin_num < needs) candidate["A"][fin_num] = 1;
    else if (fin_num === needs) answer ++;
    fin_num = 0;
    for (let i = 0; i < n; i++){
        pieces = 0;
        for (let j = i; j < i+n; j++){
            pieces += B[j % n];
            if (j === i+n-1){ 
                fin_num = pieces;
                break;
            } 
            if (pieces < needs) {
                if (pieces in candidate["B"]){
                    candidate["B"][pieces] ++;
                }else{
                    candidate["B"][pieces] = 1;
                }
            }else if (pieces === needs){
                answer ++;
            }else break;
        }
    }
    if (fin_num < needs) candidate["B"][fin_num] = 1;
    else if (fin_num === needs) answer ++;

    

    // console.log(candidate, answer)
    
    for (let a in candidate["A"]){
        if (!((needs-a) in candidate["B"])) continue;
        answer += candidate["A"][a] * candidate["B"][needs-a];
    }

    console.log(answer);

}

const [N, m, n, A, B] = settings();


main(N)(m,n)(A,B);