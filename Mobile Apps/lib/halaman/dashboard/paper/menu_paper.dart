import 'package:flutter/material.dart';
import 'package:compest_artificialifelse/api/api.dart';
import 'package:fluttertoast/fluttertoast.dart';

class MenuPaper extends StatefulWidget {
  MenuPaper({Key? key}) : super(key: key);

  @override
  _MenuPaper createState() => _MenuPaper();
}

class _MenuPaper extends State<MenuPaper> {
  int selectedValue = 1;

  TextEditingController judul = TextEditingController();
  TextEditingController abstrak = TextEditingController();

  String tema = "";

  void _cekJurnal() async {
    Api.cekJurnal(judul.text, abstrak.text, selectedValue).then((value) {
      setState(() {
        tema = value.theme;
        print(tema);
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
              getAppBarUI(),
              TextFormField(
                controller: judul,
                cursorColor: Theme.of(context).cursorColor,
                textCapitalization: TextCapitalization.sentences,
                maxLines: null,
                keyboardType: TextInputType.multiline,
                decoration: InputDecoration(
                  icon: Icon(Icons.book),
                  labelText: 'Judul Paper',
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
                height: 12,
              ),
              TextFormField(
                controller: abstrak,
                cursorColor: Theme.of(context).cursorColor,
                textCapitalization: TextCapitalization.sentences,
                maxLines: null,
                keyboardType: TextInputType.multiline,
                decoration: InputDecoration(
                  icon: Icon(Icons.border_color),
                  labelText: 'Abkstaksi Paper',
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
                height: 12,
              ),
              DropdownButton(
                  value: selectedValue,
                  items: [
                    DropdownMenuItem(
                      child: Text("Bahasa Inggris"),
                      value: 1,
                    ),
                    DropdownMenuItem(
                      child: Text("Bahasa Indonesia"),
                      value: 2,
                    ),
                  ],
                  onChanged: (int? value) {
                    setState(() {
                      selectedValue = value!;
                    });
                  }),
              SizedBox(
                height: 36,
              ),
              RaisedButton(
                onPressed: () {
                  if (abstrak.text.length > 50 && judul.text != "") {
                    _cekJurnal();
                  } else {
                    Fluttertoast.showToast(
                        msg: "Judul dan Abstraksi yang kamu inputkan salah!",
                        toastLength: Toast.LENGTH_SHORT,
                        backgroundColor: Colors.red,
                        webShowClose: false);
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
                'Paper yang kamu maksud bertema : $tema',
                style: TextStyle(
                  fontSize: 18,
                  letterSpacing: 0.27,
                  color: Colors.black,
                  fontWeight: FontWeight.bold,
                ),
              ),
              SizedBox(
                height: 36,
              ),
            ],
          ),
        ),
      ),
    );
  }

  Widget getAppBarUI() {
    return Padding(
      padding: const EdgeInsets.only(left: 18, right: 18, bottom: 18),
      child: Row(
        children: <Widget>[
          Expanded(
            child: Column(
              mainAxisAlignment: MainAxisAlignment.end,
              crossAxisAlignment: CrossAxisAlignment.start,
              children: <Widget>[
                SizedBox(
                  height: 36,
                ),
                Text(
                  'Klasifikasikan Papermu!',
                  textAlign: TextAlign.left,
                  style: TextStyle(
                    fontWeight: FontWeight.bold,
                    fontSize: 18,
                    letterSpacing: 0.27,
                    color: Colors.black87,
                  ),
                ),
              ],
            ),
          ),
        ],
      ),
    );
  }
}
