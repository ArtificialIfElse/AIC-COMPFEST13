import 'package:flutter/material.dart';
import 'package:compest_artificialifelse/api/api.dart';
import 'package:compest_artificialifelse/api/kepribadian/soal_respon.dart';
import 'detail_hasil.dart';

class KepribadianTes extends StatefulWidget {
  KepribadianTes({Key? key}) : super(key: key);

  @override
  _KepribadianTes createState() => _KepribadianTes();
}

class _KepribadianTes extends State<KepribadianTes> {
  var _soal = <Data>[];

  List<String> advice = [];
  String mbti = "";
  String message = "";
  double neuroticism = 0.0;
  double openness = 0.0;
  double agreeableness = 0.0;
  double conscientiousness = 0.0;
  double extroversion = 0.0;
  String recommendationMajor = "";

  var features = [
    "neuroticism",
    "openness",
    "agreeableness",
    "conscientiousness",
    "extroversion"
  ];

  void _getSoal() async {
    Api.getSoal().then((value) {
      setState(() {
        _soal = value.data;
      });
    }).catchError((err) {
      print(err);
    });
  }

  void _cekKepribadian(List<double> jawaban) async {
    Api.cekKepribadian(jawaban).then((value) {
      setState(() {
        mbti = value.mbti;
        recommendationMajor = value.recommendationMajor;
        advice = value.advice;
        agreeableness = value.agreeableness;
        conscientiousness = value.conscientiousness;
        extroversion = value.extroversion;
        neuroticism = value.neuroticism;
        openness = value.openness;
        Navigator.push(
          context,
          MaterialPageRoute(
            builder: (context) => DetailHasil(
              tipe: mbti,
              jurusan: recommendationMajor,
              advice: advice,
              data: [
                [
                  (neuroticism * 10) as int,
                  (openness * 10) as int,
                  (agreeableness * 10) as int,
                  (conscientiousness * 10) as int,
                  (extroversion * 10) as int
                ],
              ],
            ),
          ),
        );
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
      body: Column(
        children: <Widget>[
          getAppBarUI(),
          Expanded(
            child: new ListView.builder(
                itemCount: _soal.length,
                itemBuilder: (context, index) {
                  return Padding(
                    padding: EdgeInsets.only(left: 40, right: 40),
                    child: Column(
                      crossAxisAlignment: CrossAxisAlignment.start,
                      children: <Widget>[
                        Text('${index + 1}. ${_soal[index].soal} ?'),
                        Slider(
                          value: _soal[index].value_slider,
                          min: -2,
                          max: 2,
                          divisions: 4,
                          label: _soal[index].value_slider.round().toString(),
                          onChanged: (double value) {
                            setState(() {
                              _soal[index].value_slider = value;
                            });
                          },
                        ),
                        _soal.length == index + 1
                            ? SizedBox(
                                height: 36,
                              )
                            : SizedBox(),
                        _soal.length == index + 1
                            ? RaisedButton(
                                onPressed: () {
                                  List<double> jawaban = [];
                                  for (final item in _soal) {
                                    jawaban.add(item.value_slider);
                                  }
                                  print(jawaban);
                                  _cekKepribadian(jawaban);
                                },
                                shape: RoundedRectangleBorder(
                                    borderRadius: BorderRadius.circular(80.0)),
                                padding: EdgeInsets.all(0.0),
                                child: Ink(
                                  decoration: BoxDecoration(
                                      gradient: LinearGradient(
                                        colors: [
                                          Color(0xff374ABE),
                                          Color(0xff64B6FF)
                                        ],
                                        begin: Alignment.centerLeft,
                                        end: Alignment.centerRight,
                                      ),
                                      borderRadius:
                                          BorderRadius.circular(30.0)),
                                  child: Container(
                                    constraints: BoxConstraints(
                                        maxWidth: 500.0, minHeight: 50.0),
                                    alignment: Alignment.center,
                                    child: Text(
                                      "Prediksi",
                                      textAlign: TextAlign.center,
                                      style: TextStyle(
                                          color: Colors.white, fontSize: 14),
                                    ),
                                  ),
                                ),
                              )
                            : SizedBox(),
                        SizedBox(
                          height: 46,
                        ),
                      ],
                    ),
                  );
                }),
          ),
        ],
      ),
    );
  }

  Widget getAppBarUI() {
    return Padding(
      padding: const EdgeInsets.only(top: 8.0, left: 18, right: 18),
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
                  'Jawablah Pertanyaan Berikut!',
                  textAlign: TextAlign.left,
                  style: TextStyle(
                    fontWeight: FontWeight.bold,
                    fontSize: 18,
                    letterSpacing: 0.27,
                    color: Colors.black87,
                  ),
                ),
                SizedBox(
                  height: 24,
                ),
              ],
            ),
          ),
          Container(
            width: 60,
            height: 60,
          )
        ],
      ),
    );
  }
}
