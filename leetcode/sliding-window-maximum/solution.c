/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
typedef struct Node {
    int val;
    struct Node *next;
    struct Node *prev;
} Node;

typedef struct List {
    struct Node *head;
    struct Node *tail;
} List;

void push(List *l, int val) {
    Node *node = malloc(sizeof(Node));
    node->val = val;
    node->next = NULL;
    node->prev = NULL;
    if(!l->head) {
        l->head = node;
    }
    
    if(!l->tail) {
        l->tail = node;
    } else {
        node->prev = l->tail;
        l->tail->next = node;
        l->tail = node;
    }
}

int* maxSlidingWindow(int* nums, int numsSize, int k, int* returnSize) {
    *returnSize = numsSize - k + 1;
    int *ret = malloc(sizeof(int) * *returnSize);
    List maxs = {.head = NULL, .tail = NULL}; 
    int l = 0;
    int r = 0;
    Node *tail;

    while(r < numsSize) {
        while((maxs.tail) && (nums[maxs.tail->val] < nums[r])){
            tail = maxs.tail;
            if(maxs.tail->prev) {
                maxs.tail->prev->next = NULL;
            } else {
                maxs.head = NULL;
            }
            maxs.tail = maxs.tail->prev;
            free(tail);
        }
        push(&maxs, r);
        if(l>maxs.head->val) {
            tail = maxs.head;
            if(maxs.head->next) {
                maxs.head->next->prev = NULL;
            } else {
                maxs.tail = NULL;
            }
            maxs.head = maxs.head->next;
            free(tail);
        }
        if(r>=(k-1)) {
            ret[r-k+1] = nums[maxs.head->val];
            l++;
        }
        r++;
    }
    return ret;
}
