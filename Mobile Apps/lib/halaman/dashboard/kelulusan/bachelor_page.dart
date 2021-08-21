import 'package:flutter/material.dart';

class BachelorPage extends StatefulWidget {
  @override
  _BachelorPage createState() => _BachelorPage();
}

class _BachelorPage extends State<BachelorPage> {
  int selectedValue = 5;
  bool enableEnam = false;
  bool enableTujuh = false;

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
                      child: Text("Semester 5"),
                      value: 5,
                    ),
                    DropdownMenuItem(
                      child: Text("Semester 6"),
                      value: 6,
                    ),
                    DropdownMenuItem(
                      child: Text("Semester 7"),
                      value: 7,
                    ),
                  ],
                  onChanged: (int? value) {
                    setState(() {
                      selectedValue = value!;
                      if (selectedValue == 5) {
                        enableEnam = false;
                        enableTujuh = false;
                      } else if (selectedValue == 6) {
                        enableEnam = true;
                        enableTujuh = false;
                      } else if (selectedValue == 7) {
                        enableEnam = true;
                        enableTujuh = true;
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
              TextFormField(
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
              ),
              TextFormField(
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
              ),
              enableEnam
                  ? TextFormField(
                      enabled: enableEnam,
                      cursorColor: Theme.of(context).cursorColor,
                      maxLength: 10,
                      keyboardType: TextInputType.number,
                      decoration: InputDecoration(
                        icon: Icon(Icons.border_color),
                        labelText: 'IPS Semester 6',
                        labelStyle: TextStyle(
                          color: Colors.blue[400],
                        ),
                        enabledBorder: UnderlineInputBorder(
                          borderSide: BorderSide(color: Colors.blue),
                        ),
                      ),
                    )
                  : SizedBox(),
              enableTujuh
                  ? TextFormField(
                      enabled: enableTujuh,
                      cursorColor: Theme.of(context).cursorColor,
                      maxLength: 10,
                      keyboardType: TextInputType.number,
                      decoration: InputDecoration(
                        icon: Icon(Icons.border_color),
                        labelText: 'IPS Semester 7',
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
