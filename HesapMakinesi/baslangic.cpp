#include <iostream>
#include <locale.h>
#include <string>
#include <math.h>

using namespace std;


char islem;
double s1, s2;
string onunadi;


int main() {

	setlocale(LC_ALL, "Turkish");
	cout << "Selamlar, benimle adını paylaşabilir misin :)" << endl;
	cin >> onunadi;
	cout << "Hoş geldin " << onunadi << " hesaplamasını yapmak istediğin iki sayı gir." << endl;
	cin >> s1 >> s2;
	cout << "Toplama için t, çıkarma için f, çarpma için c, bölme için b harfine bas!: ";
	cin >> islem;
	if (islem == 't' || islem == 'T' || islem == '+') {

		cout << "İşleminin sonucu : " << s1 + s2 << endl;

	}
	else if (islem == 'f' || islem == 'F' || islem == '-') {

		cout << "İşleminizin sonucu : " << s1 - s2 << endl;

	}
	else if (islem == 'c' || islem == 'C' || islem == 'x') {

		cout << "İşleminizin sonucu : " << s1 * s2 << endl;

	}
	else if (islem == 'b' || islem == 'B' || islem == '/') {

		cout << "İşleminizin sonucu : " << s1 / s2 << endl;

	}
	else {

		cout << "Yapmak istediğiniz işlem geçersiz." << endl;

	}


	return 0;
}