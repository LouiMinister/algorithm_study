/**
 * 문제 설명
 *
 * 다리를 지나는 트럭 *
 트럭 여러 대가 강을 가로지르는 일 차선 다리를 정해진 순으로 건너려 합니다. 모든 트럭이 다리를 건너려면 최소 몇 초가 걸리는지 알아내야 합니다. 트럭은 1초에 1만큼 움직이며, 다리 길이는 bridge_length이고 다리는 무게 weight까지 견딥니다.
 ※ 트럭이 다리에 완전히 오르지 않은 경우, 이 트럭의 무게는 고려하지 않습니다.

 예를 들어, 길이가 2이고 10kg 무게를 견디는 다리가 있습니다. 무게가 [7, 4, 5, 6]kg인 트럭이 순서대로 최단 시간 안에 다리를 건너려면 다음과 같이 건너야 합니다.

 경과 시간	다리를 지난 트럭	다리를 건너는 트럭	대기 트럭
 0	[]	[]	[7,4,5,6]
 1~2	[]	[7]	[4,5,6]
 3	[7]	[4]	[5,6]
 4	[7]	[4,5]	[6]
 5	[7,4]	[5]	[6]
 6~7	[7,4,5]	[6]	[]
 8	[7,4,5,6]	[]	[]
 따라서, 모든 트럭이 다리를 지나려면 최소 8초가 걸립니다.

 solution 함수의 매개변수로 다리 길이 bridge_length, 다리가 견딜 수 있는 무게 weight, 트럭별 무게 truck_weights가 주어집니다. 이때 모든 트럭이 다리를 건너려면 최소 몇 초가 걸리는지 return 하도록 solution 함수를 완성하세요.

 제한 조건
 bridge_length는 1 이상 10,000 이하입니다.
 weight는 1 이상 10,000 이하입니다.
 truck_weights의 길이는 1 이상 10,000 이하입니다.
 모든 트럭의 무게는 1 이상 weight 이하입니다.
 입출력 예
 bridge_length	weight	truck_weights	return
 2	10	[7,4,5,6]	8
 100	100	[10]	101
 100	100	[10,10,10,10,10,10,10,10,10,10]	110


 ** 느낀점 **
 *
 * solution_ 이 처음 풀었던 코드이다.
 * 답은 전부 맞았지만 테스트 5번이 시간초과되어 solution 코드로 대하였다.
 * 수정한 부분은 도로 위의 차의 무게를 reduce 함수를 이용하여 main loop 를 돌때마다 구했던 것을 차가 다리에 올라오고 내려갈 때 직접 다른 변수로 컨트롤 하였다.체
 *
 *
 */
(function main(){

    const bridge_lenghth = 100;
    const weight = 100;
    const truck_weights = [10,10,10,10,10,10,10,10,10,10];

    console.log(solution(bridge_lenghth, weight, truck_weights));
})();


/**
 *
 * 테스트 1 〉	통과 (2.64ms, 37.6MB)
 테스트 2 〉	통과 (51.66ms, 37.7MB)
 테스트 3 〉	통과 (1.82ms, 37.4MB)
 테스트 4 〉	통과 (11.26ms, 37.5MB)
 테스트 5 〉	통과 (240.02ms, 37.9MB)
 테스트 6 〉	통과 (37.41ms, 37.5MB)
 테스트 7 〉	통과 (2.29ms, 37.4MB)
 테스트 8 〉	통과 (1.85ms, 37.5MB)
 테스트 9 〉	통과 (4.41ms, 37.5MB)
 테스트 10 〉	통과 (1.87ms, 37.3MB)
 테스트 11 〉	통과 (1.82ms, 37.3MB)
 테스트 12 〉	통과 (1.96ms, 37.2MB)
 테스트 13 〉	통과 (2.26ms, 37.5MB)
 */
function solution(bridge_length, weight, truck_weights) {

    const max_weight = weight;
    const arrived_trucks = [];
    const bridge_trucks = new Array(bridge_length).fill(0);
    let bridge_weight = 0;
    const ready_trucks = [...truck_weights];
    let time = 0;


    while(true){
        if(arrived_trucks.length == truck_weights.length){
            break;
        }
        time++;

        console.log(`bridge_weight : ${bridge_weight} bridge_trucks: ${bridge_trucks}`);
        let start_truck =undefined;

        if(bridge_weight + ready_trucks[0] - bridge_trucks[bridge_trucks.length-1]  <= max_weight){
            start_truck = ready_trucks.shift();
        } else {
            start_truck = 0;
        }
        bridge_trucks.unshift(start_truck);
        bridge_weight += start_truck;

        const arrived_truck = bridge_trucks.pop();
        if(arrived_truck !=0){
            arrived_trucks.push(arrived_truck);
            bridge_weight -= arrived_truck;
        }
    }

    return time;
}


/**
 테스트 1 〉	통과 (49.81ms, 37.9MB)
 테스트 2 〉	통과 (3822.88ms, 40.1MB)
 테스트 3 〉	통과 (1.90ms, 37.3MB)
 테스트 4 〉	통과 (726.75ms, 39.2MB)
 테스트 5 〉	실패 (시간 초과)
 테스트 6 〉	통과 (3576.73ms, 41.8MB)
 테스트 7 〉	통과 (18.25ms, 37.6MB)
 테스트 8 〉	통과 (2.35ms, 37.5MB)
 테스트 9 〉	통과 (10.62ms, 38MB)
 테스트 10 〉	통과 (2.56ms, 37.3MB)
 테스트 11 〉	통과 (1.82ms, 37.3MB)
 테스트 12 〉	통과 (2.19ms, 37.2MB)
 테스트 13 〉	통과 (5.53ms, 37.8MB)
 */

function solution_(bridge_length, weight, truck_weights) {

    const max_weight = weight;
    const arrived_trucks = [];
    const bridge_trucks = new Array(bridge_length).fill(0);
    const ready_trucks = [...truck_weights];
    let time = 0;


    while(true){
        if(arrived_trucks.length == truck_weights.length){
            break;
        }
        time++;

        const bridge_weight = bridge_trucks.reduce((accumulate, current) => accumulate + current);
        console.log(`bridge_weight : ${bridge_weight} bridge_trucks: ${bridge_trucks}`);
        let start_truck =undefined;

        if(bridge_weight + ready_trucks[0] - bridge_trucks[bridge_trucks.length-1]  <= max_weight){
            start_truck = ready_trucks.shift();
        } else {
            start_truck = 0;
        }
        bridge_trucks.unshift(start_truck);

        const arrived_truck = bridge_trucks.pop();
        if(arrived_truck !=0){
            arrived_trucks.push(arrived_truck);
        }
    }

    return time;
}

//