import 'package:flutter/material.dart';
import 'package:flutter_radar_chart/flutter_radar_chart.dart';

class DetailHasil extends StatefulWidget {
  final String tipe, jurusan;
  final List<String> advice;
  final List<List<int>> data;
  const DetailHasil({
    Key? key,
    required this.tipe,
    required this.jurusan,
    required this.advice,
    required this.data,
  }) : super(key: key);

  @override
  _DetailHasil createState() => _DetailHasil();
}

class _DetailHasil extends State<DetailHasil> {
  var ticks = [10, 20, 30, 40, 50];
  var features = ["NEU", "OPN", "AGR", "CSN", "EXT"];

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Container(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.start,
          crossAxisAlignment: CrossAxisAlignment.start,
          children: <Widget>[
            Expanded(
                child: Padding(
              padding: EdgeInsets.all(30),
              child: Column(
                children: <Widget>[
                  SizedBox(
                    height: 24,
                  ),
                  Text(
                    'Hasil prediksi kepribadianmu ${widget.tipe}',
                    style: TextStyle(
                      fontSize: 16,
                      color: Colors.black,
                      fontWeight: FontWeight.bold,
                    ),
                  ),
                  SizedBox(
                    height: 12,
                  ),
                  Text(
                    'Jurusan yang cocok untukmu adalah ${widget.jurusan}',
                    style: TextStyle(
                      fontSize: 14,
                      letterSpacing: 0.27,
                      color: Colors.black,
                    ),
                  ),
                ],
              ),
            )),
            Expanded(
              child: RadarChart.light(
                ticks: ticks,
                features: features,
                data: widget.data,
                useSides: true,
              ),
            ),
            Padding(
              padding: EdgeInsets.all(30),
              child: Column(
                children: <Widget>[
                  Text(
                    "NEU : Neuroticism, OPN : Openness, AGR : Agreeableness, CSN : Conscientiousness, EXT : Extroversion\n\n",
                    style: TextStyle(fontSize: 12),
                  ),
                  Text(
                    "Penjelasan Grafik : ",
                    style: TextStyle(fontWeight: FontWeight.bold),
                  ),
                ],
              ),
            ),
            Expanded(
              child: Padding(
                padding: EdgeInsets.only(left: 20, right: 20),
                child: Card(
                  shape: RoundedRectangleBorder(
                    borderRadius: BorderRadius.circular(16.0),
                  ),
                  color: Color(0xff27C499),
                  child: Padding(
                    padding: EdgeInsets.all(15),
                    child: SingleChildScrollView(
                      child: Column(
                        children: <Widget>[
                          Text(
                            '1. ${widget.advice[0]}\n2.${widget.advice[1]}\n3. ${widget.advice[2]}\n4. ${widget.advice[3]}\n5. ${widget.advice[4]}',
                            style: TextStyle(
                              fontSize: 14,
                              letterSpacing: 0.27,
                              color: Colors.white,
                            ),
                          ),
                        ],
                      ),
                    ),
                  ),
                ),
              ),
            ),
            SizedBox(
              height: 16,
            ),
          ],
        ),
      ),
    );
  }
}
