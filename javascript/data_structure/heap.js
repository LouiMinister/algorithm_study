/*
 완전 이진트리의 일종으로 여러 값 중, 최대값과 최소값을 빠르게 찾아내도록 만들어진 자료구조이다.
 우선순위 큐: 우선순위의 개념을 큐에 도입한 자료 구조
 우선순위 큐는 배열, 연결리스트, 힙 으로 구현이 가능하다. 이 중에서 힙(heap)으로 구현하는 것이 가장 효율적이다.
 */

class MaxHeap {
    constructor() {
        this.ary = [null];
        this.idx = 1;
    }

    swap(i,j) {
        const tmp = this.ary[i];
        this.ary[i] = this.ary[j];
        this.ary[j] = tmp;
    }

    insert(val) {
        let idx = this.idx;
        this.ary[idx] = val; 
        this.idx += 1;
        let parentIdx = Math.floor(idx/2);
        while ( this.ary[idx] > this.ary[parentIdx] && idx != 1 ){
            this.swap(idx, parentIdx);
            idx = parentIdx;
            parentIdx = Math.floor(idx/2);
        }
    }

    delete() {
        const result = this.ary[1];
        const lastVal = this.ary[this.idx-1];
        this.ary[this.idx-1] = undefined;
        this.idx --
        this.ary[1] = lastVal;

        let idx = 1;
        while (true) {
            const chiledIdx = this.ary[idx*2] > this.ary[idx*2+1] ? idx*2 : idx*2+1;
            if (this.ary[chiledIdx] > this.ary[idx]){
                this.swap(idx, chiledIdx);
                idx = chiledIdx;
            } else {
                break;
            }
        }
        return result;
    }
}

const maxHeap = new MaxHeap();

maxHeap.insert(3);
console.log(maxHeap.ary);
maxHeap.insert(4);
console.log(maxHeap.ary);
maxHeap.insert(5);
console.log(maxHeap.ary);
maxHeap.delete();
console.log(maxHeap.ary);
maxHeap.delete();
console.log(maxHeap.ary);