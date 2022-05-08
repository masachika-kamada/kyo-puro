#include <iostream>
#include <vector>
using namespace std;

int main(void){
    int n, q;
    cin >> n >> q;
    vector<unsigned int> a;
    for (i = 1; i <= n; i++)
    {
        a.push_back(i);
    }
    unsigned int x;
    unsigned int tmp;
    for (int i = 0; i < q; i++)
    {
        cin >> x;
        int idx = a.at(x);
        if (idx == n - 1)
        {
            tmp = a[idx];
            a[idx] = a[idx - 1];
            a[idx - 1] = tmp;
        }
        else{
            tmp = a[idx];
            a[idx] = a[idx + 1];
            a[idx + 1] = tmp;
        }
    }
    for (int i = 0; i < a.size() - 1; i++)
    {
        cout << a[i] << " ";
    }
    cout << vec.back() << endl;
}