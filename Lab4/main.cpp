#include <iostream>
#include <string>
#include <cmath>

using namespace std;


int pc_2[48] = {14,    17,   11,    24,     1,    5,
                  3,    28,   15,     6,    21,   10,
                 23,    19,   12,     4,    26,    8,
                 16,     7,   27,    20,    13,    2,
                 41,    52,   31,    37,    47,   55,
                 30,    40,   51,    45,    33,   48,
                 44,    49,   39,    56,    34,   53,
                 46,    42,   50,    36,    29,   32};
                 
                 
string* split_and_permutation(string message_56_bit){
    string* final_rounds = new string[16];
    string** rounds = new string*[2];
    rounds[0] = new string[17];
    rounds[1] = new string[17];
    rounds[0][0] = message_56_bit.substr(0,28);
    rounds[1][0] = message_56_bit.substr(28);
    cout << "C0: " + rounds[0][0] + " , D0: " + rounds[1][0] << endl;
    for(int i = 1; i < 17; i++){
        if(((i >=3) && (i <=8)) || ((i >=10) && (i <=15))){
            rounds[0][i] = rounds[0][i-1].substr(2)+rounds[0][i-1].substr(0,2);
            rounds[1][i] = rounds[1][i-1].substr(2)+rounds[1][i-1].substr(0,2);
        }else{
            rounds[0][i] = rounds[0][i-1].substr(1)+rounds[0][i-1].substr(0,1);
            rounds[1][i] = rounds[1][i-1].substr(1)+rounds[1][i-1].substr(0,1);
        }
        cout << "C" << i << ": " + rounds[0][i] + " , D" << i << ": " + rounds[1][i] << endl;
        final_rounds[i-1] =rounds[0][i] + rounds[1][i]; 
    }
    
    return final_rounds;
}

string permutation_56_to_48_bits(string message_56_bit){
    string message_48_bit = "";
    for(int i = 0; i < 48; i++){
        message_48_bit+=message_56_bit[pc_2[i]-1];
    }
    return message_48_bit;
}

string* r_keys(string* c_d_keys){
    string* round_keys;
    round_keys = new string[16];
    for(int i = 0; i < 16; i++){
        round_keys[i] = permutation_56_to_48_bits(c_d_keys[i]);
        cout << "K" << i+1 << ": " + round_keys[i] << endl;
    }
    return round_keys;
}

int main()
{
  string key, k, k_plus, message, permutated_message,rounded_message,reversed_message,f_permutation;
  string* keys_c_d;
  string* round_keys;
  cout << "Type in K+: ";
  cin >> k_plus;
  keys_c_d = split_and_permutation(k_plus);
  round_keys = r_keys(keys_c_d);

}
