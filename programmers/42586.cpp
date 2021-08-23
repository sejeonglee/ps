#include <string>
#include <vector>
#include <iostream>

using namespace std;

vector<int> solution(vector<int> progresses, vector<int> speeds) {
    vector<int> answer;
    progresses.assign(1, 0);
    speeds.assign(1, 0);
    return answer;
}

vector<int> input_vector(){
    vector<int> a;
    return a;
}

void print_vector(vector<int> v){
    printf("[");
}

int main(){
    // vector<int> progresses;
    // vector<int> speeds;

    // progresses = input_vector();
    // speeds = input_vector();

    vector<int> v = {1,2,3};

    printf("%s", v);
    return 0;
}