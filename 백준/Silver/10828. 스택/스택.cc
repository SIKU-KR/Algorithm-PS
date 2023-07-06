#include<iostream>
#include<string>
using namespace std;

struct node {
	int data;
	struct node* next;
};

struct stack {
	struct node* top;
	int size;
};

struct stack* createStack() {
	struct stack* stk;
	stk = (struct stack*)malloc(sizeof(struct stack));
	if (!stk)
		return NULL;
	stk->top = NULL;
	stk->size = 0;
	return stk;
}

void push(struct stack* stk, int data) {
	struct node* tmp;
	tmp = (struct node*)malloc(sizeof(struct node));
	if (!tmp)
		return;
	tmp->data = data;
	tmp->next = stk->top;
	stk->top = tmp;
	stk->size++;
}

int empty(struct stack* stk) {
	return (stk->top == NULL);
}

int pop(struct stack* stk) {
	int data;
	struct node* tmp;
	if (empty(stk))
		return -1;
	tmp = stk->top;
	stk->top = stk->top->next;
	data = tmp->data;
	stk->size--;
	free(tmp);
	return data;
}

int top(struct stack *stk){
	if (empty(stk))
		return -1;
	return stk->top->data;
}

int size(struct stack *stk){
	return stk->size;
}

int main(){
	int N, data;
	string str1;
	struct stack* stk = createStack();
	cin >> N;
	for (int i = 0; i < N; i++) {
		cin >> str1;
		if (str1 == "push") {
			cin >> data;
			push(stk, data);
		}
		else if (str1 == "pop") {
			cout << pop(stk) << endl;
		}
		else if (str1 == "size") {
			cout << size(stk) << endl;
		}
		else if(str1 == "empty") {
			cout << empty(stk) << endl;
		}
		else if (str1 == "top") {
			cout << top(stk) << endl;
		}
		else {
			break;
		}
	}
	return 0;
}