// Priority Queue
class QElement {
  constructor(element, priority) {
    this.element = element;
    this.priority = priority;
  }
}

class PriorityQueue {
  constructor() {
    this.items = [];
  }

  // isEmpty()

  // pushPQueue(item, priority)
  // popPQueue()
  // indexPQueue(idx)
  // printPQueue()

  isEmpty() {
    return this.items.length === 0;
  }

  pushPQueue(element, priority) {
    const qElement = new QElement(element, priority);
    let contain = false;

    for (let i = 0; i < this.items.length; i++) {
      if (this.items[i].priority > qElement.priority) {
        this.items.splice(i, 0, qElement);
        contain = true;
        break;
      }
    }

    if (!contain) {
      this.items.push(qElement);
    }
  }
  popPQueue() {
    if (this.isEmpty()) {
      return "Underflow";
    }
    return this.items.shift();
  }
  indexPQueue(idx) {
    if (this.isEmpty()) {
      return "No elements in Queue";
    }
    return this.items[idx].element;
  }
  printPQueue() {
    let str = "";
    for (let i = 0; i < this.items.length; i++) {
      str += this.items[i].element + " ";
    }
    return str;
  }
}

const priorityQueue = new PriorityQueue();

console.log(priorityQueue);

priorityQueue.pushPQueue("a");

console.log(priorityQueue);
