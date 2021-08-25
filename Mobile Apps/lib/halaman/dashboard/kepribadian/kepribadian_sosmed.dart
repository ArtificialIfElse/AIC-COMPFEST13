import 'package:flutter/material.dart';

class KepribadianSosmed extends StatefulWidget {
  KepribadianSosmed({Key? key}) : super(key: key);

  @override
  _KepribadianSosmed createState() => _KepribadianSosmed();
}

class _KepribadianSosmed extends State<KepribadianSosmed> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Container(
        padding: EdgeInsets.all(30),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: <Widget>[
            SizedBox(
              height: 36,
            ),
            TextFormField(
              cursorColor: Theme.of(context).cursorColor,
              maxLength: 100,
              decoration: InputDecoration(
                icon: Icon(Icons.person),
                labelText: 'Username Twitter',
                labelStyle: TextStyle(
                  color: Colors.blue[400],
                ),
                helperText: 'Panjang teks',
                enabledBorder: UnderlineInputBorder(
                  borderSide: BorderSide(color: Colors.blue),
                ),
              ),
            ),
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
                  constraints: BoxConstraints(maxWidth: 500.0, minHeight: 50.0),
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
          ],
        ),
      ),
    );
  }
}
