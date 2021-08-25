import 'package:compest_artificialifelse/api/api.dart';
import 'package:flutter/material.dart';

class DiplomaPage extends StatefulWidget {
  @override
  _DiplomaPage createState() => _DiplomaPage();
}

class _DiplomaPage extends State<DiplomaPage> {
  int selectedValue = 3;
  bool enableEmpat = false;
  bool enableLima = false;

  String hasil = "";

  TextEditingController s1 = TextEditingController();
  TextEditingController s2 = TextEditingController();
  TextEditingController s3 = TextEditingController();
  TextEditingController s4 = TextEditingController();
  TextEditingController s5 = TextEditingController();

  void _cekDiplomaTiga() async {
    Api.cekDiplomaTiga(
            double.parse(s1.text), double.parse(s2.text), double.parse(s3.text))
        .then((value) {
      setState(() {
        hasil = value.prediction;
        print(hasil);
      });
    }).catchError((err) {
      print(err);
    });
  }

  void _cekDiplomaEmpat() async {
    Api.cekDiplomaEmpat(double.parse(s1.text), double.parse(s2.text),
            double.parse(s3.text), double.parse(s4.text))
        .then((value) {
      setState(() {
        hasil = value.prediction;
      });
    }).catchError((err) {
      print(err);
    });
  }

  void _cekDiplomaLima() async {
    Api.cekDiplomaLima(double.parse(s1.text), double.parse(s2.text),
            double.parse(s3.text), double.parse(s4.text), double.parse(s5.text))
        .then((value) {
      setState(() {
        hasil = value.prediction;
      });
    }).catchError((err) {
      print(err);
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Container(
        padding: EdgeInsets.all(30),
        child: SingleChildScrollView(
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: <Widget>[
              SizedBox(
                height: 36,
              ),
              Text(
                'Kamu sudah melalui semester berapa?',
                textAlign: TextAlign.left,
                style: TextStyle(
                  fontSize: 14,
                  letterSpacing: 0.27,
                  color: Colors.black,
                ),
              ),
              SizedBox(
                height: 12,
              ),
              DropdownButton(
                  value: selectedValue,
                  items: [
                    DropdownMenuItem(
                      child: Text("Semester 3"),
                      value: 3,
                    ),
                    DropdownMenuItem(
                      child: Text("Semester 4"),
                      value: 4,
                    ),
                    DropdownMenuItem(
                      child: Text("Semester 5"),
                      value: 5,
                    ),
                  ],
                  onChanged: (int? value) {
                    setState(() {
                      selectedValue = value!;
                      if (selectedValue == 3) {
                        enableEmpat = false;
                        enableLima = false;
                      } else if (selectedValue == 4) {
                        enableEmpat = true;
                        enableLima = false;
                      } else if (selectedValue == 5) {
                        enableEmpat = true;
                        enableLima = true;
                      }
                    });
                  }),
              SizedBox(
                height: 12,
              ),
              TextFormField(
                controller: s1,
                cursorColor: Theme.of(context).cursorColor,
                maxLength: 10,
                keyboardType: TextInputType.number,
                decoration: InputDecoration(
                  icon: Icon(Icons.border_color),
                  labelText: 'IPS Semester 1',
                  labelStyle: TextStyle(
                    color: Colors.blue[400],
                  ),
                  enabledBorder: UnderlineInputBorder(
                    borderSide: BorderSide(color: Colors.blue),
                  ),
                ),
              ),
              TextFormField(
                controller: s2,
                cursorColor: Theme.of(context).cursorColor,
                maxLength: 10,
                keyboardType: TextInputType.number,
                decoration: InputDecoration(
                  icon: Icon(Icons.border_color),
                  labelText: 'IPS Semester 2',
                  labelStyle: TextStyle(
                    color: Colors.blue[400],
                  ),
                  enabledBorder: UnderlineInputBorder(
                    borderSide: BorderSide(color: Colors.blue),
                  ),
                ),
              ),
              TextFormField(
                controller: s3,
                cursorColor: Theme.of(context).cursorColor,
                maxLength: 10,
                keyboardType: TextInputType.number,
                decoration: InputDecoration(
                  icon: Icon(Icons.border_color),
                  labelText: 'IPS Semester 3',
                  labelStyle: TextStyle(
                    color: Colors.blue[400],
                  ),
                  enabledBorder: UnderlineInputBorder(
                    borderSide: BorderSide(color: Colors.blue),
                  ),
                ),
              ),
              enableEmpat
                  ? TextFormField(
                      controller: s4,
                      enabled: enableEmpat,
                      cursorColor: Theme.of(context).cursorColor,
                      maxLength: 10,
                      keyboardType: TextInputType.number,
                      decoration: InputDecoration(
                        icon: Icon(Icons.border_color),
                        labelText: 'IPS Semester 4',
                        labelStyle: TextStyle(
                          color: Colors.blue[400],
                        ),
                        enabledBorder: UnderlineInputBorder(
                          borderSide: BorderSide(color: Colors.blue),
                        ),
                      ),
                    )
                  : SizedBox(),
              enableLima
                  ? TextFormField(
                      controller: s5,
                      enabled: enableLima,
                      cursorColor: Theme.of(context).cursorColor,
                      maxLength: 10,
                      keyboardType: TextInputType.number,
                      decoration: InputDecoration(
                        icon: Icon(Icons.border_color),
                        labelText: 'IPS Semester 5',
                        labelStyle: TextStyle(
                          color: Colors.blue[400],
                        ),
                        enabledBorder: UnderlineInputBorder(
                          borderSide: BorderSide(color: Colors.blue),
                        ),
                      ),
                    )
                  : SizedBox(),
              SizedBox(
                height: 36,
              ),
              RaisedButton(
                onPressed: () {
                  if (selectedValue == 3) {
                    _cekDiplomaTiga();
                  } else if (selectedValue == 4) {
                    _cekDiplomaEmpat();
                  } else if (selectedValue == 5) {
                    _cekDiplomaLima();
                  }
                },
                shape: RoundedRectangleBorder(
                    borderRadius: BorderRadius.circular(80.0)),
                padding: EdgeInsets.all(0.0),
                child: Ink(
                  decoration: BoxDecoration(
                      gradient: LinearGradient(
                        colors: [Color(0xff374ABE), Color(0xff64B6FF)],
                        begin: Alignment.centerLeft,
                        end: Alignment.centerRight,
                      ),
                      borderRadius: BorderRadius.circular(30.0)),
                  child: Container(
                    constraints:
                        BoxConstraints(maxWidth: 500.0, minHeight: 50.0),
                    alignment: Alignment.center,
                    child: Text(
                      "Klasifikasikan",
                      textAlign: TextAlign.center,
                      style: TextStyle(color: Colors.white, fontSize: 14),
                    ),
                  ),
                ),
              ),
              SizedBox(
                height: 36,
              ),
              Text(
                'Selamat! Anda lulus dengan predikat $hasil',
                style: TextStyle(
                  fontSize: 18,
                  letterSpacing: 0.27,
                  color: Colors.black,
                  fontWeight: FontWeight.bold,
                ),
              ),
              SizedBox(
                height: 146,
              ),
            ],
          ),
        ),
      ),
    );
  }
}
