//Insertion Sort

#include <iostream>
using namespace std;

int main(){
	int y;
	cout<<"======Insertion Sort======"<<endl<<endl<<"Masukkan panjang array: ";
	cin>>y;
	cout<<endl;
	int x[y];
	for(int i=0; i<y; i++){
		cout<<"Masukkan data ke-"<<i+1<<": ";
		cin>>x[i];
	}
	cout<<endl;
	cout<<"Proses sorting: "<<endl;
	for(int i=1; i<y; i++){
		int key = x[i];
		int j = i-1;
		while(j>=0 && x[j] > key){
			x[j+1] = x[j];
			j--;
		}
		x[j+1] = key;
		for(int m=0;m<y;m++){
		cout<<x[m]<<" ";
	    }
	    cout<<endl;
	}
	cout<<endl;
	cout<<"Hasil akhir: "<<endl;
	for(int m=0;m<y;m++){
		cout<<x[m]<<" ";
	}
	cout<<endl;
}

//Shell Sort

#include<iostream>
#include<conio.h>
#include<stdlib.h>

using namespace std;

int main() {
    int array;
    cout << "======Shell Sort======\n"<<endl;
    cout << "Masukkan panjang array: ";cin>>array;
    cout << endl;
    int arr_sorting[array], a, k,j, i, t;

    for (i = 0; i < array; i++)
    {
        cout<<"Masukkan data ke-"<<i+1<<": ";
        cin >> arr_sorting[i];
    }
    cout<<endl;

    cout<<"Proses sorting: "<<endl;
    for (i = array / 2; i > 0; i = i / 2) {
        for (j = i; j < array; j++) {
            for (k = j-i; k >= 0; k = k-i) {
                if (arr_sorting[k + i] >= arr_sorting[k])
                    break;
                else {

                    t = arr_sorting[k];
                    arr_sorting[k] = arr_sorting[k + i];
                    arr_sorting[k + i] = t;
                }
            }

            cout << "\nGap " << i << ":";
            for (a = 0; a < array; a++) {
                cout << " " << arr_sorting[a];
            }
        }

    }

    cout << "\n\nHasil akhir:\n";
    for (i = 0; i < array; i++) {
        cout << " " << arr_sorting[i];
    }
    cout<<endl;
}
