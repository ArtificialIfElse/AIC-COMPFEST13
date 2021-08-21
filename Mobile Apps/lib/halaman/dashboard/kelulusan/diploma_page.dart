import 'dart:html';

import 'package:flutter/material.dart';

class DiplomaPage extends StatefulWidget {
  @override
  _DiplomaPage createState() => _DiplomaPage();
}

class _DiplomaPage extends State<DiplomaPage> {
  int selectedValue = 3;
  bool enableEmpat = false;
  bool enableLima = false;

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Container(
        padding: EdgeInsets.all(30),
        child: SingleChildScrollView(
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: <Widget>[
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
                onPressed: () {},
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
            ],
          ),
        ),
      ),
    );
  }
}
