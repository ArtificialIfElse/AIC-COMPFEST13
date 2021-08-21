import 'package:flutter/material.dart';

class MenuPaper extends StatefulWidget {
  MenuPaper({Key? key}) : super(key: key);

  @override
  _MenuPaper createState() => _MenuPaper();
}

class _MenuPaper extends State<MenuPaper> {
  int selectedValue = 1;

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Container(
        padding: EdgeInsets.all(30),
        child: SingleChildScrollView(
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: <Widget>[
              TextFormField(
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
