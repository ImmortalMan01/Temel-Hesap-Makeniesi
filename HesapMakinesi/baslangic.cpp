#include <iostream>
#include <locale.h>
#include <math.h>
#include <string>

using namespace std;

string onunadi;
string benimadim = "Oğulcan";
string markam;

char islem;
float s1, s2;

void marka() {

	cout << markam << endl;


}

int main() {

	setlocale(LC_ALL, "Turkish");
	cout << "Hoş geldin, benimle adını paylaşabilir misin?" << endl;
	cin >> onunadi;
	cout << "Tanıştığıma memnun oldum " << onunadi << ". Benim adım " << benimadim << endl;
	cout << "Şimdi senden işlemini yapmak istediğin iki sayıyı girmeni istiyorum." << endl;
	cin >> s1 >> s2;
	cout << "Girdiğin sayılar " << s1 << " ve " << s2 << endl;
	cout << "toplama için t, çıkarma için f, çarpma için c, bölme için b harfine bas" << endl;
	cin >> islem;
	cout << "Seçtiğiniz işlem : " << islem << endl;
	if (islem == 't' || islem == 'T' || islem == '+') {

		cout << "İşleminizin sonucu : " << s1 + s2 << endl;

	}
	else if (islem == 'f' || islem == 'F' || islem == '-') {

		cout << "İşleminizin sonucu : " << s1 - s2 << endl;

	}
	else if (islem == 'c' || islem == 'C' || islem == 'x') {

		cout << "İşleminizin sonucu : " << s1 * s2 << endl;

	}
	else if (islem == 'b' || islem == 'B' || islem == '/') {

		cout << "işleminizin sonucu : " << s1 / s2 << endl;

	}
	else {

		cout << onunadi << " yapmaya çalıştığın işlem geçersiz." << endl;

	}

	marka();

	return 0;
}