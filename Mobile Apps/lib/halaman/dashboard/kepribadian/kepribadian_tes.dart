import 'dart:convert';

import 'package:flutter/material.dart';
import 'package:compest_artificialifelse/api/api.dart';
import 'package:compest_artificialifelse/api/kepribadian/soal.dart';

class KepribadianTes extends StatefulWidget {
  KepribadianTes({Key? key}) : super(key: key);

  @override
  _KepribadianTes createState() => _KepribadianTes();
}

class _KepribadianTes extends State<KepribadianTes> {
  double _currentSliderValue = 0;
  var _soal = <Data>[];

  void _getSoal() async {
    Api.getSoal().then((value) {
      setState(() {
        _soal = value.data;
        print(_soal);
      });
    }).catchError((err) {
      print(err);
    });
  }

  @override
  initState() {
    super.initState();
    _getSoal();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Container(
        padding: EdgeInsets.all(30),
        child: SingleChildScrollView(
          child: Expanded(
            child: ListView.builder(
                itemCount: _soal.length,
                itemBuilder: (context, index) {
                  return Column(
                    crossAxisAlignment: CrossAxisAlignment.start,
                    children: <Widget>[
                      Text("Apakah anda kuat?"),
                      Slider(
                        value: _currentSliderValue,
                        min: -2,
                        max: 2,
                        divisions: 4,
                        label: _currentSliderValue.round().toString(),
                        onChanged: (double value) {
                          setState(() {
                            _currentSliderValue = value;
                          });
                        },
                      ),
                      SizedBox(
                        height: 12,
                      ),
                    ],
                  );
                }),
          ),
        ),
      ),
    );
  }
}
