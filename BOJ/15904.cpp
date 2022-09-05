#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main() {
  vector<char> characters = {'U', 'C', 'P', 'C'};
  string s;
  getline(cin, s);

  for (auto c : characters) {
    auto n = s.find(c);
    if (n == string::npos) {
      cout << "I hate UCPC" << endl;
      return 0;
    }
    s = s.substr(n + 1);
  }
  cout << "I love UCPC" << endl;
  return 0;
}
